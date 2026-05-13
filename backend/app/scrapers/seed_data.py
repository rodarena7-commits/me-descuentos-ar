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
