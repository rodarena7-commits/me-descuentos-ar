// Catálogo de marcas adheridas a descuentos en Argentina.
// keywords: array de strings que se buscan en title + description de cada descuento.
// Todas en minúsculas para matching case-insensitive.

export const MARCAS = [
  // ── Supermercados ────────────────────────────────────────────────────────
  { id: 'carrefour',  name: 'Carrefour',      categoria: 'Supermercados', keywords: ['carrefour'],              logo: 'https://logo.clearbit.com/carrefour.com.ar' },
  { id: 'coto',       name: 'Coto',           categoria: 'Supermercados', keywords: ['coto'],                   logo: 'https://logo.clearbit.com/coto.com.ar' },
  { id: 'jumbo',      name: 'Jumbo',          categoria: 'Supermercados', keywords: ['jumbo'],                  logo: 'https://logo.clearbit.com/jumbo.com.ar' },
  { id: 'disco',      name: 'Disco / Vea',    categoria: 'Supermercados', keywords: ['disco', 'vea'],           logo: 'https://logo.clearbit.com/disco.com.ar' },
  { id: 'dia',        name: 'Supermercado Día', categoria: 'Supermercados', keywords: ['supermercado día', 'supermercado dia', 'en día', 'en dia'], logo: 'https://logo.clearbit.com/dia.com.ar' },
  { id: 'changomas',  name: 'Chango Más',     categoria: 'Supermercados', keywords: ['chango más', 'chango mas', 'changomás'], logo: 'https://logo.clearbit.com/changomas.com.ar' },
  { id: 'open25h',    name: 'Open 25h',       categoria: 'Supermercados', keywords: ['open 25h'],               logo: 'https://logo.clearbit.com/open25h.com.ar' },
  { id: 'lanónima',   name: 'La Anónima',     categoria: 'Supermercados', keywords: ['anónima', 'anonima'],     logo: 'https://logo.clearbit.com/laanonimaonline.com' },
  { id: 'diarco',     name: 'Diarco',         categoria: 'Supermercados', keywords: ['diarco'],                 logo: 'https://logo.clearbit.com/diarco.com.ar' },

  // ── Combustible ──────────────────────────────────────────────────────────
  { id: 'ypf',        name: 'YPF',            categoria: 'Combustible',   keywords: ['ypf'],                    logo: 'https://logo.clearbit.com/ypf.com' },
  { id: 'shell',      name: 'Shell',          categoria: 'Combustible',   keywords: ['shell'],                  logo: 'https://logo.clearbit.com/shell.com' },
  { id: 'axion',      name: 'Axion Energy',   categoria: 'Combustible',   keywords: ['axion'],                  logo: 'https://logo.clearbit.com/axionenergy.com.ar' },
  { id: 'gulf',       name: 'GULF',           categoria: 'Combustible',   keywords: ['gulf'],                   logo: 'https://logo.clearbit.com/gulf.com' },
  { id: 'puma',       name: 'Puma Energy',    categoria: 'Combustible',   keywords: ['puma energy'],            logo: 'https://logo.clearbit.com/pumaenergy.com' },

  // ── Farmacias / Salud ────────────────────────────────────────────────────
  { id: 'farmacity',  name: 'Farmacity',      categoria: 'Farmacias',     keywords: ['farmacity'],              logo: 'https://logo.clearbit.com/farmacity.com' },
  { id: 'simplicity', name: 'Simplicity',     categoria: 'Farmacias',     keywords: ['simplicity'],             logo: 'https://logo.clearbit.com/simplicity.com.ar' },
  { id: 'farmaonline',name: 'Farmaonline',    categoria: 'Farmacias',     keywords: ['farmaonline'],            logo: 'https://logo.clearbit.com/farmaonline.com' },
  { id: 'gethelook',  name: 'Get The Look',   categoria: 'Farmacias',     keywords: ['get the look'],           logo: 'https://logo.clearbit.com/getthelook.com.ar' },
  { id: 'drahorro',   name: 'Dr Ahorro',      categoria: 'Farmacias',     keywords: ['dr ahorro'],              logo: 'https://logo.clearbit.com/drdrives.com.ar' },

  // ── Gastronomía ──────────────────────────────────────────────────────────
  { id: 'mcdonalds',  name: "McDonald's",     categoria: 'Gastronomía',   keywords: ["mcdonald"],               logo: 'https://logo.clearbit.com/mcdonalds.com' },
  { id: 'burgerking', name: 'Burger King',    categoria: 'Gastronomía',   keywords: ['burger king'],            logo: 'https://logo.clearbit.com/burgerking.com' },
  { id: 'mostaza',    name: 'Mostaza',        categoria: 'Gastronomía',   keywords: ['mostaza'],                logo: 'https://logo.clearbit.com/mostaza.com.ar' },
  { id: 'kfc',        name: 'KFC',            categoria: 'Gastronomía',   keywords: ['kfc'],                    logo: 'https://logo.clearbit.com/kfc.com' },
  { id: 'wendys',     name: "Wendy's",        categoria: 'Gastronomía',   keywords: ["wendy"],                  logo: 'https://logo.clearbit.com/wendys.com' },
  { id: 'rapanui',    name: 'Rapanui',        categoria: 'Gastronomía',   keywords: ['rapanui'],                logo: 'https://logo.clearbit.com/rapanuihelados.com' },
  { id: 'havanna',    name: 'Havanna',        categoria: 'Gastronomía',   keywords: ['havanna'],                logo: 'https://logo.clearbit.com/havanna.com' },
  { id: 'luccianos',  name: "Lucciano's",     categoria: 'Gastronomía',   keywords: ["lucciano"],               logo: 'https://logo.clearbit.com/luccianos.com.ar' },
  { id: 'pedidosya',  name: 'PedidosYa',      categoria: 'Gastronomía',   keywords: ['pedidos ya'],             logo: 'https://logo.clearbit.com/pedidosya.com' },

  // ── Indumentaria / Deportes ──────────────────────────────────────────────
  { id: 'adidas',     name: 'Adidas',         categoria: 'Indumentaria',  keywords: ['adidas'],                 logo: 'https://logo.clearbit.com/adidas.com' },
  { id: 'nike',       name: 'Nike',           categoria: 'Indumentaria',  keywords: ['nike'],                   logo: 'https://logo.clearbit.com/nike.com' },
  { id: 'dexter',     name: 'Dexter',         categoria: 'Indumentaria',  keywords: ['dexter'],                 logo: 'https://logo.clearbit.com/dexter.com.ar' },
  { id: 'moov',       name: 'Moov',           categoria: 'Indumentaria',  keywords: ['moov'],                   logo: 'https://logo.clearbit.com/moov.com.ar' },
  { id: 'stockcenter',name: 'Stock Center',   categoria: 'Indumentaria',  keywords: ['stock center'],           logo: 'https://logo.clearbit.com/stockcenter.com.ar' },
  { id: 'decathlon',  name: 'Decathlon',      categoria: 'Indumentaria',  keywords: ['decathlon'],              logo: 'https://logo.clearbit.com/decathlon.com.ar' },
  { id: 'carocuore',  name: 'Caro Cuore',     categoria: 'Indumentaria',  keywords: ['caro cuore'],             logo: 'https://logo.clearbit.com/carocuore.com.ar' },

  // ── Electrónica / Tecnología ─────────────────────────────────────────────
  { id: 'samsung',    name: 'Samsung',        categoria: 'Electrónica',   keywords: ['samsung'],                logo: 'https://logo.clearbit.com/samsung.com' },
  { id: 'lg',         name: 'LG',             categoria: 'Electrónica',   keywords: [' lg ', 'lg,'],            logo: 'https://logo.clearbit.com/lg.com' },
  { id: 'fravega',    name: 'Frávega',        categoria: 'Electrónica',   keywords: ['frávega', 'fravega'],     logo: 'https://logo.clearbit.com/fravega.com' },
  { id: 'megatone',   name: 'Megatone',       categoria: 'Electrónica',   keywords: ['megatone'],               logo: 'https://logo.clearbit.com/megatone.net' },
  { id: 'cetrogar',   name: 'Cetrogar',       categoria: 'Electrónica',   keywords: ['cetrogar'],               logo: 'https://logo.clearbit.com/cetrogar.com.ar' },
  { id: 'motorola',   name: 'Motorola',       categoria: 'Electrónica',   keywords: ['motorola'],               logo: 'https://logo.clearbit.com/motorola.com' },

  // ── Viajes / Transporte ──────────────────────────────────────────────────
  { id: 'despegar',   name: 'Despegar',       categoria: 'Viajes',        keywords: ['despegar'],               logo: 'https://logo.clearbit.com/despegar.com' },
  { id: 'aerolineas', name: 'Aerolíneas Argentinas', categoria: 'Viajes', keywords: ['aerolíneas', 'aerolineas'], logo: 'https://logo.clearbit.com/aerolineas.com.ar' },
  { id: 'cabify',     name: 'Cabify',         categoria: 'Viajes',        keywords: ['cabify'],                 logo: 'https://logo.clearbit.com/cabify.com' },
  { id: 'flechabus',  name: 'Flechabus',      categoria: 'Viajes',        keywords: ['flechabus'],              logo: 'https://logo.clearbit.com/flechabus.com.ar' },
  { id: 'almundo',    name: 'Almundo',        categoria: 'Viajes',        keywords: ['almundo'],                logo: 'https://logo.clearbit.com/almundo.com' },

  // ── Entretenimiento ──────────────────────────────────────────────────────
  { id: 'cinemark',   name: 'Cinemark / Hoyts', categoria: 'Entretenimiento', keywords: ['cinemark', 'hoyts'],  logo: 'https://logo.clearbit.com/cinemark.com.ar' },
  { id: 'sportclub',  name: 'Sportclub',      categoria: 'Entretenimiento', keywords: ['sportclub'],            logo: 'https://logo.clearbit.com/sportclub.com.ar' },
  { id: 'newman',     name: 'Newman',         categoria: 'Entretenimiento', keywords: ['newman'],               logo: 'https://logo.clearbit.com/newman.com.ar' },

  // ── Librerías ────────────────────────────────────────────────────────────
  { id: 'yenny',      name: 'Yenny / El Ateneo', categoria: 'Librerías',  keywords: ['yenny', 'ateneo'],        logo: 'https://logo.clearbit.com/elateneo.com' },
  { id: 'cuspide',    name: 'Cúspide',        categoria: 'Librerías',     keywords: ['cúspide', 'cuspide'],     logo: 'https://logo.clearbit.com/cuspide.com' },

  // ── Hogar / Construcción ─────────────────────────────────────────────────
  { id: 'easy',       name: 'Easy',           categoria: 'Hogar',         keywords: ['easy'],                   logo: 'https://logo.clearbit.com/easy.com.ar' },
  { id: 'natura',     name: 'Natura',         categoria: 'Hogar',         keywords: ['natura'],                 logo: 'https://logo.clearbit.com/natura.com.ar' },
]

export const CATEGORIAS_MARCA = [
  'Supermercados', 'Combustible', 'Farmacias', 'Gastronomía',
  'Indumentaria', 'Electrónica', 'Viajes', 'Entretenimiento',
  'Librerías', 'Hogar',
]

export function getMarca(slug) {
  return MARCAS.find(m => m.id === slug) ?? null
}
