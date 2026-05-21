// Tasas orientativas — actualizar periódicamente según BCRA y sitios oficiales
export const ULTIMA_ACTUALIZACION = 'mayo 2026'

export const TASAS_PLAZO_FIJO = [
  // fintechs
  { nombre: 'Mercado Pago',    tna: 37.0, tipo: 'fintech', url: 'https://www.mercadopago.com.ar' },
  { nombre: 'Ualá',           tna: 36.0, tipo: 'fintech', url: 'https://www.uala.com.ar' },
  { nombre: 'Brubank',         tna: 35.5, tipo: 'fintech', url: 'https://www.brubank.com.ar' },
  { nombre: 'Naranja X',       tna: 35.0, tipo: 'fintech', url: 'https://www.naranjax.com' },
  { nombre: 'Personal Pay',    tna: 34.0, tipo: 'fintech', url: 'https://www.personal-pay.com.ar' },
  // bancos
  { nombre: 'Banco Galicia',   tna: 32.0, tipo: 'banco',   url: 'https://www.bancogalicia.com.ar' },
  { nombre: 'Santander',       tna: 31.0, tipo: 'banco',   url: 'https://www.santander.com.ar' },
  { nombre: 'BBVA',            tna: 30.5, tipo: 'banco',   url: 'https://www.bbva.com.ar' },
  { nombre: 'Banco Provincia', tna: 30.0, tipo: 'banco',   url: 'https://www.bapro.com.ar' },
  { nombre: 'ICBC',            tna: 30.0, tipo: 'banco',   url: 'https://www.icbc.com.ar' },
  { nombre: 'Macro',           tna: 29.5, tipo: 'banco',   url: 'https://www.macro.com.ar' },
  { nombre: 'Banco Nación',    tna: 29.0, tipo: 'banco',   url: 'https://www.bna.com.ar' },
  { nombre: 'HSBC',            tna: 29.0, tipo: 'banco',   url: 'https://www.hsbc.com.ar' },
  { nombre: 'Supervielle',     tna: 30.0, tipo: 'banco',   url: 'https://www.supervielle.com.ar' },
].sort((a, b) => b.tna - a.tna)

export const TASAS_REMUNERATIVAS = [
  // fintechs
  { nombre: 'Mercado Pago',    apr: 37.0, tipo: 'fintech', url: 'https://www.mercadopago.com.ar' },
  { nombre: 'Ualá',           apr: 36.0, tipo: 'fintech', url: 'https://www.uala.com.ar' },
  { nombre: 'Lemon Cash',      apr: 35.0, tipo: 'fintech', url: 'https://www.lemon.me' },
  { nombre: 'Brubank',         apr: 34.5, tipo: 'fintech', url: 'https://www.brubank.com.ar' },
  { nombre: 'Naranja X',       apr: 34.0, tipo: 'fintech', url: 'https://www.naranjax.com' },
  { nombre: 'Personal Pay',    apr: 33.0, tipo: 'fintech', url: 'https://www.personal-pay.com.ar' },
  { nombre: 'Modo',            apr: 31.0, tipo: 'fintech', url: 'https://www.modo.com.ar' },
  // bancos
  { nombre: 'Banco Galicia',   apr: 28.0, tipo: 'banco',   url: 'https://www.bancogalicia.com.ar' },
  { nombre: 'Santander',       apr: 27.0, tipo: 'banco',   url: 'https://www.santander.com.ar' },
  { nombre: 'BBVA',            apr: 26.5, tipo: 'banco',   url: 'https://www.bbva.com.ar' },
  { nombre: 'Macro',           apr: 26.0, tipo: 'banco',   url: 'https://www.macro.com.ar' },
  { nombre: 'Banco Nación',    apr: 25.0, tipo: 'banco',   url: 'https://www.bna.com.ar' },
].sort((a, b) => b.apr - a.apr)
