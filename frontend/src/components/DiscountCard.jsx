import { useState } from 'react'
import { format, differenceInDays, isPast } from 'date-fns'
import { es } from 'date-fns/locale'

const TYPE_STYLES = {
  descuento: 'bg-blue-500/20 text-blue-400 border border-blue-500/30',
  reintegro: 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30',
  promocion: 'bg-violet-500/20 text-violet-400 border border-violet-500/30',
}

const TYPE_LABELS = {
  descuento: 'Descuento',
  reintegro: 'Reintegro',
  promocion: 'Promoción',
}

// Dominios para Google Favicons API como segundo intento
const BRAND = {
  'Banco Galicia':  { domain: 'galicia.ar',         color: 'bg-red-600',      text: 'text-white' },
  'Santander':      { domain: 'santander.com.ar',    color: 'bg-red-700',      text: 'text-white' },
  'BBVA':           { domain: 'bbva.com.ar',         color: 'bg-blue-600',     text: 'text-white' },
  'Banco Nación':   { domain: 'bna.com.ar',          color: 'bg-sky-700',      text: 'text-white' },
  'Banco Macro':    { domain: 'macro.com.ar',        color: 'bg-yellow-500',   text: 'text-slate-900' },
  'MercadoPago':    { domain: 'mercadopago.com',     color: 'bg-sky-400',      text: 'text-white' },
  'Naranja X':      { domain: 'naranjax.com',        color: 'bg-orange-500',   text: 'text-white' },
  'Lemon':          { domain: 'lemon.me',            color: 'bg-lime-400',     text: 'text-slate-900' },
  'MODO':           { domain: 'modo.com.ar',         color: 'bg-indigo-600',   text: 'text-white' },
  'Cuenta DNI':     { domain: 'cuentadni.ar',        color: 'bg-sky-500',      text: 'text-white' },
  'Banco Patagonia':{ domain: 'bancopatagonia.com.ar',color: 'bg-emerald-700', text: 'text-white' },
  'Ualá':           { domain: 'uala.com.ar',          color: 'bg-violet-800',   text: 'text-white' },
  'Brubank':        { domain: 'brubank.com',           color: 'bg-teal-600',     text: 'text-white' },
  'Personal Pay':   { domain: 'personalpay.com.ar',   color: 'bg-purple-700',   text: 'text-white' },
  'Supervielle':    { domain: 'supervielle.com.ar',   color: 'bg-red-800',      text: 'text-white' },
  'Banco Ciudad':   { domain: 'bancociudad.com.ar',   color: 'bg-green-600',    text: 'text-white' },
  'ICBC':           { domain: 'icbc.com.ar',           color: 'bg-red-700',      text: 'text-white' },
}


const CATEGORY_LABELS = {
  supermercados:    'Supermercados',
  combustible:      'Combustible',
  farmacias:        'Farmacias',
  gastronomia:      'Gastronomía',
  indumentaria:     'Indumentaria',
  viajes:           'Viajes',
  electronica:      'Electrónica',
  entretenimiento:  'Entretenimiento',
  librerias:        'Librerías',
  jugueterias:      'Jugueterías',
  neumaticos:       'Neumáticos',
  peluquerias:      'Peluquerías',
  opticas:          'Ópticas',
  transporte:       'Transporte',
  servicios:        'Servicios públicos',
  educacion:        'Educación',
  hogar:            'Hogar',
  todos:            'Todos',
  varios:           'Varios',
}

// Usa la API de favicons de Google (alta resolución, no bloqueada por ad blockers)
function gFavicon(domain) {
  return `https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://${domain}&size=128`
}

