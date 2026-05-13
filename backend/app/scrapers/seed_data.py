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

    # ── SANTANDER — datos reales verificados (mayo 2026) ────────────────────
    {
        "title": "30% de reintegro en Coto los lunes — Santander",
        "description": (
            "Reintegro pagando con MODO desde la app Santander o app MODO "
            "con tarjeta Santander Visa crédito o débito. Tope $15.000 por semana."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 15000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/personas/beneficios",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "25% de reintegro en Carrefour los viernes — Santander",
        "description": (
            "Reintegro pagando con Visa Santander crédito o débito a través de MODO. "
            "Tope $20.000 por mes. No aplica en electrodomésticos ni carne vacuna."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 20000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/personas/beneficios",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "25% de descuento en Mostaza los miércoles — Super Miércoles",
        "description": (
            "Descuento en Mostaza todos los miércoles pagando con tarjetas Santander. "
            "Programa Super Miércoles. Tope $15.000 mensual. Vigente hasta 25/06/2026."
        ),
        "discount_type": "descuento",
        "percentage": 25.0,
        "max_amount": 15000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 6, 25),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/banco/online/personas/beneficios/volvieron-super-miercoles",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "15% en Yenny & El Ateneo los miércoles — Super Miércoles",
        "description": (
            "15% de descuento en Yenny y El Ateneo todos los miércoles con Santander. "
            "Tope $20.000 mensual. Incluye 3 cuotas sin interés. Vigente hasta 25/06/2026."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": 20000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "librerias",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 6, 25),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/banco/online/personas/beneficios/volvieron-super-miercoles",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "20% en jugueterías los miércoles sin tope — Super Miércoles",
        "description": (
            "20% de descuento en Mundo del Juguete los miércoles con Santander. "
            "Sin tope de reintegro. Incluye 3 cuotas sin interés. Vigente hasta 25/06/2026."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": None,
        "source": "Santander",
        "source_type": "banco",
        "category": "jugueterias",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 6, 25),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/banco/online/personas/beneficios/volvieron-super-miercoles",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "20% en neumáticos los miércoles sin tope — Super Miércoles",
        "description": (
            "20% de descuento en Neumáticos Juan los miércoles con Santander. "
            "Sin tope de reintegro. Incluye 3 cuotas sin interés. Vigente hasta 25/06/2026."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": None,
        "source": "Santander",
        "source_type": "banco",
        "category": "neumaticos",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 6, 25),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/banco/online/personas/beneficios/volvieron-super-miercoles",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "10% en YPF los jueves — Santander Select (Visa Black/Platinum)",
        "description": (
            "10% de descuento en YPF los jueves con Visa Black o Platinum Santander Select "
            "a través de la app YPF. Tope $7.500 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": 7500.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/banco/online/landings/supercuenta-combustible",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "30% de descuento en Cabify (mar y vie) — Santander",
        "description": (
            "30% de descuento en Cabify los martes y viernes pagando con "
            "tarjetas Santander. Tope $20.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 20000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "viajes",
        "days_of_week": "martes,viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/personas/beneficios",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "20% en farmacias los miércoles — Santander Visa Women",
        "description": (
            "20% de descuento en farmacias adheridas los miércoles con tarjeta "
            "Santander Visa Women crédito o débito. Tope $3.000–$8.000 según tipo de tarjeta."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 8000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/personas/beneficios",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    {
        "title": "50% en peluquerías (mar y vie) — Santander Visa Women",
        "description": (
            "50% de descuento en peluquerías adheridas los martes y viernes con "
            "Santander Visa Women. Tope $3.000–$8.000 por mes según tipo de tarjeta."
        ),
        "discount_type": "descuento",
        "percentage": 50.0,
        "max_amount": 8000.0,
        "source": "Santander",
        "source_type": "banco",
        "category": "peluquerias",
        "days_of_week": "martes,viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.santander.com.ar/personas/beneficios",
        "logo_url": "https://logo.clearbit.com/santander.com.ar",
    },
    # ── BBVA — datos reales verificados (mayo 2026) ─────────────────────────
    # Supermercados con QR MODO
    {
        "title": "20% de reintegro en Día (vie y sáb) — BBVA",
        "description": (
            "Reintegro pagando con QR MODO desde la app BBVA en Supermercado Día. "
            "Compra mínima $30.000. Tope $20.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 20000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "viernes,sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "20% de reintegro en Coto los martes — BBVA",
        "description": (
            "Reintegro pagando con QR MODO desde la app BBVA en Coto. "
            "Compra mínima $60.000. Tope $25.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "20% de reintegro en Jumbo (mar y jue) — BBVA",
        "description": (
            "Reintegro pagando con QR MODO desde la app BBVA en Jumbo. "
            "Compra mínima $100.000. Tope $25.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes,jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "20% de reintegro en Vea y Disco (vie–dom) — BBVA",
        "description": (
            "Reintegro pagando con QR MODO desde la app BBVA en Vea y Disco. "
            "Compra mínima $100.000. Tope $25.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "viernes,sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "25% de reintegro en Carrefour — BBVA (cuenta sueldo)",
        "description": (
            "Hasta 25% de reintegro en Carrefour con Visa BBVA y MODO "
            "para clientes que acreditan sueldo en BBVA. Tope $20.000 por semana."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 20000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # Gastronomía
    {
        "title": "20% de reintegro en restaurantes todos los días — BBVA a la Carta",
        "description": (
            "Reintegro pagando con NFC (Apple Pay, Google Pay o MODO contactless) "
            "en restaurantes adheridos: Kansas, Dandy, Burger54, Rock&Feller's, "
            "La Parolaccia y más. Tope $50.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 50000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "20% de reintegro en heladerías — BBVA",
        "description": (
            "Reintegro en Lucciano's y Rapanue pagando con NFC o MODO. "
            "Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # Indumentaria y Farmacias
    {
        "title": "20% de reintegro en indumentaria y farmacias — BBVA",
        "description": (
            "Reintegro en comercios de indumentaria y farmacias adheridas "
            "con tarjetas BBVA. Incluye 18 cuotas sin interés. "
            "Mínimo $75.000. Tope $15.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # Servicios públicos (jubilados)
    {
        "title": "50% de reintegro en servicios públicos — BBVA jubilados",
        "description": (
            "Reintegro del 50% en pagos de luz, gas, agua, teléfono, cable e internet "
            "mediante débito automático con tarjeta de crédito BBVA. "
            "Tope mensual: $6.000–$36.000 según tipo de cuenta. Vigente hasta 30/06/2026."
        ),
        "discount_type": "reintegro",
        "percentage": 50.0,
        "max_amount": 36000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "servicios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/personas/productos/jubilados.html",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # NFC primeras compras
    {
        "title": "100% de reintegro en tus primeras 3 compras NFC — BBVA",
        "description": (
            "Reintegro del 100% en las primeras 3 compras pagando con NFC "
            "(Apple Pay o Google Pay) con tarjeta de crédito BBVA. "
            "Tope $10.000 por compra. Vigente hasta 30/06/2026."
        ),
        "discount_type": "reintegro",
        "percentage": 100.0,
        "max_amount": 10000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": True,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/personas/servicios-digitales/app-bbva/nfc.html",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # Duty Free
    {
        "title": "20% de reintegro en Duty Free — BBVA",
        "description": (
            "Reintegro en tiendas Duty Free de aeropuertos pagando con "
            "NFC o MODO con tarjetas BBVA. Tope $25.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    # Hot Sale 2026 (11-17 mayo)
    {
        "title": "20% de reintegro en electro y hogar — BBVA Hot Sale 2026",
        "description": (
            "Hot Sale (11–17/05): 20% de reintegro + hasta 18 cuotas sin interés "
            "en Samsung, Frávega y electro/hogar adheridos pagando con MODO desde app BBVA. "
            "Tope $30.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 30000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 17),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com.ar/beneficios/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "20% en vuelos a Miami y Cancún — BBVA Hot Sale 2026",
        "description": (
            "Hot Sale (11–17/05): 20% de descuento en vuelos Aerolíneas Argentinas "
            "a Miami y Cancún con tarjetas BBVA. Hoteles Orlando/Miami 20% tope $145.000. "
            "Hyatt Cancún 15%."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 145000.0,
        "source": "BBVA",
        "source_type": "banco",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 17),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com/es/ar/economia-y-finanzas/hot-sale-2026-con-bbva-viajes-turismo-electro-y-tecnologia/",
        "logo_url": "https://logo.clearbit.com/bbva.com.ar",
    },
    {
        "title": "Hasta 55% de descuento en Assist Card — BBVA Hot Sale 2026",
        "description": (
            "Hot Sale (11–17/05): hasta 55% de descuento en asistencia al viajero "
            "Assist Card para viajes a México, USA y Canadá con tarjetas BBVA. "
            "Incluye 12 cuotas sin interés."
        ),
        "discount_type": "descuento",
        "percentage": 55.0,
        "max_amount": None,
        "source": "BBVA",
        "source_type": "banco",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 17),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bbva.com/es/ar/economia-y-finanzas/hot-sale-2026-con-bbva-viajes-turismo-electro-y-tecnologia/",
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
