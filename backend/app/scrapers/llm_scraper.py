"""
Scraper basado en LLM: fetchea la página de promos de cada entidad,
extrae el texto visible y lo procesa con Claude para obtener JSON estructurado.
"""

import os
import json
import logging
import httpx
from bs4 import BeautifulSoup
from anthropic import Anthropic

logger = logging.getLogger(__name__)

_client = None

def get_client() -> Anthropic:
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY no está configurada")
        _client = Anthropic(api_key=api_key)
    return _client


FETCH_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-AR,es;q=0.9,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
}

SYSTEM_PROMPT = """\
Sos un asistente especializado en extraer información de descuentos y promociones \
bancarias de Argentina. Analizás contenido de páginas web y devolvés datos estructurados.

Para cada promoción, descuento o reintegro encontrado extraé:
- title: título corto y descriptivo (máx 80 chars), incluí el nombre de la entidad al final (ej: "20% en Coto los martes — Banco X")
- description: descripción completa con todas las condiciones importantes
- discount_type: "descuento" (rebaja directa), "reintegro" (se devuelve después), o "promocion" (cuotas sin interés u otros)
- percentage: número flotante del porcentaje (ej: 20.0), null si no aplica
- max_amount: tope máximo en pesos argentinos como número (ej: 10000.0), null si no hay tope
- category: UNA categoría de esta lista: supermercados, combustible, farmacias, gastronomia, indumentaria, viajes, electronica, entretenimiento, servicios, educacion, hogar, transporte, varios
- days_of_week: días en minúsculas sin tildes separados por coma (lunes,martes,miercoles,jueves,viernes,sabado,domingo) o "todos"
- valid_until: fecha límite en formato YYYY-MM-DD, null si no se especifica
- url: URL de la promoción si está disponible, null si no

Respondé ÚNICAMENTE con un JSON array válido, sin texto adicional, sin markdown. \
Si no encontrás promociones, respondé con [].
"""


def fetch_page_text(url: str, timeout: int = 20) -> str:
    """Fetchea la URL y devuelve el texto visible extraído con BeautifulSoup."""
    try:
        with httpx.Client(headers=FETCH_HEADERS, timeout=timeout, follow_redirects=True) as client:
            resp = client.get(url)
            resp.raise_for_status()
    except Exception as e:
        logger.warning(f"fetch_page_text error para {url}: {e}")
        return ""

    soup = BeautifulSoup(resp.text, "lxml")

    # Eliminar scripts, estilos, nav y footer que no aportan info de promos
    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    # Limpiar líneas vacías y límitar a 12.000 chars para no exceder el contexto
    lines = [l for l in text.splitlines() if l.strip()]
    text = "\n".join(lines)[:12000]
    return text


def extract_with_claude(text: str, entity_name: str, entity_url: str) -> list[dict]:
    """Envía el texto a Claude y devuelve lista de discounts estructurados."""
    if not text or len(text) < 100:
        logger.info(f"{entity_name}: texto muy corto ({len(text)} chars), saltando")
        return []

    prompt = (
        f"Analizá el siguiente contenido de la página de promociones de {entity_name} "
        f"(URL: {entity_url}) y extraé TODAS las promociones vigentes.\n\n"
        f"Contenido:\n{text}"
    )

    try:
        msg = get_client().messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = msg.content[0].text.strip()

        # Limpiar markdown si Claude lo envuelve en ```json ... ```
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
            raw = raw.strip()

        data = json.loads(raw)
        if not isinstance(data, list):
            return []
        return data

    except json.JSONDecodeError as e:
        logger.error(f"{entity_name}: JSON inválido de Claude — {e}")
        return []
    except Exception as e:
        logger.error(f"{entity_name}: error Claude API — {e}")
        return []


def scrape_entity(entity: dict) -> list[dict]:
    """
    Pipeline completo para una entidad:
    fetch → extraer texto → Claude → lista de discounts.
    Agrega source, source_type y logo_url a cada item.
    """
    source = entity["source"]
    url = entity["url"]
    logger.info(f"[SCRAPER] Procesando {source} → {url}")

    text = fetch_page_text(url)
    discounts = extract_with_claude(text, source, url)

    # Enriquecer cada discount con metadata de la entidad
    enriched = []
    for d in discounts:
        if not isinstance(d, dict):
            continue
        d["source"] = source
        d["source_type"] = entity.get("source_type", "banco")
        d["logo_url"] = entity.get("logo_url", "")
        d["is_active"] = True
        d["is_new"] = True
        enriched.append(d)

    logger.info(f"[SCRAPER] {source}: {len(enriched)} promociones encontradas")
    return enriched
