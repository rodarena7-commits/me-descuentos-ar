"""
Configuración de cada entidad financiera para el scraper automático.
'source' debe coincidir EXACTAMENTE con el campo source en la DB.
"""

ENTITIES = [
    # ── BANCOS ───────────────────────────────────────────────────────────────
    {
        "source": "Banco Galicia",
        "source_type": "banco",
        "url": "https://www.galicia.ar/personas/promociones",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://galicia.ar&size=128",
    },
    {
        "source": "Santander",
        "source_type": "banco",
        "url": "https://www.santander.com.ar/banco/online/beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://santander.com.ar&size=128",
    },
    {
        "source": "BBVA",
        "source_type": "banco",
        "url": "https://www.bbva.com.ar/personas/beneficios.html",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://bbva.com.ar&size=128",
    },
    {
        "source": "Banco Nación",
        "source_type": "banco",
        "url": "https://www.bna.com.ar/Personas/Beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://bna.com.ar&size=128",
    },
    {
        "source": "Banco Macro",
        "source_type": "banco",
        "url": "https://www.macro.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg",
    },
    {
        "source": "Banco Patagonia",
        "source_type": "banco",
        "url": "https://www.bancopatagonia.com.ar/patagoniaon/beneficios.php",
        "logo_url": "https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg",
    },
    {
        "source": "Cuenta DNI",
        "source_type": "banco",
        "url": "https://www.cuentadni.ar/beneficios",
        "logo_url": "https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg",
    },
    {
        "source": "HSBC",
        "source_type": "banco",
        "url": "https://www.hsbc.com.ar/tarjetas/beneficios/",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://hsbc.com.ar&size=128",
    },
    {
        "source": "ICBC",
        "source_type": "banco",
        "url": "https://www.beneficios.icbc.com.ar/",
        "logo_url": "https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg",
    },
    {
        "source": "Brubank",
        "source_type": "fintech",
        "url": "https://www.brubank.com/beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://brubank.com&size=128",
    },
    {
        "source": "Banco Ciudad",
        "source_type": "banco",
        "url": "https://www.bancociudad.com.ar/personas/beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://bancociudad.com.ar&size=128",
    },
    {
        "source": "Supervielle",
        "source_type": "banco",
        "url": "https://www.supervielle.com.ar/beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://supervielle.com.ar&size=128",
    },
    {
        "source": "Banco Comafi",
        "source_type": "banco",
        "url": "https://www.comafi.com.ar/2543-Beneficios.note.aspx",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://comafi.com.ar&size=128",
    },
    {
        "source": "Credicoop",
        "source_type": "banco",
        "url": "https://www.bancocredicoop.coop/Personas/Beneficios",
        "logo_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Logo_Banco_Credicoop.svg/500px-Logo_Banco_Credicoop.svg.png",
    },
    # ── FINTECHS ─────────────────────────────────────────────────────────────
    {
        "source": "MercadoPago",
        "source_type": "fintech",
        "url": "https://www.mercadopago.com.ar/beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://mercadopago.com&size=128",
    },
    {
        "source": "Naranja X",
        "source_type": "fintech",
        "url": "https://www.naranjax.com/beneficios",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://naranjax.com&size=128",
    },
    {
        "source": "MODO",
        "source_type": "fintech",
        "url": "https://www.modo.com.ar/promos",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://modo.com.ar&size=128",
    },
    {
        "source": "Ualá",
        "source_type": "fintech",
        "url": "https://www.uala.com.ar/promociones",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://uala.com.ar&size=128",
    },
    {
        "source": "Personal Pay",
        "source_type": "fintech",
        "url": "https://www.personalpay.com.ar/beneficios",
        "logo_url": "https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg",
    },
    {
        "source": "Lemon",
        "source_type": "fintech",
        "url": "https://lemon.me/tarjeta",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://lemon.me&size=128",
    },
    # ── EXCHANGES / CRYPTO ───────────────────────────────────────────────────
    {
        "source": "Binance",
        "source_type": "fintech",
        "url": "https://www.binance.com/es/earn",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://binance.com&size=128",
    },
    {
        "source": "Ripio",
        "source_type": "fintech",
        "url": "https://ripio.com/ar/beneficios/",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://ripio.com&size=128",
    },
    {
        "source": "AstroPay",
        "source_type": "fintech",
        "url": "https://astropay.com/es/",
        "logo_url": "https://i.pinimg.com/736x/a5/a6/00/a5a600775bff34cd9842e3555110c144.jpg",
    },
    {
        "source": "Let'sBit",
        "source_type": "fintech",
        "url": "https://letsbit.io/es",
        "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://letsbit.io&size=128",
    },
]
