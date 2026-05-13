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
    # ── CUENTA DNI (Banco Provincia) — datos reales verificados (mayo 2026) ──
    {
        "title": "20% en comercios de cercanía lun–vie — Cuenta DNI",
        "description": (
            "20% de descuento de lunes a viernes en carnicerías, granjas, pescaderías "
            "y comercios de cercanía adheridos, pagando con QR o Clave DNI. "
            "Tope $5.000 por semana."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 5000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes,martes,miercoles,jueves,viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "40% en ferias y mercados bonaerenses todos los días — Cuenta DNI",
        "description": (
            "40% de reintegro en ferias y mercados de la provincia de Buenos Aires "
            "todos los días pagando con QR o Clave DNI. Tope $6.000 por semana."
        ),
        "discount_type": "reintegro",
        "percentage": 40.0,
        "max_amount": 6000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "40% en universidades, clubes y entidades educativas — Cuenta DNI",
        "description": (
            "40% de descuento todos los días en universidades, clubes deportivos "
            "y entidades educativas adheridas con QR o Clave DNI. "
            "Tope $6.000 por semana. Mínimo $15.000."
        ),
        "discount_type": "descuento",
        "percentage": 40.0,
        "max_amount": 6000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "educacion",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "25% en gastronomía los fines de semana — Cuenta DNI",
        "description": (
            "25% de descuento en restaurantes, bares y gastronomía adherida "
            "los sábados y domingos con QR o Clave DNI. "
            "Incluye Full YPF (gastronomía, NO combustible). Tope $8.000 por semana."
        ),
        "discount_type": "descuento",
        "percentage": 25.0,
        "max_amount": 8000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "30% en marcas destacadas todos los días — Cuenta DNI",
        "description": (
            "30% de descuento en marcas destacadas adheridas todos los días "
            "pagando con QR o Clave DNI. Tope $15.000 por mes. Mínimo $50.000."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 15000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "varios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "10% en Supermercado Día los lunes sin tope — Cuenta DNI",
        "description": (
            "10% de descuento en Supermercado Día los lunes "
            "pagando con QR o Clave DNI. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": None,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "20% en Chango Más los jueves sin tope — Cuenta DNI",
        "description": (
            "20% de descuento en Chango Más los jueves "
            "pagando con QR o Clave DNI. Sin tope de reintegro. Sin mínimo de compra."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": None,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "30% en Coto con NFC los jueves sin límite — Cuenta DNI",
        "description": (
            "30% de descuento en Coto los jueves pagando con NFC (pago sin contacto). "
            "Sin límite de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": None,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "10% en Carrefour los miércoles sin tope — Cuenta DNI",
        "description": (
            "10% de descuento en Carrefour los miércoles "
            "pagando con QR o Clave DNI. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": None,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "15% en supermercados adheridos (mar y mié) — Cuenta DNI",
        "description": (
            "15% de descuento martes y miércoles en supermercados del interior bonaerense "
            "adheridos (Josimar, Toledo y otros) con QR o Clave DNI. "
            "Mínimo $30.000. Tope $6.000 por semana."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": 6000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes,miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "10% en librerías los lunes y martes sin tope — Cuenta DNI",
        "description": (
            "10% de descuento en librerías de texto los lunes y martes "
            "con QR o Clave DNI. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": None,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "librerias",
        "days_of_week": "lunes,martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "10% en farmacias y perfumerías (mié y jue) sin tope — Cuenta DNI",
        "description": (
            "10% de descuento los miércoles y jueves en farmacias y perfumerías adheridas "
            "pagando con QR o Clave DNI. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": None,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "miercoles,jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "title": "+5% adicional en supermercados para jubilados — Cuenta DNI",
        "description": (
            "Jubilados y pensionados obtienen un 5% adicional de descuento "
            "en supermercados adheridos con Cuenta DNI. Tope unificado $5.000."
        ),
        "discount_type": "descuento",
        "percentage": 5.0,
        "max_amount": 5000.0,
        "source": "Cuenta DNI",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },

    # ── BANCO PATAGONIA (Patagonia ON) — datos reales verificados (mayo 2026) ─
    {
        "title": "30% en bares los viernes — Banco Patagonia",
        "description": (
            "30% de descuento en bares adheridos los viernes "
            "con tarjeta de crédito Mastercard Patagonia. Tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 10000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "50% en educación IT todos los días sin tope — Banco Patagonia",
        "description": (
            "50% de descuento en institutos de educación IT adheridos todos los días "
            "con débito o crédito Mastercard Patagonia. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 50.0,
        "max_amount": None,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "educacion",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "15% en Carrefour los miércoles — Banco Patagonia",
        "description": (
            "15% de descuento en Carrefour los miércoles "
            "con débito o crédito Mastercard Patagonia. Tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": 10000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "50% en cines los viernes — Banco Patagonia",
        "description": (
            "50% de descuento en cines adheridos los viernes "
            "con tarjeta de débito Mastercard Patagonia. Tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 50.0,
        "max_amount": 10000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "entretenimiento",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "20% en Havanna todos los días — Banco Patagonia",
        "description": (
            "20% de descuento en Havanna todos los días "
            "con crédito Mastercard Patagonia. Tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 10000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "20% en Farmacity los viernes — Banco Patagonia",
        "description": (
            "20% de descuento en Farmacity los viernes "
            "con crédito Mastercard Patagonia. Tope $20.000."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 20000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "20% en Get the Look los viernes — Banco Patagonia",
        "description": (
            "20% de descuento en Get the Look (indumentaria/belleza) los viernes "
            "con crédito Mastercard Patagonia. Tope $20.000."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 20000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "15% en Adidas, Stock Center y Dexter los jueves — Banco Patagonia",
        "description": (
            "15% de descuento en Adidas, Stock Center y Dexter los jueves "
            "con débito o crédito Mastercard Patagonia. Tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": 10000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "25% en Pedidos Ya los jueves — Banco Patagonia",
        "description": (
            "25% de descuento en Pedidos Ya los jueves "
            "con crédito Mastercard Patagonia. Tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 25.0,
        "max_amount": 10000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "title": "20–25% en combustible los jueves — Banco Patagonia",
        "description": (
            "20% de reintegro en combustible los jueves con tarjetas Patagonia "
            "(tope $10.000/mes). Clientes con cuenta sueldo: 25% (tope $15.000/mes). "
            "En YPF, Shell, Axion, Puma y Gulf."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "Banco Patagonia",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },

    # ── ICBC — datos reales verificados (mayo 2026) ─────────────────────────
    {
        "title": "20% en Coto los jueves sin tope — ICBC",
        "description": (
            "20% de reintegro en Coto todos los jueves pagando con Visa Débito ICBC. "
            "Sin tope de reintegro."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": None,
        "source": "ICBC",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "20% en Coto Digital los lunes — ICBC",
        "description": (
            "20% de reintegro en cotoonline.com.ar los lunes con tarjetas ICBC. "
            "Tope $15.000/mes (cuenta sueldo) o $10.000/mes (general)."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "ICBC",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "20% en Farmacity los viernes + 3 cuotas — ICBC",
        "description": (
            "20% de reintegro en Farmacity los viernes con Visa o Mastercard ICBC, "
            "más 3 cuotas sin interés. Tope $4.000 por compra."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 4000.0,
        "source": "ICBC",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "15% en Farmaonline los viernes con MODO — ICBC",
        "description": (
            "15% de reintegro en Farmaonline los viernes pagando con MODO "
            "con tarjetas ICBC. Tope $5.000 por transacción."
        ),
        "discount_type": "reintegro",
        "percentage": 15.0,
        "max_amount": 5000.0,
        "source": "ICBC",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "20% en gastronomía con MODO — ICBC",
        "description": (
            "20% de reintegro en restaurantes y gastronomía adherida pagando con MODO "
            "con tarjetas ICBC. Tope $15.000 por transacción. "
            "Exclusive Banking: 30%, tope $20.000."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 15000.0,
        "source": "ICBC",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "30% en combustible — ICBC",
        "description": (
            "30% de reintegro en combustible en estaciones adheridas "
            "con tarjetas ICBC. Tope $25.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 25000.0,
        "source": "ICBC",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "20% en Dexter + 6 cuotas — ICBC Exclusive Banking",
        "description": (
            "20% de reintegro en Dexter más 6 cuotas sin interés "
            "con tarjetas ICBC Exclusive Banking. "
            "Válido todos los días."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": None,
        "source": "ICBC",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "Hasta 18 cuotas + $50.000 de reintegro — ICBC Mall Hot Sale 2026",
        "description": (
            "Hot Sale (11–17/05): hasta 18 cuotas sin interés con tarjetas ICBC en ICBC Mall. "
            "Reintegro de hasta $50.000 pagando en 3 cuotas vía MODO o Mobile Banking. "
            "Envíos gratis y cupones acumulables."
        ),
        "discount_type": "reintegro",
        "percentage": None,
        "max_amount": 50000.0,
        "source": "ICBC",
        "source_type": "banco",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 17),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://mall.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "title": "50% en Gift Cards de moda — ICBC Mall Hot Sale 2026",
        "description": (
            "Hot Sale (11–17/05): hasta 50% de ahorro en Gift Cards de moda seleccionadas "
            "en ICBC Mall. Pagable en hasta 6 cuotas con tarjetas ICBC."
        ),
        "discount_type": "descuento",
        "percentage": 50.0,
        "max_amount": None,
        "source": "ICBC",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 17),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://mall.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
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
    # ── BANCO MACRO — datos reales verificados (mayo 2026) ──────────────────
    # Macro tiene dos segmentos: General/Platinum y Selecta (mayores beneficios)
    {
        "title": "20% de reintegro en supermercados con MODO — Banco Macro",
        "description": (
            "20% de reintegro en Coto (martes) y Jumbo, Vea, Disco "
            "pagando con MODO con tarjeta Visa Banco Macro. Tope $25.000 por mes. "
            "Mínimo $60.000 en Coto."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "Hasta 12 cuotas sin interés en Coto y Chango Más — Banco Macro",
        "description": (
            "De 2 a 12 cuotas sin interés todos los días en Coto y Chango Más "
            "con tarjetas Amex, Mastercard o Visa Banco Macro. Vigente hasta 30/06/2026."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "20–30% en YPF los miércoles — Banco Macro",
        "description": (
            "Miércoles en YPF: 20% de ahorro para clientes Platinum "
            "y 30% para Selecta con tarjetas Banco Macro. Tope $25.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 25000.0,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "20% en Farmacity + 3 cuotas sin interés — Banco Macro",
        "description": (
            "20% de descuento en Farmacity presencial y online "
            "con tarjeta Mastercard Banco Macro. Tope $20.000. "
            "3 cuotas sin interés pagando con QR."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 20000.0,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "Hasta 12 cuotas sin interés en electro — Banco Macro",
        "description": (
            "Hasta 12 cuotas sin interés todos los días en Cetrogar, Frávega y Megatone "
            "con tarjetas Amex, Mastercard o Visa Banco Macro. Vigente hasta 30/06/2026."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "Hasta 6 cuotas sin interés en indumentaria — Banco Macro",
        "description": (
            "Hasta 6 cuotas sin interés todos los días en Dexter, Caro Cuore y Devré "
            "con tarjetas Banco Macro en locales físicos. Vigente hasta 30/06/2026."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "Hasta 6 cuotas sin interés en Yenny — Banco Macro",
        "description": (
            "Hasta 6 cuotas sin interés todos los días en Yenny / El Ateneo "
            "con tarjetas Amex, Mastercard o Visa Banco Macro. Vigente hasta 31/05/2026."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "librerias",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "3 y 6 cuotas sin interés en gastronomía viüMi — Banco Macro",
        "description": (
            "3 y 6 cuotas sin interés en restaurantes y gastronomía adherida "
            "a través de viüMi con tarjetas Banco Macro. "
            "Vigente del 01/05/2026 al 31/05/2026. Excluye viajes y turismo."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/personas/viumi",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "title": "20% de descuento con MODO — Banco Macro Selecta (Hot Sale)",
        "description": (
            "Hot Sale (11–13/05): 20% de descuento pagando con MODO "
            "con tarjetas de crédito Macro Selecta. Tope $30.000. "
            "Tarjeta general/crédito: 10%, tope $10.000."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 30000.0,
        "source": "Banco Macro",
        "source_type": "banco",
        "category": "varios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 13),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },

    # ── MERCADOPAGO — datos reales verificados (mayo 2026) ──────────────────
    # Supermercados
    {
        "title": "15% en Supermercado Día los miércoles sin tope — MercadoPago",
        "description": (
            "15% de descuento en Supermercado Día todos los miércoles "
            "pagando con QR de MercadoPago. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    {
        "title": "15% en Chango Más los miércoles sin tope — MercadoPago",
        "description": (
            "15% de descuento en Chango Más, HiperChangoMás y Punto Mayorista "
            "todos los miércoles pagando con QR de MercadoPago. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    {
        "title": "Hasta 25% en supermercados (Carrefour, Coto, Vea) — MercadoPago",
        "description": (
            "Hasta 25% de descuento sin tope en supermercados adheridos "
            "(Carrefour, Coto, Vea, Chango Más) pagando con QR o tarjeta MercadoPago."
        ),
        "discount_type": "descuento",
        "percentage": 25.0,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Combustible
    {
        "title": "30% en combustible los lunes — MercadoPago",
        "description": (
            "30% de descuento en combustible todos los lunes "
            "pagando con tarjeta de crédito MercadoPago. Tope $6.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 6000.0,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "combustible",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Gastronomía
    {
        "title": "30% en McDonald's los viernes — MercadoPago",
        "description": (
            "30% de descuento en McDonald's todos los viernes "
            "pagando con QR o tarjeta MercadoPago. Tope $4.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 4000.0,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    {
        "title": "15% en Burger King los miércoles — MercadoPago",
        "description": (
            "15% de descuento en Burger King todos los miércoles "
            "pagando con QR de MercadoPago. Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Transporte
    {
        "title": "100% de reintegro en colectivo y subte — MercadoPago",
        "description": (
            "100% de reintegro en viajes de colectivo y subte pagando con QR "
            "de MercadoPago en líneas habilitadas. Solo para usuarios que activan "
            "la promo por primera vez en la app. Tope $8.000. Hasta 31/05/2026."
        ),
        "discount_type": "reintegro",
        "percentage": 100.0,
        "max_amount": 8000.0,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "transporte",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": True,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Entretenimiento
    {
        "title": "2x1 en Cinemark — MercadoPago",
        "description": (
            "2x1 en entradas de Cinemark pagando con QR o tarjeta MercadoPago. "
            "Consultá días y funciones habilitadas en la app."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "entretenimiento",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Viajes
    {
        "title": "Hasta 15% en vuelos y hoteles en Despegar — MercadoPago",
        "description": (
            "Hasta 15% de descuento en vuelos y hoteles nacionales e internacionales "
            "en Despegar pagando con MercadoPago. Incluye cuotas sin interés. "
            "Ofertas especiales durante Hot Sale."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    {
        "title": "Cuotas sin interés en Flechabus — MercadoPago",
        "description": (
            "Cuotas sin interés en pasajes de Flechabus "
            "pagando con tarjeta de crédito MercadoPago."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Indumentaria / Deportes
    {
        "title": "Cuotas y descuentos en Adidas (mejor los miércoles) — MercadoPago",
        "description": (
            "Financiación en cuotas sin interés en Adidas todos los días "
            "con tarjeta MercadoPago, con mejores condiciones los miércoles."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "indumentaria",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Farmacias
    {
        "title": "Descuentos en farmacias (Dr Ahorro, Selma) — MercadoPago",
        "description": (
            "Descuentos sin tope de reintegro en Farmacias Dr Ahorro y Farmacias Selma "
            "pagando con QR o tarjeta MercadoPago."
        ),
        "discount_type": "descuento",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "farmacias",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Hogar / Construcción
    {
        "title": "3 y 6 cuotas sin interés en Easy — MercadoPago",
        "description": (
            "3 y 6 cuotas sin interés en Easy (construcción, decoración y hogar) "
            "pagando con QR o tarjeta física MercadoPago."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "hogar",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Belleza / Cosmética
    {
        "title": "3 cuotas sin interés desde $55.000 en Natura — MercadoPago",
        "description": (
            "Hasta 3 cuotas sin interés en compras desde $55.000 en Natura "
            "pagando con QR o tarjeta física MercadoPago."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "peluquerias",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # Mercado Libre
    {
        "title": "Cuotas sin interés en Mercado Libre — MercadoPago",
        "description": (
            "3 cuotas sin interés en Mercado Libre y en comercios con QR MercadoPago "
            "para compras desde $50.000. Gestión 100% desde la app."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MercadoPago",
        "source_type": "fintech",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://logo.clearbit.com/mercadopago.com",
    },
    # ── RIPIO — datos reales verificados (2026) ─────────────────────────────
    # Ripio es una exchange/billetera crypto. El cashback se devuelve en UXD, ETH o BTC.
    # Tarjeta Visa prepaga, gratuita, sin costo de mantenimiento.
    {
        "title": "0.5% cashback en cripto pagando con pesos — Ripio Card Visa",
        "description": (
            "Con la Ripio Card Visa prepaga: 0.5% de cashback en UXD, ETH o BTC "
            "en cada compra pagando con pesos en cualquier comercio Visa del mundo. "
            "Se acredita en tu billetera Ripio. Tope $50.000 ARS por mes. "
            "Tarjeta gratuita, sin mantenimiento, envío gratis a todo el país."
        ),
        "discount_type": "reintegro",
        "percentage": 0.5,
        "max_amount": 50000.0,
        "source": "Ripio",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 12, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.ripio.com/ar/productos/ripio-card",
        "logo_url": "https://logo.clearbit.com/ripio.com",
    },
    {
        "title": "2% cashback en cripto pagando con crypto — Ripio Card Visa",
        "description": (
            "Con la Ripio Card Visa: 2% de cashback en UXD, ETH o BTC "
            "en cada compra pagando con criptomonedas en cualquier comercio Visa. "
            "Cashback instantáneo en tu billetera. Tope $50.000 ARS por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 2.0,
        "max_amount": 50000.0,
        "source": "Ripio",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 12, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.ripio.com/ar/productos/ripio-card",
        "logo_url": "https://logo.clearbit.com/ripio.com",
    },
    {
        "title": "4% cashback primeros 30 días — Ripio Card (nuevos usuarios)",
        "description": (
            "Nuevos en Ripio Card: 4% de cashback en UXD/ETH/BTC pagando con cripto "
            "y 1% pagando con pesos durante los primeros 30 días desde la activación. "
            "Tarjeta Visa prepaga, gratuita y sin costo de mantenimiento."
        ),
        "discount_type": "reintegro",
        "percentage": 4.0,
        "max_amount": 50000.0,
        "source": "Ripio",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 12, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.ripio.com/ar/productos/ripio-card",
        "logo_url": "https://logo.clearbit.com/ripio.com",
    },

    # ── LEMON — datos reales verificados (2026) ─────────────────────────────
    # Lemon es una billetera crypto. El cashback se devuelve siempre en BTC.
    {
        "title": "0.5% cashback en BTC en todas las compras con pesos — Lemon",
        "description": (
            "Con la Lemon Card Visa: 0.5% de cashback en Bitcoin en cada compra "
            "pagando con pesos en cualquier comercio del mundo que acepte Visa. "
            "Tope $40.000 ARS en BTC por mes. Se acredita en el acto en tu billetera."
        ),
        "discount_type": "reintegro",
        "percentage": 0.5,
        "max_amount": 40000.0,
        "source": "Lemon",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 12, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://lemon.me/tarjeta",
        "logo_url": "https://logo.clearbit.com/lemon.me",
    },
    {
        "title": "2% cashback en BTC pagando con cripto — Lemon Card",
        "description": (
            "Con la Lemon Card Visa: 2% de cashback en Bitcoin en cada compra "
            "pagando con crypto (BTC, ETH, USDT, USDC) en cualquier comercio Visa. "
            "Aplica comisión del 0.5% al pagar. Tope $40.000 ARS en BTC por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 2.0,
        "max_amount": 40000.0,
        "source": "Lemon",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 12, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://lemon.me/tarjeta",
        "logo_url": "https://logo.clearbit.com/lemon.me",
    },
    {
        "title": "1% cashback en BTC pagando con QR cripto — Lemon",
        "description": (
            "Pagá con QR desde la app Lemon usando crypto (BTC, ETH, USDT, USDC) "
            "en cualquier comercio con QR interoperable de Argentina "
            "y recibí 1% de cashback en Bitcoin automáticamente."
        ),
        "discount_type": "reintegro",
        "percentage": 1.0,
        "max_amount": None,
        "source": "Lemon",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 12, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://lemon.me/tarjeta",
        "logo_url": "https://logo.clearbit.com/lemon.me",
    },
    # ── UALÁ — datos reales verificados (mayo 2026) ─────────────────────────
    # Supermercados — cada cadena tiene su día y condiciones NFC vs tarjeta física
    {
        "title": "25% en Coto los lunes — Ualá",
        "description": (
            "25% de reintegro en Coto los lunes con tarjeta de crédito o prepaga Ualá. "
            "Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 15000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "25% en Carrefour Express los lunes con NFC — Ualá",
        "description": (
            "25% de reintegro en Carrefour Express los lunes pagando con celular vía NFC "
            "(Apple Pay / Google Pay) con Ualá. Tope $8.000 por semana. "
            "Con tarjeta física sin contacto: 15%, tope $3.000/sem."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 8000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "25% en Jumbo, Vea y Disco los martes con NFC — Ualá",
        "description": (
            "25% de reintegro en Jumbo, Vea y Disco los martes pagando con NFC "
            "(Apple Pay / Google Pay) con Ualá. Tope $8.000 por semana. "
            "Con tarjeta física: 15%, tope $6.000/sem."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 8000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "25% en Supermercado Día los viernes — Ualá",
        "description": (
            "25% de reintegro en Supermercado Día los viernes (presencial y online) "
            "con tarjeta de crédito Mastercard Ualá. "
            "Reintegro en 30 días corridos."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": None,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "25% en Chango Más los jueves — Ualá",
        "description": (
            "25% de reintegro en Chango Más los jueves "
            "con tarjeta de crédito Ualá (exclusivamente crédito). "
            "Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 15000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "15% en Carrefour online los jueves sin tope — Ualá",
        "description": (
            "15% de descuento en carrefour.com.ar todos los jueves con tarjeta Ualá. "
            "Sin tope de reintegro."
        ),
        "discount_type": "descuento",
        "percentage": 15.0,
        "max_amount": None,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "60% en Open 25h (vie–dom) con NFC — Ualá",
        "description": (
            "60% de reintegro en Open 25h los viernes, sábados y domingos "
            "pagando con NFC (Apple Pay / Google Pay) con Ualá. Tope $5.000 por día. "
            "Con tarjeta física: 40%, tope $4.000/día."
        ),
        "discount_type": "reintegro",
        "percentage": 60.0,
        "max_amount": 5000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "viernes,sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    # Gastronomía
    {
        "title": "30% en gastronomía los fines de semana con NFC — Ualá",
        "description": (
            "30% de reintegro los sábados y domingos en restaurantes, comida rápida, "
            "cervecerías y cafeterías de todo el país pagando con NFC con Ualá. "
            "Tope $30.000 por mes ($7.500 por semana)."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 30000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "30% en McDonald's todos los días con NFC — Ualá",
        "description": (
            "30% de reintegro en McDonald's todos los días "
            "pagando con NFC (Apple Pay / Google Pay) con Ualá. "
            "Tope $10.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 10000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    {
        "title": "35% en delivery los jueves — Ualá",
        "description": (
            "35% de reintegro los jueves en pedidos de delivery "
            "con tarjeta Ualá. Tope $4.000 por día."
        ),
        "discount_type": "reintegro",
        "percentage": 35.0,
        "max_amount": 4000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    # Farmacias
    {
        "title": "25% en Farmacity y Simplicity los sábados — Ualá",
        "description": (
            "25% de reintegro los sábados en Farmacity, Simplicity y Get the Look "
            "con tarjeta de crédito o prepaga Ualá. Tope $10.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 10000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "farmacias",
        "days_of_week": "sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    # Transporte
    {
        "title": "Hasta 100% de reintegro en subte y colectivo — Ualá",
        "description": (
            "Hasta 100% de reintegro en subte y colectivos habilitados todos los días "
            "pagando con NFC (Apple Pay o Google Pay) con tarjeta Ualá. "
            "Tope $20.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 100.0,
        "max_amount": 20000.0,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "transporte",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },
    # Entretenimiento
    {
        "title": "20% en Sportclub (planes mensual) — Ualá",
        "description": (
            "20% de descuento en los planes mensual Total y Plus de Sportclub "
            "con tarjeta prepaga o de crédito Ualá."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": None,
        "source": "Ualá",
        "source_type": "fintech",
        "category": "entretenimiento",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://logo.clearbit.com/uala.com.ar",
    },

    # ── BRUBANK — datos reales verificados (mayo 2026) ──────────────────────
    # Brubank usa el sistema "Girá la ruedita": después de cada compra participante
    # entrás a la app, tocás la compra y girás la rueda para activar el reintegro.
    {
        "title": "10% en YPF los lunes vía App YPF — Brubank Plan Plus",
        "description": (
            "10% de reintegro en YPF los lunes usando débito o crédito Visa Brubank "
            "en la App YPF. Tope $4.000 por compra. Máx. 1 compra/semana y 4/mes. "
            "Exclusivo Plan Plus. Activar girando la ruedita en la app Brubank."
        ),
        "discount_type": "reintegro",
        "percentage": 10.0,
        "max_amount": 4000.0,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "combustible",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "20% en Burger King lunes y viernes — Brubank",
        "description": (
            "20% de reintegro en Burger King los lunes y viernes con "
            "débito o crédito Brubank. Tope $2.000 por compra. "
            "Máx. 1 compra/semana y 4 en mayo. Activar girando la ruedita."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 2000.0,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "lunes,viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "30% en Farmacity, Simplicity y Get The Look (vie–dom) — Brubank",
        "description": (
            "30% de reintegro los viernes, sábados y domingos en Farmacity, Simplicity, "
            "Get The Look y The Food Market con débito o crédito Visa Brubank. "
            "Girá la ruedita en la app para activar."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 4000.0,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "farmacias",
        "days_of_week": "viernes,sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "30% en Coto los jueves — Brubank",
        "description": (
            "30% de descuento en Coto los jueves pagando con tarjeta Brubank. "
            "Girá la ruedita en la app para activar el reintegro."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "jueves",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "30% en Rapanui (vie–dom) — Brubank",
        "description": (
            "30% de reintegro los viernes, sábados y domingos en Rapanui "
            "con débito o crédito Visa Brubank. Girá la ruedita para activar."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "viernes,sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "50% en Cerini todos los días — Brubank",
        "description": (
            "50% de reintegro en Cerini (peluquería/estética) todos los días "
            "con débito Visa Brubank. Tope $6.000 por compra. Máx. 1 compra por mes. "
            "Girá la ruedita para activar."
        ),
        "discount_type": "reintegro",
        "percentage": 50.0,
        "max_amount": 6000.0,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "peluquerias",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": True,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "50% en Newman (cuota social) — Brubank",
        "description": (
            "50% de reintegro en el pago mensual de la cuota social de Newman "
            "con débito o crédito Brubank. Todos los días."
        ),
        "discount_type": "reintegro",
        "percentage": 50.0,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "entretenimiento",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "45% en Educación IT todos los días — Brubank",
        "description": (
            "45% de descuento en cursos de Educación IT con débito o crédito Visa Brubank. "
            "Todos los días. Código: BRUBEDUIT."
        ),
        "discount_type": "descuento",
        "percentage": 45.0,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "educacion",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "Hasta 6 cuotas sin interés en Decathlon — Brubank",
        "description": (
            "Hasta 6 cuotas sin interés en Decathlon todos los días "
            "con tarjeta de crédito Brubank."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "Hasta 6 cuotas en Dexter, Moov y Stock Center — Brubank",
        "description": (
            "Hasta 6 cuotas sin interés en Dexter, Moov y Stock Center "
            "con tarjeta de crédito Brubank. Todos los días."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "Hasta 12 cuotas en Samsung, JBL y electro — Brubank Plan Ultra",
        "description": (
            "Hasta 12 cuotas sin interés en Samsung, JBL, Diggit, Ferbi y más "
            "con tarjeta de crédito Brubank Plan Ultra. Todos los días."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },
    {
        "title": "Hasta 12 cuotas en Despegar y Aerolíneas — Brubank Plan Ultra",
        "description": (
            "Hasta 12 cuotas sin interés en Despegar y Aerolíneas Argentinas "
            "(vuelos nacionales) con tarjeta de crédito Brubank Plan Ultra. Todos los días."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Brubank",
        "source_type": "fintech",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://logo.clearbit.com/brubank.com",
    },

    # ── PERSONAL PAY — datos reales verificados (mayo 2026) ─────────────────
    # Personal Pay tiene sistema de NIVELES según consumo mensual:
    # Nivel 1 (todos): hasta $6.000/sem | Nivel 2 ($125k/mes): $8.000/sem
    # Nivel 3 ($350k/mes): $12.000/sem  | Nivel 4 ($400k/mes + Flow): $15.000/sem
    {
        "title": "Reintegro semanal en todos los comercios — Personal Pay Nivel 1",
        "description": (
            "Reintegro semanal de hasta $6.000 en compras con tarjeta Visa Personal Pay "
            "en supermercados, gastronomía y más. Nivel 1: disponible para todos los usuarios. "
            "Acreditado dentro de las 48 hs. hábiles posteriores a la compra."
        ),
        "discount_type": "reintegro",
        "percentage": None,
        "max_amount": 6000.0,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "Hasta $15.000 de reintegro semanal — Personal Pay Nivel 4 (Personal Flow)",
        "description": (
            "Clientes Personal Flow con consumo mensual ≥ $400.000: reintegro semanal "
            "de hasta $15.000 en todos los comercios con tarjeta Visa Personal Pay. "
            "Nivel 2 ($125k/mes): $8.000/sem | Nivel 3 ($350k/mes): $12.000/sem."
        ),
        "discount_type": "reintegro",
        "percentage": None,
        "max_amount": 15000.0,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "todos",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/reintegro-plus",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "15% sin tope en factura Personal Flow — Reintegro Plus",
        "description": (
            "Reintegro Plus: hasta 15% del valor de tu factura mensual de Personal + Flow "
            "sin tope, acreditado en tu cuenta Personal Pay. "
            "Más $7.000 adicionales pagando desde la app. "
            "Requiere factura unificada (móvil + hogar). Activar en personalpay.com.ar/reintegro-plus."
        ),
        "discount_type": "reintegro",
        "percentage": 15.0,
        "max_amount": None,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "servicios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/reintegro-plus",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "Hasta $55.000 de reintegro en Tienda Personal — Personal Pay",
        "description": (
            "Comprando en Tienda Personal con Personal Pay obtenés hasta $55.000 "
            "de reintegro adicional por mes. Combina con Reintegro Plus."
        ),
        "discount_type": "reintegro",
        "percentage": None,
        "max_amount": 55000.0,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/reintegro-plus",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "Hasta 25% en supermercados Día y Chango Más — Personal Pay",
        "description": (
            "Hasta 25% de reintegro en Supermercado Día y Chango Más "
            "pagando con tarjeta Visa Personal Pay. "
            "El reintegro semanal queda dentro del tope de tu nivel."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": None,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "Hasta 50% en gastronomía — Personal Pay",
        "description": (
            "Hasta 50% de reintegro en restaurantes y gastronomía adherida "
            "(McDonald's, Burger King, Empanadas Morita, Solo Empanadas y más) "
            "pagando con tarjeta Visa Personal Pay."
        ),
        "discount_type": "reintegro",
        "percentage": 50.0,
        "max_amount": None,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "2x1 en cines (Cinemark, Hoyts, Multiplex) — Personal Pay",
        "description": (
            "2x1 en entradas generales en Cinemark, Hoyts, Multiplex y más cines "
            "pagando con tarjeta Visa Personal Pay."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "entretenimiento",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "20% en primera recarga semanal de celular prepago — Personal Pay",
        "description": (
            "20% de reintegro en la primera recarga semanal de celular prepago Personal "
            "desde la app Personal Pay."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": None,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "servicios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "title": "Reintegro en recarga SUBE con NFC — Personal Pay",
        "description": (
            "Reintegro en recargas de SUBE y viajes en transporte público "
            "pagando con NFC (tarjeta Visa Personal Pay en Apple Pay / Google Pay). "
            "El monto del reintegro depende del nivel de consumo mensual."
        ),
        "discount_type": "reintegro",
        "percentage": None,
        "max_amount": 3000.0,
        "source": "Personal Pay",
        "source_type": "fintech",
        "category": "transporte",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },

    # ── SUPERVIELLE — datos reales verificados (mayo 2026) ──────────────────
    # Beneficios escalan según tipo de cuenta:
    # Cartera General < Plan Sueldo < Identité (porcentajes y topes distintos)
    {
        "title": "20% en Jumbo, Vea y Disco los martes — Supervielle",
        "description": (
            "20% de reintegro en Jumbo, Vea y Disco los martes con tarjeta de crédito "
            "Visa o Mastercard, o débito Visa vía MODO. "
            "Cartera General: tope $8.000/mes. "
            "Plan Sueldo/Identité: 25%, tope $15.000/mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 8000.0,
        "source": "Supervielle",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.supervielle.com.ar/personas/beneficios/descuentos",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Logo_Banco_Supervielle.svg",
    },
    {
        "title": "25% en Jumbo, Vea y Disco los martes — Supervielle Plan Sueldo/Identité",
        "description": (
            "25% de reintegro en Jumbo, Vea y Disco los martes para clientes "
            "Plan Sueldo o Identité con tarjeta Visa/Mastercard o débito vía MODO. "
            "Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 15000.0,
        "source": "Supervielle",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.supervielle.com.ar/personas/beneficios/descuentos",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Logo_Banco_Supervielle.svg",
    },
    {
        "title": "20% en gastronomía (vie y sáb) — Supervielle",
        "description": (
            "20% de reintegro en bares y restaurantes adheridos los viernes y sábados "
            "pagando con MODO con tarjetas Supervielle. "
            "Cartera General: tope $8.000/mes. "
            "Plan Sueldo: 25%, tope $20.000/mes. "
            "Identité: 30%, tope $50.000/mes."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 8000.0,
        "source": "Supervielle",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "viernes,sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.supervielle.com.ar/personas/beneficios/descuentos/restaurantes",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Logo_Banco_Supervielle.svg",
    },
    {
        "title": "30% en gastronomía (vie y sáb) — Supervielle Identité",
        "description": (
            "30% de reintegro en bares y restaurantes adheridos los viernes y sábados "
            "para clientes Identité con tarjetas Supervielle vía MODO. "
            "Tope $50.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 50000.0,
        "source": "Supervielle",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "viernes,sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.supervielle.com.ar/personas/beneficios/descuentos/restaurantes",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Logo_Banco_Supervielle.svg",
    },
    {
        "title": "10% en combustible los domingos — Supervielle",
        "description": (
            "10% de reintegro en combustible los domingos pagando con "
            "Visa Débito Supervielle vía MODO. Todas las marcas. Tope $10.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 10.0,
        "max_amount": 10000.0,
        "source": "Supervielle",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.supervielle.com.ar/personas/beneficios/descuentos/combustible",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Logo_Banco_Supervielle.svg",
    },
    {
        "title": "50% en farmacias adheridas — Supervielle",
        "description": (
            "50% de descuento en farmacias adheridas con tarjetas Supervielle. "
            "Consultá el buscador de beneficios en la app o web para ver los locales."
        ),
        "discount_type": "descuento",
        "percentage": 50.0,
        "max_amount": None,
        "source": "Supervielle",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.supervielle.com.ar/personas/beneficios/descuentos",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Logo_Banco_Supervielle.svg",
    },

    # ── BANCO CIUDAD (Buepp) — datos reales verificados (mayo 2026) ──────────
    # Buepp es la billetera digital del Banco Ciudad de Buenos Aires (CABA).
    # No requiere ser cliente del banco — cualquiera puede descargarse la app.
    # Beneficios principalmente disponibles en CABA.
    {
        "title": "30% en comercios y ferias de alimentos — Buepp / Banco Ciudad",
        "description": (
            "30% de descuento los lunes, martes, jueves y sábados en comercios adheridos "
            "y ferias de alimentos frescos de CABA pagando con QR de Buepp. "
            "Tope $20.000 por mes. Vigente hasta 30/06/2026."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 20000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes,martes,jueves,sabado",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "30% en supermercados los lunes — Buepp / Banco Ciudad",
        "description": (
            "Hasta 30% de descuento los lunes en Coto, Chango Más, Libertad, La Amistad, "
            "Cordiez y Mercamax en CABA pagando con QR de Buepp. "
            "Tope $13.000 por semana."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 13000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "lunes",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "30% en comercios vecinos seleccionados — Buepp / Banco Ciudad",
        "description": (
            "30% de descuento en Res, Cúspide, La Tablita, Punto Sano Dietética, "
            "El Topo, Mis Mascotas Petshop, verdulerías y granjas adheridas de CABA "
            "pagando con QR de Buepp. Tope $15.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 15000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "30% en gastronomía (jue–dom) — Buepp / Banco Ciudad",
        "description": (
            "30% de descuento en bares, cafés y gastronomía adherida en CABA "
            "los jueves, viernes, sábados y domingos pagando con QR de Buepp. "
            "Tope $10.000 por mes. Los sáb–dom de 7 a 12 hs hay promo especial $5.000/mes."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 10000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "gastronomia",
        "days_of_week": "jueves,viernes,sabado,domingo",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "30% en Farmacity los miércoles — Buepp / Banco Ciudad",
        "description": (
            "30% de descuento en Farmacity los miércoles pagando con QR de Buepp. "
            "Tope $5.000 por día."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 5000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "farmacias",
        "days_of_week": "miercoles",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "10% en combustible los domingos — Buepp / Banco Ciudad",
        "description": (
            "10% de descuento en combustible los domingos en Shell, Axion y YPF "
            "pagando con QR de Buepp. Tope $10.000 por mes."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": 10000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "combustible",
        "days_of_week": "domingo",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "100% de reintegro en subte y colectivo — Buepp / Banco Ciudad",
        "description": (
            "100% de reintegro en subtes y colectivos de CABA pagando con la "
            "tarjeta Mastercard digital de Buepp (Banco Ciudad). "
            "Tope $15.000 por mes."
        ),
        "discount_type": "reintegro",
        "percentage": 100.0,
        "max_amount": 15000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "transporte",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },
    {
        "title": "20% de descuento en ABL — Buepp / Banco Ciudad",
        "description": (
            "20% de descuento en el pago del ABL (Alumbrado, Barrido y Limpieza) "
            "de CABA pagando con QR o NFC de Buepp. "
            "Tope $10.000 por mes. Todos los días."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 10000.0,
        "source": "Banco Ciudad",
        "source_type": "banco",
        "category": "servicios",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 6, 30),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.buepp.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/7f/17/b7/7f17b77306a1b93f8101467298908188.jpg",
    },

    # ── NARANJA X — datos reales verificados (mayo 2026) ────────────────────
    {
        "title": "25% en supermercados los martes — Naranja X Plan Turbo",
        "description": (
            "25% de reintegro en Chango Más, Disco, Vea, Jumbo, Carrefour, Día y Coto "
            "los martes con tarjeta de crédito Naranja X (Plan Turbo). Tope $12.000/mes. "
            "Sin Plan Turbo: 10%, tope $3.000."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 12000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/plan-turbo",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "4 cuotas sin interés en Carrefour y Diarco — Naranja X",
        "description": (
            "4 cuotas sin interés todos los días en Carrefour y Diarco "
            "pagando con tarjeta Naranja X crédito."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "supermercados",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promociones",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "20% en indumentaria deportiva (lun y mar) — Naranja X",
        "description": (
            "20% de descuento los lunes y martes en Dexter, Moov, Stock Center y Adidas "
            "con tarjeta Naranja X. Tope $30.000/mes ($40.000 en Adidas)."
        ),
        "discount_type": "descuento",
        "percentage": 20.0,
        "max_amount": 30000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "indumentaria",
        "days_of_week": "lunes,martes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promociones",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "25% en McDonald's los viernes — Naranja X Plan Turbo",
        "description": (
            "25% de reintegro en McDonald's todos los viernes "
            "con tarjeta de crédito Naranja X (Plan Turbo). Tope $12.000/mes."
        ),
        "discount_type": "reintegro",
        "percentage": 25.0,
        "max_amount": 12000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "viernes",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/plan-turbo",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "30% en KFC, Wendy's y heladerías (vie y sáb) — Naranja X",
        "description": (
            "30% de reintegro los viernes y sábados en KFC, Wendy's, Ave Cesar, "
            "Sushi Pop, heladerías adheridas con tarjeta Naranja X. Tope $15.000/mes."
        ),
        "discount_type": "reintegro",
        "percentage": 30.0,
        "max_amount": 15000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "viernes,sabado",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promociones",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "10% en GULF los fines de semana — Naranja X",
        "description": (
            "10% de descuento en estaciones GULF los sábados y domingos "
            "con tarjeta Naranja X. Tope $3.000."
        ),
        "discount_type": "descuento",
        "percentage": 10.0,
        "max_amount": 3000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "combustible",
        "days_of_week": "sabado,domingo",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promociones",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "100% de reintegro en subte y colectivo — Naranja X",
        "description": (
            "100% de reintegro en subtes y colectivos todos los días "
            "pagando con NFC o débito Naranja X. "
            "Tope $10.000 con débito/NFC, $5.000 con saldo en cuenta. Hasta 31/05/2026."
        ),
        "discount_type": "reintegro",
        "percentage": 100.0,
        "max_amount": 10000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "transporte",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promociones",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "6 cuotas sin interés en Aerolíneas Argentinas — Naranja X",
        "description": (
            "6 cuotas sin interés en compras de vuelos Aerolíneas Argentinas "
            "todos los días con tarjeta de crédito Naranja X."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "viajes",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promociones",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    {
        "title": "Promos Relámpago: descuentos sorpresa el último sábado — Naranja X",
        "description": (
            "Cada último sábado del mes, Naranja X lanza promos relámpago con hasta 40% OFF "
            "en rubros sorpresa: combustible, farmacias, indumentaria, jugueterías y más."
        ),
        "discount_type": "descuento",
        "percentage": 40.0,
        "max_amount": 9000.0,
        "source": "Naranja X",
        "source_type": "fintech",
        "category": "varios",
        "days_of_week": "sabado",
        "valid_until": datetime(2026, 5, 30),
        "is_limited_stock": True,
        "is_new": True,
        "is_active": True,
        "url": "https://www.naranjax.com/promos-relampago",
        "logo_url": "https://logo.clearbit.com/naranjax.com",
    },
    # ── MODO — datos reales verificados (mayo 2026) ─────────────────────────
    # MODO es una plataforma de pago cross-bank. Sus promos aplican a tarjetas
    # de cualquier banco adherido (Galicia, Nación, Santander, BBVA, Macro, etc.)
    {
        "title": "20% de reintegro en shoppings — MODO Shopping Fest 2026",
        "description": (
            "Shopping Fest (8–10/05): 20% de reintegro pagando con MODO "
            "en más de 65 shoppings de todo el país: Alto Palermo, Abasto, "
            "Galerías Pacífico, Patio Bullrich, Unicenter y más. "
            "Tope $50.000 por banco. Aplica con tarjeta de cualquier banco adherido a MODO."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": 50000.0,
        "source": "MODO",
        "source_type": "fintech",
        "category": "indumentaria",
        "days_of_week": "sabado,domingo",
        "valid_until": datetime(2026, 5, 10),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://shoppingfest.com.ar/",
        "logo_url": "https://logo.clearbit.com/modo.com.ar",
    },
    {
        "title": "20% de reintegro + 18 cuotas en electro e indumentaria — MODO Hot Sale",
        "description": (
            "Hot Sale (11–17/05): 20% de reintegro y hasta 18 cuotas sin interés "
            "en electrónica, hogar, indumentaria, perfumería y farmacias "
            "en comercios online adheridos, pagando con MODO desde la app de tu banco."
        ),
        "discount_type": "reintegro",
        "percentage": 20.0,
        "max_amount": None,
        "source": "MODO",
        "source_type": "fintech",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 17),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.modo.com.ar/promos",
        "logo_url": "https://logo.clearbit.com/modo.com.ar",
    },
    {
        "title": "30% en gastronomía todos los días — MODO",
        "description": (
            "30% de descuento en restaurantes, bares, cafeterías y heladerías "
            "adheridos pagando con QR de MODO con tarjetas de cualquier banco. "
            "Tope $10.000 por semana."
        ),
        "discount_type": "descuento",
        "percentage": 30.0,
        "max_amount": 10000.0,
        "source": "MODO",
        "source_type": "fintech",
        "category": "gastronomia",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.modo.com.ar/promos",
        "logo_url": "https://logo.clearbit.com/modo.com.ar",
    },
    {
        "title": "Hasta 20 cuotas sin interés en electrónica — MODO",
        "description": (
            "Hasta 20 cuotas sin interés en Frávega, Samsung, On City, LG, "
            "Tienda Newsan, Megatone, Naldo y Motorola pagando con MODO "
            "con tarjetas de crédito de bancos adheridos."
        ),
        "discount_type": "promocion",
        "percentage": None,
        "max_amount": None,
        "source": "MODO",
        "source_type": "fintech",
        "category": "electronica",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.modo.com.ar/promos",
        "logo_url": "https://logo.clearbit.com/modo.com.ar",
    },
    {
        "title": "50% de reintegro en indumentaria — MODO + Banco Provincia",
        "description": (
            "50% de reintegro en indumentaria y calzado con tarjetas del Banco Provincia "
            "pagando con MODO. Hasta 6 cuotas sin interés. Tope $50.000."
        ),
        "discount_type": "reintegro",
        "percentage": 50.0,
        "max_amount": 50000.0,
        "source": "MODO",
        "source_type": "fintech",
        "category": "indumentaria",
        "days_of_week": "todos",
        "valid_until": datetime(2026, 5, 31),
        "is_limited_stock": False,
        "is_new": True,
        "is_active": True,
        "url": "https://www.modo.com.ar/promos",
        "logo_url": "https://logo.clearbit.com/modo.com.ar",
    },
]
