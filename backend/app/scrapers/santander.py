"""
Scraper de beneficios de Banco Santander Argentina.
Páginas objetivo:
  - https://www.santander.com.ar/personas/beneficios
  - https://www.santander.com.ar/banco/online/personas/beneficios/volvieron-super-miercoles
"""
import asyncio
import re
from datetime import datetime, timedelta
from typing import List, Dict

from playwright.async_api import async_playwright

SOURCE = "Santander"
SOURCE_TYPE = "banco"
LOGO_URL = "https://logo.clearbit.com/santander.com.ar"
BASE_URL = "https://www.santander.com.ar"
BENEFITS_URLS = [
    "https://www.santander.com.ar/personas/beneficios",
    "https://www.santander.com.ar/banco/online/personas/beneficios/volvieron-super-miercoles",
]


def _parse_percentage(text: str):
    m = re.search(r'(\d+(?:[.,]\d+)?)\s*%', text or '')
    return float(m.group(1).replace(',', '.')) if m else None


def _parse_max_amount(text: str):
    m = re.search(r'(?:tope|hasta|máximo)[^\d]*\$\s*([\d.,]+)', text or '', re.IGNORECASE)
    if m:
        try:
            return float(m.group(1).replace('.', '').replace(',', '.'))
        except ValueError:
            pass
    return None


def _infer_category(text: str) -> str:
    t = (text or '').lower()
    mapping = {
        'supermercados': ['supermercado', 'carrefour', 'coto', 'jumbo', 'dia', 'disco', 'vea', 'walmart'],
        'combustible':   ['combustible', 'nafta', 'ypf', 'shell', 'axion', 'puma', 'gasoil'],
        'farmacias':     ['farmacia', 'farmacity', 'del pueblo'],
        'gastronomia':   ['restaurant', 'gastronomía', 'comida', 'mostaza', 'burger', 'gourmet', 'ruta gourmet'],
        'indumentaria':  ['ropa', 'indumentaria', 'calzado', 'moda'],
        'viajes':        ['viaje', 'hotel', 'vuelo', 'aerolinea', 'turismo', 'cabify', 'uber'],
        'electronica':   ['electro', 'tecnología', 'garbarino', 'frávega'],
        'entretenimiento': ['cine', 'teatro', 'netflix', 'spotify'],
        'librerias':     ['librería', 'libro', 'yenny', 'ateneo'],
        'jugueterias':   ['juguete', 'juguetería'],
        'neumaticos':    ['neumático', 'goma', 'cubierta'],
        'peluquerias':   ['peluquería', 'pelo', 'beauty'],
    }
    for cat, kws in mapping.items():
        if any(kw in t for kw in kws):
            return cat
    return 'varios'


def _infer_days(text: str) -> str:
    t = (text or '').lower()
    days_map = {
        'lunes': 'lunes', 'martes': 'martes', 'miércoles': 'miercoles',
        'miercoles': 'miercoles', 'jueves': 'jueves', 'viernes': 'viernes',
        'sábado': 'sabado', 'sabado': 'sabado', 'domingo': 'domingo',
    }
    found = list(dict.fromkeys(v for k, v in days_map.items() if k in t))
    return ','.join(found) if found else 'todos'


def _infer_type(text: str) -> str:
    t = (text or '').lower()
    if 'reintegro' in t or 'cashback' in t or 'devolución' in t:
        return 'reintegro'
    if 'promo' in t:
        return 'promocion'
    return 'descuento'


async def scrape_santander() -> List[Dict]:
    results = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
        )

        for url in BENEFITS_URLS:
            page = await context.new_page()
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await page.wait_for_timeout(3000)

                cards = await page.query_selector_all(
                    '[class*="benefit"], [class*="promo"], [class*="card"], '
                    '[class*="descuento"], [class*="oferta"], article, section'
                )

                for card in cards[:60]:
                    try:
                        text = (await card.inner_text()).strip()
                        if len(text) < 20:
                            continue

                        link_el = await card.query_selector('a')
                        href = await link_el.get_attribute('href') if link_el else None
                        if href and not href.startswith('http'):
                            href = BASE_URL + href

                        lines = [l.strip() for l in text.split('\n') if l.strip()]
                        title = lines[0][:250] if lines else text[:250]
                        description = ' '.join(lines[1:3]) if len(lines) > 1 else None

                        results.append({
                            'title': title,
                            'description': description,
                            'discount_type': _infer_type(text),
                            'percentage': _parse_percentage(text),
                            'max_amount': _parse_max_amount(text),
                            'source': SOURCE,
                            'source_type': SOURCE_TYPE,
                            'logo_url': LOGO_URL,
                            'url': href or url,
                            'category': _infer_category(text),
                            'days_of_week': _infer_days(text),
                            'valid_until': datetime.utcnow() + timedelta(days=30),
                            'is_limited_stock': 'stock' in text.lower() or 'agotar' in text.lower(),
                            'is_new': True,
                            'is_active': True,
                        })
                    except Exception:
                        continue

            except Exception as e:
                print(f"[Santander scraper] Error en {url}: {e}")
            finally:
                await page.close()

        await browser.close()

    # Deduplicar por título
    seen = set()
    unique = []
    for r in results:
        key = r['title'][:60]
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique


def run_santander_scraper() -> List[Dict]:
    return asyncio.run(scrape_santander())
