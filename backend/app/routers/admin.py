"""
Endpoints de administración protegidos por SCRAPER_TOKEN.
Solo GitHub Actions y Render pueden llamarlos.
"""

import os
import logging
from fastapi import APIRouter, HTTPException, Header, BackgroundTasks
from typing import Optional

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/admin", tags=["admin"])


def _verify_token(authorization: Optional[str]):
    token = os.environ.get("SCRAPER_TOKEN", "")
    if not token:
        raise HTTPException(status_code=503, detail="SCRAPER_TOKEN no configurado en el servidor")
    expected = f"Bearer {token}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="Token inválido o ausente")


@router.post("/run-scraper", status_code=202)
async def run_scraper(
    background_tasks: BackgroundTasks,
    authorization: Optional[str] = Header(None),
):
    """
    Dispara el scraper semanal en background.
    Requiere: Authorization: Bearer <SCRAPER_TOKEN>
    Devuelve 202 inmediatamente — el scraping corre en segundo plano.
    """
    _verify_token(authorization)

    def _run():
        from app.scrapers.orchestrator import run_all_scrapers
        try:
            run_all_scrapers()
        except Exception as e:
            logger.error(f"[SCRAPER] Error fatal en run_all_scrapers: {e}")

    background_tasks.add_task(_run)
    logger.info("[ADMIN] Scraper semanal iniciado via endpoint")
    return {"status": "started", "message": "Scraper ejecutándose en segundo plano"}


@router.get("/scraper-status")
def scraper_status(authorization: Optional[str] = Header(None)):
    """Estado básico: verifica que el servidor y la API key estén configurados."""
    _verify_token(authorization)
    api_key_ok = bool(os.environ.get("ANTHROPIC_API_KEY"))
    return {
        "server": "ok",
        "anthropic_api_key": "configurada" if api_key_ok else "FALTA — configurar en Render",
        "scraper_token": "configurado",
    }
