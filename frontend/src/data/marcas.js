// Catálogo de marcas adheridas a descuentos en Argentina.
// keywords: array de strings que se buscan en title + description de cada descuento.
// Todas en minúsculas para matching case-insensitive.

export const MARCAS = [
  // ── Supermercados ────────────────────────────────────────────────────────
  { id: 'carrefour',  name: 'Carrefour',      categoria: 'Supermercados', keywords: ['carrefour'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://carrefour.com.ar&size=128' },
  { id: 'coto',       name: 'Coto',           categoria: 'Supermercados', keywords: ['coto'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://coto.com.ar&size=128' },
  { id: 'jumbo',      name: 'Jumbo',          categoria: 'Supermercados', keywords: ['jumbo'],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://jumbo.com.ar&size=128' },
  { id: 'disco',      name: 'Disco / Vea',    categoria: 'Supermercados', keywords: ['disco', 'vea'],           logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://disco.com.ar&size=128' },
  { id: 'dia',        name: 'Supermercado Día', categoria: 'Supermercados', keywords: ['supermercado día', 'supermercado dia', 'en día', 'en dia'], logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://dia.com.ar&size=128' },
  { id: 'changomas',  name: 'Chango Más',     categoria: 'Supermercados', keywords: ['chango más', 'chango mas', 'changomás'], logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://changomas.com.ar&size=128' },
  { id: 'open25h',    name: 'Open 25h',       categoria: 'Supermercados', keywords: ['open 25h'],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://open25h.com.ar&size=128' },
  { id: 'lanónima',   name: 'La Anónima',     categoria: 'Supermercados', keywords: ['anónima', 'anonima'],     logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://laanonimaonline.com&size=128' },
  { id: 'diarco',     name: 'Diarco',         categoria: 'Supermercados', keywords: ['diarco'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://diarco.com.ar&size=128' },

  // ── Combustible ──────────────────────────────────────────────────────────
  { id: 'ypf',        name: 'YPF',            categoria: 'Combustible',   keywords: ['ypf'],                    logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://ypf.com&size=128' },
  { id: 'shell',      name: 'Shell',          categoria: 'Combustible',   keywords: ['shell'],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://shell.com&size=128' },
  { id: 'axion',      name: 'Axion Energy',   categoria: 'Combustible',   keywords: ['axion'],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://axionenergy.com.ar&size=128' },
  { id: 'gulf',       name: 'GULF',           categoria: 'Combustible',   keywords: ['gulf'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://gulf.com&size=128' },
  { id: 'puma',       name: 'Puma Energy',    categoria: 'Combustible',   keywords: ['puma energy'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://pumaenergy.com&size=128' },

  // ── Farmacias / Salud ────────────────────────────────────────────────────
  { id: 'farmacity',  name: 'Farmacity',      categoria: 'Farmacias',     keywords: ['farmacity'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://farmacity.com&size=128' },
  { id: 'simplicity', name: 'Simplicity',     categoria: 'Farmacias',     keywords: ['simplicity'],             logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://simplicity.com.ar&size=128' },
  { id: 'farmaonline',name: 'Farmaonline',    categoria: 'Farmacias',     keywords: ['farmaonline'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://farmaonline.com&size=128' },
  { id: 'gethelook',  name: 'Get The Look',   categoria: 'Farmacias',     keywords: ['get the look'],           logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://getthelook.com.ar&size=128' },
  { id: 'drahorro',   name: 'Dr Ahorro',      categoria: 'Farmacias',     keywords: ['dr ahorro'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://drdrives.com.ar&size=128' },

  // ── Gastronomía ──────────────────────────────────────────────────────────
  { id: 'mcdonalds',  name: "McDonald's",     categoria: 'Gastronomía',   keywords: ["mcdonald"],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://mcdonalds.com&size=128' },
  { id: 'burgerking', name: 'Burger King',    categoria: 'Gastronomía',   keywords: ['burger king'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://burgerking.com&size=128' },
  { id: 'mostaza',    name: 'Mostaza',        categoria: 'Gastronomía',   keywords: ['mostaza'],                logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://mostaza.com.ar&size=128' },
  { id: 'kfc',        name: 'KFC',            categoria: 'Gastronomía',   keywords: ['kfc'],                    logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://kfc.com&size=128' },
  { id: 'wendys',     name: "Wendy's",        categoria: 'Gastronomía',   keywords: ["wendy"],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://wendys.com&size=128' },
  { id: 'rapanui',    name: 'Rapanui',        categoria: 'Gastronomía',   keywords: ['rapanui'],                logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://rapanuihelados.com&size=128' },
  { id: 'havanna',    name: 'Havanna',        categoria: 'Gastronomía',   keywords: ['havanna'],                logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://havanna.com&size=128' },
  { id: 'luccianos',  name: "Lucciano's",     categoria: 'Gastronomía',   keywords: ["lucciano"],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://luccianos.com.ar&size=128' },
  { id: 'pedidosya',  name: 'PedidosYa',      categoria: 'Gastronomía',   keywords: ['pedidos ya'],             logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://pedidosya.com&size=128' },

  // ── Indumentaria / Deportes ──────────────────────────────────────────────
  { id: 'adidas',     name: 'Adidas',         categoria: 'Indumentaria',  keywords: ['adidas'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://adidas.com&size=128' },
  { id: 'nike',       name: 'Nike',           categoria: 'Indumentaria',  keywords: ['nike'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://nike.com&size=128' },
  { id: 'dexter',     name: 'Dexter',         categoria: 'Indumentaria',  keywords: ['dexter'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://dexter.com.ar&size=128' },
  { id: 'moov',       name: 'Moov',           categoria: 'Indumentaria',  keywords: ['moov'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://moov.com.ar&size=128' },
  { id: 'stockcenter',name: 'Stock Center',   categoria: 'Indumentaria',  keywords: ['stock center'],           logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://stockcenter.com.ar&size=128' },
  { id: 'decathlon',  name: 'Decathlon',      categoria: 'Indumentaria',  keywords: ['decathlon'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://decathlon.com.ar&size=128' },
  { id: 'carocuore',  name: 'Caro Cuore',     categoria: 'Indumentaria',  keywords: ['caro cuore'],             logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://carocuore.com.ar&size=128' },

  // ── Electrónica / Tecnología ─────────────────────────────────────────────
  { id: 'samsung',    name: 'Samsung',        categoria: 'Electrónica',   keywords: ['samsung'],                logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://samsung.com&size=128' },
  { id: 'lg',         name: 'LG',             categoria: 'Electrónica',   keywords: [' lg ', 'lg,'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://lg.com&size=128' },
  { id: 'fravega',    name: 'Frávega',        categoria: 'Electrónica',   keywords: ['frávega', 'fravega'],     logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://fravega.com&size=128' },
  { id: 'megatone',   name: 'Megatone',       categoria: 'Electrónica',   keywords: ['megatone'],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://megatone.net&size=128' },
  { id: 'cetrogar',   name: 'Cetrogar',       categoria: 'Electrónica',   keywords: ['cetrogar'],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://cetrogar.com.ar&size=128' },
  { id: 'motorola',   name: 'Motorola',       categoria: 'Electrónica',   keywords: ['motorola'],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://motorola.com&size=128' },

  // ── Viajes / Transporte ──────────────────────────────────────────────────
  { id: 'despegar',   name: 'Despegar',       categoria: 'Viajes',        keywords: ['despegar'],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://despegar.com&size=128' },
  { id: 'aerolineas', name: 'Aerolíneas Argentinas', categoria: 'Viajes', keywords: ['aerolíneas', 'aerolineas'], logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://aerolineas.com.ar&size=128' },
  { id: 'cabify',     name: 'Cabify',         categoria: 'Viajes',        keywords: ['cabify'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://cabify.com&size=128' },
  { id: 'flechabus',  name: 'Flechabus',      categoria: 'Viajes',        keywords: ['flechabus'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://flechabus.com.ar&size=128' },
  { id: 'almundo',    name: 'Almundo',        categoria: 'Viajes',        keywords: ['almundo'],                logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://almundo.com&size=128' },

  // ── Entretenimiento ──────────────────────────────────────────────────────
  { id: 'cinemark',   name: 'Cinemark / Hoyts', categoria: 'Entretenimiento', keywords: ['cinemark', 'hoyts'],  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://cinemark.com.ar&size=128' },
  { id: 'sportclub',  name: 'Sportclub',      categoria: 'Entretenimiento', keywords: ['sportclub'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://sportclub.com.ar&size=128' },
  { id: 'newman',     name: 'Newman',         categoria: 'Entretenimiento', keywords: ['newman'],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://newman.com.ar&size=128' },

  // ── Librerías ────────────────────────────────────────────────────────────
  { id: 'yenny',      name: 'Yenny / El Ateneo', categoria: 'Librerías',  keywords: ['yenny', 'ateneo'],        logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://elateneo.com&size=128' },
  { id: 'cuspide',    name: 'Cúspide',        categoria: 'Librerías',     keywords: ['cúspide', 'cuspide'],     logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://cuspide.com&size=128' },

  // ── Hogar / Construcción ─────────────────────────────────────────────────
  { id: 'easy',       name: 'Easy',           categoria: 'Hogar',         keywords: ['easy'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://easy.com.ar&size=128' },
  { id: 'natura',     name: 'Natura',         categoria: 'Hogar',         keywords: ['natura'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://natura.com.ar&size=128' },
]

export const CATEGORIAS_MARCA = [
  'Supermercados', 'Combustible', 'Farmacias', 'Gastronomía',
  'Indumentaria', 'Electrónica', 'Viajes', 'Entretenimiento',
  'Librerías', 'Hogar',
]

export function getMarca(slug) {
  return MARCAS.find(m => m.id === slug) ?? null
}
