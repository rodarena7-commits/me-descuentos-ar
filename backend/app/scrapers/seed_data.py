"""
Datos de seed para desarrollo.
Galicia: datos reales verificados (mayo 2026).
Otros bancos/fintechs: datos de ejemplo — reemplazar con scrapers reales.
"""
from datetime import datetime, timedelta

_HOY = datetime(2026, 5, 13)

SAMPLE_DISCOUNTS = [
    # ── BANCO GALICIA — COMBUSTIBLE ──────────────────────────────────────────
    {
        "title": "10% de descuento en combustible los lunes",
        "description": (
            "Con Mastercard Galicia crédito en YPF, Shell, Axion y Puma Energy. "
            "Tope $10.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": 10000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones/promocion-combustible",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },
    {
        "title": "15% de descuento en combustible los lunes — Éminent",
        "description": (
            "Clientes Éminent: 15% en YPF y Shell con Mastercard Galicia crédito. "
            "Tope $15.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": 15000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones/promocion-combustible",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },
    {
        "title": "20% de reintegro en Axion pagando con MODO",
        "description": (
            "20% de reintegro en Axion Energy los lunes usando la app MODO "
            "con tarjetas Galicia. Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones/promocion-combustible",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },

    # ── BANCO GALICIA — SUPERMERCADOS ────────────────────────────────────────
    {
        "title": "25% de reintegro en Coto Digital los jueves",
        "description": (
            "Reintegro en cotoonline.com.ar con Amex Galicia crédito en 1 cuota. "
            "Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 15000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },
    {
        "title": "30% de reintegro en Coto Digital los jueves — Éminent",
        "description": (
            "Clientes Éminent: 30% de reintegro en Coto Digital cada jueves "
            "con Amex Galicia. Tope $20.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 20000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },
    {
        "title": "25% de reintegro en Cooperativa Obrera los viernes",
        "description": (
            "Reintegro en supermercado, bazar y textil de Cooperativa Obrera "
            "con Mastercard Galicia crédito en 1 cuota. "
            "+10% adicional si cobrás sueldo en Galicia. Tope $10.000/mes "
            "($15.000 Éminent)."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 10000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cooperativaobrera.coop/financiacion-y-promos-bancarias/banco-galicia.html",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },

    # ── BANCO GALICIA — FARMACIAS ────────────────────────────────────────────
    {
        "title": "25% de reintegro en Farmacity los jueves",
        "description": (
            "Reintegro en Farmacity presencial y online escaneando QR MODO con "
            "Visa Débito Galicia. Tope $10.000 por mes. Vigente hasta 27/08/2026."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 10000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 8, 27),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },

    # ── BANCO GALICIA — HOT SALE 2026 ────────────────────────────────────────
    {
        "title": "20% de reintegro — Hot Sale 2026 (Farmacity y más)",
        "description": (
            "20% de reintegro en Farmacity, The Food Market, Simplicity y Get The Look "
            "con tarjetas Galicia. Tope $15.000. Incluye 3 cuotas sin interés."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "varios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 15),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },
    {
        "title": "Hasta $50.000 de reintegro en Almundo — Hot Sale Éminent",
        "description": (
            "Clientes Éminent: hasta $50.000 de reintegro en Almundo "
            "más 12 cuotas sin interés. Promoción Hot Sale 2026."
        ),
        "discount_type": "reintegro",
        "percentage": None,
        "max_amount": 50000.0,
        "source": "Banco Galicia",
        "source_type": "banco",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 15),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.galicia.ar/personas/promociones",
        "logo_url": "https://logo.clearbit.com/galicia.ar",
    },

    # ── OTROS BANCOS — datos de ejemplo (reemplazar con scrapers) ────────────
    {
        "title": "20% reintegro en combustible con Santander",
        "description": "Reintegro en YPF, Shell, Axion con tarjetas Santander.",
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 2000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "todos",
        "valid_until": _HOY + timedelta(days=15),
        "is_limited_stock": False,
        "is_new": False,
        "is_active": True,
        "url": "https://www.santander.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "25% OFF en farmacias los miércoles — BBVA",
        "description": "Descuento en Farmacity con BBVA.",
        "discount_type": "descuento",
        "percentage": 25.0,
        "max_amount": 1500.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "miercoles",
        "valid_until": _HOY + timedelta(days=20),
        "is_limited_stock": False,
        "is_new": False,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # ── BANCO NACIÓN / BNA+ — datos reales verificados (mayo 2026) ──────────
    {
        "title": "30% de reintegro en supermercados los miércoles — BNA+",
        "description": (
            "Reintegro pagando con QR MODO o BNA+ en Carrefour, Coto, Disco, Vea, "
            "Chango Más, Diarco, Maxiconsumo y Vital. Tope $12.000 por semana."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 12000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "20% de reintegro en Chango Más los lunes — BNA+",
        "description": (
            "Reintegro con tarjeta de crédito BNA+ en Chango Más. "
            "Mínimo de compra $75.000. Tope $25.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "20% de reintegro en Coto los martes — BNA+",
        "description": (
            "Reintegro con tarjeta de crédito BNA+ en Coto. "
            "Mínimo de compra $60.000. Tope $25.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "20% de reintegro en Disco, Vea y Jumbo (vie–dom) — BNA+",
        "description": (
            "Reintegro en Disco, Vea y Jumbo de viernes a domingo con BNA+. "
            "Mínimo de compra $100.000. Tope $25.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "viernes,sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "20% de reintegro en Supermercado Día (vie–sáb) — BNA+",
        "description": (
            "Reintegro en Supermercado Día los viernes y sábados con BNA+. "
            "Mínimo de compra $35.000. Tope $20.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 20000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "viernes,sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "20% de reintegro en combustible los viernes — BNA+",
        "description": (
            "Reintegro en YPF, Shell, Axion Energy, Gulf y Dapsa los viernes "
            "con QR MODO o BNA+. Shell suma 5% adicional. Tope $10.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 10000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "50% de reintegro en transporte público — BNA+",
        "description": (
            "Reintegro en colectivos y subtes usando tarjeta Visa/Mastercard BNA+ "
            "con tecnología contactless. Tope $8.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 50.0,
        "max_amount": 8000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "transporte",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "10% en farmacias los lunes + 3 cuotas — BNA+",
        "description": (
            "10% de descuento en farmacias adheridas los lunes con BNA+, "
            "más 3 cuotas sin interés."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": None,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "20% de descuento en gastronomía — BNA+",
        "description": (
            "20% de descuento en restaurantes y gastronomía adherida todos los días "
            "con BNA+. Tope $10.000 por compra, máximo 5 transacciones por mes."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 10000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "10% en ópticas los jueves sin tope — BNA+",
        "description": (
            "10% de reintegro en ópticas adheridas los jueves con BNA+, "
            "sin tope de reintegro, más 3 cuotas sin interés."
        ),
        "discount_type": "reintegro",
        "percentage": 10.0,
        "max_amount": None,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "opticas",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "10% en librerías los sábados — BNA+",
        "description": (
            "10% de reintegro en librerías adheridas los sábados con BNA+, "
            "más 3 cuotas sin interés. Tope $10.000."
        ),
        "discount_type": "reintegro",
        "percentage": 10.0,
        "max_amount": 10000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "librerias",
        "days_of_week": "sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "Reintegro del 100% para empleados estatales — BNA+",
        "description": (
            "Reintegro del 100% para cuentas sueldo del Estado (Jefatura de Gabinete, "
            "CONICET y convenios específicos). Tope hasta $105.000. "
            "Acumula con otras promos del banco. Vigente hasta 03/07/2026."
        ),
        "discount_type": "reintegro",
        "percentage": 100.0,
        "max_amount": 105000.0,
        "source": "Banco Nación",
        "source_type": "banco",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 7, 3),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bna.com.ar/Personas/DescuentosYPromociones",
        "logo_url": "https://logo.clearbit.com/bna.com.ar",
    },
    {
        "title": "30% reintegro en indumentaria — Macro",
        "description": "Reintegro en tiendas de ropa y calzado con Macro.",
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 5000.0,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "sabado,domingo",
        "valid_until": _HOY + timedelta(days=10),
        "is_limited_stock": True,
        "is_new": False,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/macro.com.ar",
    },

    # ── FINTECHS — datos de ejemplo ──────────────────────────────────────────
    {
        "title": "10% de reintegro en todos los comercios — MercadoPago",
        "description": "Reintegro pagando con saldo en cuenta de MercadoPago.",
        "discount_type": "reintegro",
        "percentage": 10.0,
        "max_amount": 1000.0,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": _HOY + timedelta(days=7),
        "is_limited_stock": True,
        "is_new": False,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    {
        "title": "5% cashback en compras con Lemon",
        "description": "Cashback en crypto en todas tus compras con la tarjeta Lemon.",
        "discount_type": "reintegro",
        "percentage": 5.0,
        "max_amount": None,
        "source": "Lemon",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": _HOY + timedelta(days=60),
        "is_limited_stock": False,
        "is_new": False,
        "is_active": True,
        "url": "https://lemon.me/beneficios",
        "logo_url": "https://logo.clearbit.com/lemon.me",
    },
    {
        "title": "30% OFF los jueves en supermercados — Naranja X",
        "description": "30% OFF los jueves en supermercados con NaranjaX.",
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 2000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": _HOY + timedelta(days=20),
        "is_limited_stock": False,
        "is_new": False,
        "is_active": True,
        "url": "https://www.naranjax.com/beneficios",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "20% OFF en viajes pagando con MODO",
        "description": "20% OFF en plataformas de turismo pagando con MODO.",
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 10000.0,
        "source": "MODO",
        "source_type": "fintech",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": _HOY + timedelta(days=3),
        "is_limited_stock": True,
        "is_new": False,
        "is_active": True,
        "url": "https://www.modo.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/modo.com.ar",
    },
]
