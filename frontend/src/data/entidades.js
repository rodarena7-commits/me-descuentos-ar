const gFav = d =>
  `https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://${d}&size=128`

export const ENTIDADES = [
  // ── Bancos ───────────────────────────────────────────────────────────────
  { id: 'galicia',     name: 'Banco Galicia',   tipo: 'Banco',    source: 'Banco Galicia',   logo: gFav('galicia.ar') },
  { id: 'santander',   name: 'Santander',        tipo: 'Banco',    source: 'Santander',       logo: gFav('santander.com.ar') },
  { id: 'bbva',        name: 'BBVA',             tipo: 'Banco',    source: 'BBVA',            logo: gFav('bbva.com.ar') },
  { id: 'bna',         name: 'Banco Nación',     tipo: 'Banco',    source: 'Banco Nación',    logo: gFav('bna.com.ar') },
  { id: 'macro',       name: 'Banco Macro',      tipo: 'Banco',    source: 'Banco Macro',     logo: 'https://i.pinimg.com/736x/cf/bd/f0/cfbdf0a13b75a09b4a0e21805b087124.jpg' },
  { id: 'patagonia',   name: 'Banco Patagonia',  tipo: 'Banco',    source: 'Banco Patagonia', logo: 'https://i.pinimg.com/236x/93/77/73/937773ce8b832fb110e5da731996b8d1.jpg' },
  { id: 'cuenta-dni',  name: 'Cuenta DNI',       tipo: 'Banco',    source: 'Cuenta DNI',      logo: 'https://i.pinimg.com/736x/50/d9/f5/50d9f5295dfa90d8cdb3aaa44287e0d9.jpg' },
  { id: 'icbc',        name: 'ICBC',             tipo: 'Banco',    source: 'ICBC',            logo: 'https://i.pinimg.com/736x/d3/2d/01/d32d018136507dc5697d02974c927300.jpg' },
  { id: 'ciudad',      name: 'Banco Ciudad',     tipo: 'Banco',    source: 'Banco Ciudad',    logo: gFav('bancociudad.com.ar') },
  { id: 'supervielle', name: 'Supervielle',      tipo: 'Banco',    source: 'Supervielle',     logo: gFav('supervielle.com.ar') },
  { id: 'hsbc',        name: 'HSBC',             tipo: 'Banco',    source: 'HSBC',            logo: gFav('hsbc.com.ar') },
  { id: 'credicoop',  name: 'Credicoop',        tipo: 'Banco',    source: 'Credicoop',       logo: 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Logo_Banco_Credicoop.svg/500px-Logo_Banco_Credicoop.svg.png' },
  { id: 'comafi',     name: 'Banco Comafi',     tipo: 'Banco',    source: 'Banco Comafi',    logo: gFav('comafi.com.ar') },

  // ── Fintechs ─────────────────────────────────────────────────────────────
  { id: 'mercadopago', name: 'MercadoPago',      tipo: 'Fintech',  source: 'MercadoPago',     logo: gFav('mercadopago.com') },
  { id: 'naranjax',    name: 'Naranja X',        tipo: 'Fintech',  source: 'Naranja X',       logo: gFav('naranjax.com') },
  { id: 'modo',        name: 'MODO',             tipo: 'Fintech',  source: 'MODO',            logo: gFav('modo.com.ar') },
  { id: 'uala',        name: 'Ualá',             tipo: 'Fintech',  source: 'Ualá',            logo: gFav('uala.com.ar') },
  { id: 'brubank',     name: 'Brubank',          tipo: 'Fintech',  source: 'Brubank',         logo: gFav('brubank.com') },
  { id: 'personalpay', name: 'Personal Pay',     tipo: 'Fintech',  source: 'Personal Pay',    logo: 'https://i.pinimg.com/1200x/e1/b2/3a/e1b23a9f6ea1a8a548e3937d6cd4e795.jpg' },
  { id: 'lemon',       name: 'Lemon',            tipo: 'Fintech',  source: 'Lemon',           logo: gFav('lemon.me') },
  { id: 'buepp',       name: 'Buepp',            tipo: 'Fintech',  source: 'Buepp',           logo: gFav('buepp.com.ar') },

  // ── Exchanges / Crypto ───────────────────────────────────────────────────
  { id: 'binance',     name: 'Binance',          tipo: 'Exchange', source: 'Binance',         logo: gFav('binance.com') },
  { id: 'ripio',       name: 'Ripio',            tipo: 'Exchange', source: 'Ripio',           logo: gFav('ripio.com') },
  { id: 'astropay',    name: 'AstroPay',         tipo: 'Exchange', source: 'AstroPay',        logo: 'https://i.pinimg.com/736x/a5/a6/00/a5a600775bff34cd9842e3555110c144.jpg' },
  { id: 'letsbit',     name: "Let'sBit",         tipo: 'Exchange', source: "Let'sBit",        logo: gFav('letsbit.io') },
]

export const TIPOS_ENTIDAD = ['Banco', 'Fintech', 'Exchange']

export function getEntidad(slug) {
  return ENTIDADES.find(e => e.id === slug) ?? null
}