function SourceLogo({ source, logoUrl }) {
  const brand = BRAND[source]
  // Si el source está en BRAND, usar Google Favicon API directamente (ignora clearbit bloqueado)
  // Si tiene URL propia (Pinterest, etc.), usarla como primaria
  const isPinterest = logoUrl?.includes('pinimg.com')
  const initialSrc = isPinterest
    ? logoUrl
    : (brand ? gFavicon(brand.domain) : logoUrl)

  const [src, setSrc] = useState(initialSrc)
  const [triedFallback, setTriedFallback] = useState(false)

  function handleError() {
    if (!triedFallback && isPinterest && brand) {
      setTriedFallback(true)
      setSrc(gFavicon(brand.domain))
    } else {
      setSrc(null)
    }
  }

  if (src) {
    return (
      <img
        src={src}
        alt={source}
        className="w-11 h-11 rounded-lg object-contain bg-white p-1 border border-slate-700 flex-shrink-0"
        onError={handleError}
      />
    )
  }

  const color = brand?.color || 'bg-violet-600'
  const textColor = brand?.text || 'text-white'
  return (
    <div className={`w-11 h-11 rounded-lg ${color} flex items-center justify-center ${textColor} font-bold text-lg flex-shrink-0`}>
      {source[0]}
    </div>
  )
}

function ExpiryBadge({ validUntil }) {
  if (!validUntil) return null
  const date = new Date(validUntil)
  if (isPast(date)) return <span className="text-xs text-red-400 font-medium">Vencido</span>
  const days = differenceInDays(date, new Date())
  if (days <= 3)
    return (
      <span className="text-xs text-amber-400 font-medium">
        ⏰ Vence {days === 0 ? 'hoy' : `en ${days}d`}
      </span>
    )
  return <span className="text-xs text-slate-500">{format(date, "d MMM", { locale: es })}</span>
}

const DAY_LABELS = {
  lunes: 'Lunes',
  martes: 'Martes',
  miercoles: 'Miércoles',
  jueves: 'Jueves',
  viernes: 'Viernes',
  sabado: 'Sábado',
  domingo: 'Domingo',
  todos: null,
}

function DayBadge({ daysOfWeek }) {
  if (!daysOfWeek || daysOfWeek === 'todos') return null
  const days = daysOfWeek.split(',').map(d => DAY_LABELS[d.trim()] || d.trim()).filter(Boolean)
  return (
    <span className="text-xs px-2 py-0.5 rounded-full bg-slate-700/60 text-slate-400 border border-slate-600/50">
      {days.join(' · ')}
    </span>
  )
}

export default function DiscountCard({ discount }) {
  const {
    title, description, discount_type, percentage, max_amount,
    source, logo_url, url, category, days_of_week,
    valid_until, is_limited_stock, is_new,
  } = discount

  return (
    <a
      href={url || '#'}
      target="_blank"
      rel="noopener noreferrer"
      className="group block bg-slate-900/60 border border-slate-800 rounded-xl p-4 hover:border-violet-500/50 hover:bg-slate-800/60 transition-all duration-200 hover:shadow-lg hover:shadow-violet-500/5"
    >
      <div className="flex items-start gap-3">
        <SourceLogo source={source} logoUrl={logo_url} />

        <div className="flex-1 min-w-0">
          <div className="flex flex-wrap items-center gap-1.5 mb-1.5">
            <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${TYPE_STYLES[discount_type] || 'bg-slate-700 text-slate-400'}`}>
              {TYPE_LABELS[discount_type] || discount_type}
            </span>
            {is_new && (
              <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                Nuevo
              </span>
            )}
            {is_limited_stock && (
              <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-red-500/20 text-red-400 border border-red-500/30">
                ⚡ Stock
              </span>
            )}
          </div>

          <h3 className="font-semibold text-slate-200 text-sm leading-snug group-hover:text-violet-300 transition-colors">
            {title}
          </h3>

          {description && (
            <p className="text-xs text-slate-500 mt-1 line-clamp-2">{description}</p>
          )}

          <div className="flex flex-wrap items-center gap-2 mt-2">
            {percentage && (
              <span className="text-xl font-bold text-violet-400">{percentage}%</span>
            )}
            {max_amount && (
              <span className="text-xs text-slate-500">
                tope <span className="text-slate-400">${max_amount.toLocaleString('es-AR')}</span>
              </span>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2 mt-2 text-xs">
            <span className="font-medium text-slate-400">{source}</span>
            {category && <span className="text-slate-600">·</span>}
            {category && <span className="text-slate-500">{CATEGORY_LABELS[category] ?? category}</span>}
            <DayBadge daysOfWeek={days_of_week} />
            <ExpiryBadge validUntil={valid_until} />
          </div>
        </div>
      </div>
    </a>
  )
}
