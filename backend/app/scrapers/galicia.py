import asyncio
from datetime import datetime, timedelta
from typing import List, Dict
from playwright.async_api import async_playwright
import re


SOURCE = "Banco Galicia"
SOURCE_TYPE = "banco"
LOGO_URL = "https://logo.clearbit.com/bancogalicia.com"
BASE_URL = "https://www.bancogalicia.com"
BENEFITS_URL = "https://www.bancogalicia.com/personas/beneficios"


def _parse_percentage(text: str):
    match = re.search(r'(\d+(?:[.,]\d+)?)\s*%', text or '')
    if match:
        return float(match.group(1).replace(',', '.'))
    return None


def _parse_max_amount(text: str):
    match = re.search(r'(?:tope|hasta|máximo)[^\d]*\$\s*([\d.,]+)', text or '', re.IGNORECASE)
    if match:
        raw = match.group(1).replace('.', '').replace(',', '.')
        try:
            return float(raw)
        except ValueError:
            pass
    return None


def _infer_category(text: str) -> str:
    text_lower = (text or '').lower()
    categories = {
        'supermercados': ['supermercado', 'carrefour', 'coto', 'jumbo', 'dia', 'walmart', 'disco'],
        'combustible': ['combustible', 'nafta', 'ypf', 'shell', 'axion', 'puma'],
        'farmacias': ['farmacia', 'farmacity', 'del pueblo', 'ahorro'],
        'gastronomia': ['restaurant', 'gastronomía', 'comida', 'delivery', 'burger', 'mcdonald'],
        'indumentaria': ['ropa', 'indumentaria', 'calzado', 'moda', 'zara', 'h&m'],
        'viajes': ['viaje', 'turismo', 'hotel', 'vuelo', 'aerolinea', 'booking'],
        'electronica': ['electrodoméstico', 'tecnología', 'electrónica', 'garbarino', 'frávega'],
        'entretenimiento': ['cine', 'teatro', 'hulu', 'netflix', 'disney', 'spotify'],
    }
    for category, keywords in categories.items():
        if any(kw in text_lower for kw in keywords):
            return category
    return 'varios'


def _infer_days(text: str) -> str:
    text_lower = (text or '').lower()
    days_map = {
        'lunes': 'lunes', 'martes': 'martes', 'miércoles': 'miercoles',
        'miercoles': 'miercoles', 'jueves': 'jueves', 'viernes': 'viernes',
        'sábado': 'sabado', 'sabado': 'sabado', 'domingo': 'domingo',
    }
    found = [v for k, v in days_map.items() if k in text_lower]
    if found:
        return ','.join(dict.fromkeys(found))
    return 'todos'


def _parse_date(text: str):
    if not text:
        return None
    patterns = [
        (r'(\d{1,2})/(\d{1,2})/(\d{4})', lambda m: datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)))),
        (r'(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})', None),
    ]
    for pattern, parser in patterns:
        m = re.search(pattern, text, re.IGNORECASE)
        if m and parser:
            try:
                return parser(m)
            except Exception:
                pass
    return None


async def scrape_galicia() -> List[Dict]:
    results = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
        )
        page = await context.new_page()

        try:
            await page.goto(BENEFITS_URL, wait_until="domcontentloaded", timeout=30000)
            await page.wait_for_timeout(3000)

            cards = await page.query_selector_all('[class*="benefit"], [class*="promo"], [class*="descuento"], [class*="card"], article')

            for card in cards[:50]:
                try:
                    text = (await card.inner_text()).strip()
                    if len(text) < 20:
                        continue

                    link_el = await card.query_selector('a')
                    href = await link_el.get_attribute('href') if link_el else None
                    if href and not href.startswith('http'):
                        href = BASE_URL + href

                    percentage = _parse_percentage(text)
                    max_amount = _parse_max_amount(text)

                    discount_type = 'descuento'
                    if 'reintegro' in text.lower() or 'cashback' in text.lower():
                        discount_type = 'reintegro'
                    elif 'promoción' in text.lower() or 'promo' in text.lower():
                        discount_type = 'promocion'

                    lines = [l.strip() for l in text.split('\n') if l.strip()]
                    title = lines[0][:250] if lines else text[:250]
                    description = ' '.join(lines[1:3]) if len(lines) > 1 else None

                    results.append({
                        'title': title,
                        'description': description,
                        'discount_type': discount_type,
                        'percentage': percentage,
                        'max_amount': max_amount,
                        'source': SOURCE,
                        'source_type': SOURCE_TYPE,
                        'logo_url': LOGO_URL,
                        'url': href or BENEFITS_URL,
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
            print(f"[Galicia scraper] Error: {e}")
        finally:
            await browser.close()

    return results


def run_galicia_scraper() -> List[Dict]:
    return asyncio.run(scrape_galicia())
