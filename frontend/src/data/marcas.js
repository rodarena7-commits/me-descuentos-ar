// Catálogo de marcas adheridas a descuentos en Argentina.
// keywords: array de strings que se buscan en title + description de cada descuento.
// Todas en minúsculas para matching case-insensitive.

export const MARCAS = [
  // ── Supermercados ────────────────────────────────────────────────────────
  { id: 'carrefour',  name: 'Carrefour',      categoria: 'Supermercados', keywords: ['carrefour'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://carrefour.com.ar&size=128' },
  { id: 'coto',       name: 'Coto',           categoria: 'Supermercados', keywords: ['coto'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://coto.com.ar&size=128' },
  { id: 'jumbo',      name: 'Jumbo',          categoria: 'Supermercados', keywords: ['jumbo'],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://jumbo.com.ar&size=128' },
  { id: 'disco',      name: 'Disco / Vea',    categoria: 'Supermercados', keywords: ['disco', 'vea'],           logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://disco.com.ar&size=128' },
  { id: 'dia',        name: 'Supermercado Día', categoria: 'Supermercados', keywords: ['supermercado día', 'supermercado dia', 'en día', 'en dia'], logo: 'https://i.pinimg.com/736x/a9/3a/17/a93a17ad28f3edc51c08cbf28130bc27.jpg' },
  { id: 'changomas',  name: 'Chango Más',     categoria: 'Supermercados', keywords: ['chango más', 'chango mas', 'changomás'], logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://changomas.com.ar&size=128' },
  { id: 'open25h',    name: 'Open 25h',       categoria: 'Supermercados', keywords: ['open 25h'],               logo: 'https://acdn-us.mitiendanube.com/stores/006/038/294/themes/common/logo-275663435-1756774944-d0b736e82b0746e83bb9a0f6136eb3d91756774944-480-0.webp' },
  { id: 'lanónima',   name: 'La Anónima',     categoria: 'Supermercados', keywords: ['anónima', 'anonima'],     logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://laanonimaonline.com&size=128' },
  { id: 'diarco',     name: 'Diarco',         categoria: 'Supermercados', keywords: ['diarco'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://diarco.com.ar&size=128' },

  // ── Combustible ──────────────────────────────────────────────────────────
  { id: 'ypf',        name: 'YPF',            categoria: 'Combustible',   keywords: ['ypf'],                    logo: 'https://i.pinimg.com/736x/67/05/1e/67051edb05b11de24cea7f39a5253545.jpg' },
  { id: 'shell',      name: 'Shell',          categoria: 'Combustible',   keywords: ['shell'],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://shell.com&size=128' },
  { id: 'axion',      name: 'Axion Energy',   categoria: 'Combustible',   keywords: ['axion'],                  logo: 'https://i.pinimg.com/736x/86/e6/46/86e64634d8cf26f7432e2bc09403798d.jpg' },
  { id: 'gulf',       name: 'GULF',           categoria: 'Combustible',   keywords: ['gulf'],                   logo: 'https://i.pinimg.com/1200x/f3/07/6f/f3076fdd21cdc09d79f3403502ed9769.jpg' },
  { id: 'puma',       name: 'Puma Energy',    categoria: 'Combustible',   keywords: ['puma energy'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://pumaenergy.com&size=128' },

  // ── Farmacias / Salud ────────────────────────────────────────────────────
  { id: 'farmacity',  name: 'Farmacity',      categoria: 'Farmacias',     keywords: ['farmacity'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://farmacity.com&size=128' },
  { id: 'simplicity', name: 'Simplicity',     categoria: 'Farmacias',     keywords: ['simplicity'],             logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://simplicity.com.ar&size=128' },
  { id: 'farmaonline',name: 'Farmaonline',    categoria: 'Farmacias',     keywords: ['farmaonline'],            logo: 'https://assets.hotsale.com.ar/uploads/brands/18860/orig-1776281185-farmaonline.jpg' },
  { id: 'gethelook',  name: 'Get The Look',   categoria: 'Farmacias',     keywords: ['get the look'],           logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://getthelook.com.ar&size=128' },
  { id: 'drahorro',   name: 'Dr Ahorro',      categoria: 'Farmacias',     keywords: ['dr ahorro'],              logo: 'https://images.seeklogo.com/logo-png/43/1/farmacias-dr-ahorro-logo-png_seeklogo-430759.png' },

  // ── Gastronomía ──────────────────────────────────────────────────────────
  { id: 'mcdonalds',  name: "McDonald's",     categoria: 'Gastronomía',   keywords: ["mcdonald"],               logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://mcdonalds.com&size=128' },
  { id: 'burgerking', name: 'Burger King',    categoria: 'Gastronomía',   keywords: ['burger king'],            logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://burgerking.com&size=128' },
  { id: 'mostaza',    name: 'Mostaza',        categoria: 'Gastronomía',   keywords: ['mostaza'],                logo: 'https://i.pinimg.com/1200x/7c/e7/02/7ce702c6dddebcb54817cc28b5bc9afd.jpg' },
  { id: 'kfc',        name: 'KFC',            categoria: 'Gastronomía',   keywords: ['kfc'],                    logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://kfc.com&size=128' },
  { id: 'wendys',     name: "Wendy's",        categoria: 'Gastronomía',   keywords: ["wendy"],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://wendys.com&size=128' },
  { id: 'rapanui',    name: 'Rapanui',        categoria: 'Gastronomía',   keywords: ['rapanui'],                logo: 'https://i.pinimg.com/736x/c2/a6/2f/c2a62f711b21dc13d8ffd7b3e425fc4a.jpg' },
  { id: 'havanna',    name: 'Havanna',        categoria: 'Gastronomía',   keywords: ['havanna'],                logo: 'https://i.pinimg.com/736x/9c/12/ee/9c12eece72840c999014efa99faa994e.jpg' },
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
  { id: 'aerolineas', name: 'Aerolíneas Argentinas', categoria: 'Viajes', keywords: ['aerolíneas', 'aerolineas'], logo: 'https://i.pinimg.com/1200x/7c/cb/a8/7ccba809b9309e29383287a7c94a6978.jpg' },
  { id: 'cabify',     name: 'Cabify',         categoria: 'Viajes',        keywords: ['cabify'],                 logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://cabify.com&size=128' },
  { id: 'flechabus',  name: 'Flechabus',      categoria: 'Viajes',        keywords: ['flechabus'],              logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://flechabus.com.ar&size=128' },
  { id: 'almundo',    name: 'Almundo',        categoria: 'Viajes',        keywords: ['almundo'],                logo: 'https://i.pinimg.com/280x280_RS/87/78/19/877819af49b541c7157872048d9be78d.jpg' },

  // ── Entretenimiento ──────────────────────────────────────────────────────
  { id: 'cinemark',   name: 'Cinemark / Hoyts', categoria: 'Entretenimiento', keywords: ['cinemark', 'hoyts'],  logo: 'https://i.pinimg.com/1200x/2c/aa/6f/2caa6f67d1111a8731dc8d05bb64ac40.jpg' },
  { id: 'sportclub',  name: 'Sportclub',      categoria: 'Entretenimiento', keywords: ['sportclub'],            logo: 'https://images.seeklogo.com/logo-png/62/1/sportclub-logo-png_seeklogo-626111.png' },
  { id: 'newman',     name: 'Newman',         categoria: 'Entretenimiento', keywords: ['newman'],               logo: 'https://i.pinimg.com/736x/c9/1d/c9/c91dc94730f6ff65c110a0d06b786194.jpg' },

  // ── Librerías ────────────────────────────────────────────────────────────
  { id: 'yenny',      name: 'Yenny / El Ateneo', categoria: 'Librerías',  keywords: ['yenny', 'ateneo'],        logo: 'https://acdn-us.mitiendanube.com/stores/004/088/117/themes/common/logo-810418616-1731438736-7b6920ff653fd2214af40085c6145fea1731438737-320-0.webp' },
  { id: 'cuspide',    name: 'Cúspide',        categoria: 'Librerías',     keywords: ['cúspide', 'cuspide'],     logo: 'https://i.pinimg.com/736x/f3/bc/44/f3bc44ab765d51e227b0c31955d8a35f.jpg' },

  // ── Hogar / Construcción ─────────────────────────────────────────────────
  { id: 'easy',       name: 'Easy',           categoria: 'Hogar',         keywords: ['easy'],                   logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://easy.com.ar&size=128' },
  { id: 'natura',     name: 'Natura',         categoria: 'Hogar',         keywords: ['natura'],                 logo: 'https://i.pinimg.com/1200x/12/ea/5f/12ea5f3612861d9d80493a207e67f33d.jpg' },

  // ── Crypto / Fintech ─────────────────────────────────────────────────────
  { id: 'ripio',     name: 'Ripio',           categoria: 'Crypto',        keywords: ['ripio'],                  logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://ripio.com&size=128' },
  { id: 'astropay',  name: 'AstroPay',        categoria: 'Crypto',        keywords: ['astropay'],               logo: 'https://i.pinimg.com/736x/a5/a6/00/a5a600775bff34cd9842e3555110c144.jpg' },
  { id: 'letsbit',   name: "Let'sBit",        categoria: 'Crypto',        keywords: ["let'sbit", 'letsbit', 'lb finanzas'], logo: 'https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://letsbit.io&size=128' },
]

export const CATEGORIAS_MARCA = [
  'Supermercados', 'Combustible', 'Farmacias', 'Gastronomía',
  'Indumentaria', 'Electrónica', 'Viajes', 'Entretenimiento',
  'Librerías', 'Hogar', 'Crypto',
]

export function getMarca(slug) {
  return MARCAS.find(m => m.id === slug) ?? null
}
