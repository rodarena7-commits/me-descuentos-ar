"""
Orquestador del scraper semanal.
Procesa entidad por entidad, actualiza la DB y elimina vencidos.
"""

import logging
from datetime import datetime, date
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.discount import Discount
from app.scrapers.entities_config import ENTITIES
from app.scrapers.llm_scraper import scrape_entity

logger = logging.getLogger(__name__)


def _normalize_title(title: str) -> str:
    """Compara títulos ignorando mayúsculas y espacios extras."""
    return " ".join(title.lower().split())


def update_entity_in_db(db: Session, source: str, new_discounts: list[dict]) -> dict:
    """
    Actualiza la DB para una entidad:
    1. Elimina discounts vencidos (valid_until < hoy).
    2. Si Claude devolvió resultados, agrega los que no existen aún.
    Devuelve stats de la operación.
    """
    today = date.today()
    stats = {"added": 0, "deleted_expired": 0, "skipped": 0}

    # 1. Borrar vencidos
    expired = db.query(Discount).filter(
        Discount.source == source,
        Discount.valid_until != None,
        Discount.valid_until < datetime.combine(today, datetime.min.time()),
    ).all()
    for d in expired:
        db.delete(d)
    stats["deleted_expired"] = len(expired)

    # 2. Si Claude no trajo nada, no tocamos el resto
    if not new_discounts:
        db.commit()
        return stats

    # 3. Títulos existentes en DB para evitar duplicados
    existing = db.query(Discount.title).filter(Discount.source == source).all()
    existing_titles = {_normalize_title(r.title) for r in existing}

    # 4. Insertar solo los verdaderamente nuevos
    for d in new_discounts:
        title = d.get("title", "").strip()
        if not title:
            continue
        if _normalize_title(title) in existing_titles:
            stats["skipped"] += 1
            continue

        # Parsear valid_until si viene como string
        valid_until = None
        vu = d.get("valid_until")
        if vu:
            try:
                valid_until = datetime.strptime(vu[:10], "%Y-%m-%d")
            except (ValueError, TypeError):
                pass

        discount = Discount(
            title=title[:200],
            description=(d.get("description") or "")[:500],
            discount_type=d.get("discount_type", "descuento"),
            percentage=_safe_float(d.get("percentage")),
            max_amount=_safe_float(d.get("max_amount")),
            source=source,
            source_type=d.get("source_type", "banco"),
            logo_url=d.get("logo_url", ""),
            url=(d.get("url") or "")[:500],
            category=d.get("category", "varios"),
            days_of_week=d.get("days_of_week", "todos"),
            valid_until=valid_until,
            is_active=True,
            is_new=True,
        )
        db.add(discount)
        existing_titles.add(_normalize_title(title))
        stats["added"] += 1

    db.commit()
    return stats


def _safe_float(value) -> float | None:
    try:
        return float(value) if value is not None else None
    except (ValueError, TypeError):
        return None


def run_all_scrapers() -> dict:
    """
    Punto de entrada principal del scraper semanal.
    Procesa todas las entidades en secuencia y devuelve un resumen.
    """
    logger.info("=" * 60)
    logger.info(f"[SCRAPER] Iniciando actualización semanal — {datetime.now().isoformat()}")
    logger.info("=" * 60)

    db = SessionLocal()
    summary = {
        "started_at": datetime.now().isoformat(),
        "entities": [],
        "total_added": 0,
        "total_deleted": 0,
        "total_errors": 0,
    }

    try:
        for entity in ENTITIES:
            source = entity["source"]
            result = {"source": source, "status": "ok", "added": 0, "deleted_expired": 0, "error": None}

            try:
                new_discounts = scrape_entity(entity)
                stats = update_entity_in_db(db, source, new_discounts)
                result.update(stats)
                logger.info(
                    f"[OK] {source}: +{stats['added']} nuevos, "
                    f"-{stats['deleted_expired']} vencidos, "
                    f"{stats['skipped']} duplicados omitidos"
                )
            except Exception as e:
                result["status"] = "error"
                result["error"] = str(e)
                summary["total_errors"] += 1
                logger.error(f"[ERROR] {source}: {e}")

            summary["entities"].append(result)
            summary["total_added"] += result.get("added", 0)
            summary["total_deleted"] += result.get("deleted_expired", 0)

    finally:
        db.close()

    summary["finished_at"] = datetime.now().isoformat()
    logger.info("=" * 60)
    logger.info(
        f"[SCRAPER] Finalizado — "
        f"+{summary['total_added']} nuevos, "
        f"-{summary['total_deleted']} eliminados, "
        f"{summary['total_errors']} errores"
    )
    logger.info("=" * 60)
    return summary
