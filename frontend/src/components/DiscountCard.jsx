import { format, differenceInDays, isPast } from 'date-fns'
import { es } from 'date-fns/locale'

const TYPE_STYLES = {
  descuento: 'bg-blue-100 text-blue-700',
  reintegro: 'bg-green-100 text-green-700',
  promocion: 'bg-purple-100 text-purple-700',
}

const TYPE_LABELS = {
  descuento: 'Descuento',
  reintegro: 'Reintegro',
  promocion: 'Promoción',
}

function ExpiryBadge({ validUntil }) {
  if (!validUntil) return null
  const date = new Date(validUntil)
  if (isPast(date)) return <span className="text-xs text-red-500 font-medium">Vencido</span>
  const days = differenceInDays(date, new Date())
  if (days <= 3)
    return <span className="text-xs text-amber-600 font-medium">⏰ Vence en {days === 0 ? 'hoy' : `${days}d`}</span>
  return <span className="text-xs text-slate-400">{format(date, "d MMM", { locale: es })}</span>
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
      className="block bg-white rounded-xl border border-slate-200 p-4 hover:shadow-md hover:border-indigo-300 transition-all group"
    >
      <div className="flex items-start gap-3">
        {logo_url ? (
          <img
            src={logo_url}
            alt={source}
            className="w-10 h-10 rounded-lg object-contain border border-slate-100 p-1 flex-shrink-0"
            onError={e => { e.target.style.display = 'none' }}
          />
        ) : (
          <div className="w-10 h-10 rounded-lg bg-indigo-100 flex items-center justify-center text-indigo-600 font-bold flex-shrink-0">
            {source[0]}
          </div>
        )}

        <div className="flex-1 min-w-0">
          <div className="flex flex-wrap items-center gap-1.5 mb-1">
            <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${TYPE_STYLES[discount_type] || 'bg-slate-100 text-slate-600'}`}>
              {TYPE_LABELS[discount_type] || discount_type}
            </span>
            {is_new && (
              <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">
                Nuevo
              </span>
            )}
            {is_limited_stock && (
              <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-red-100 text-red-600">
                ⚡ Stock limitado
              </span>
            )}
          </div>

          <h3 className="font-semibold text-slate-800 text-sm leading-snug group-hover:text-indigo-600 transition-colors">
            {title}
          </h3>

          {description && (
            <p className="text-xs text-slate-500 mt-1 line-clamp-2">{description}</p>
          )}

          <div className="flex flex-wrap items-center gap-3 mt-2">
            {percentage && (
              <span className="text-lg font-bold text-indigo-600">{percentage}%</span>
            )}
            {max_amount && (
              <span className="text-xs text-slate-500">tope ${max_amount.toLocaleString('es-AR')}</span>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2 mt-2 text-xs text-slate-400">
            <span className="font-medium text-slate-600">{source}</span>
            {category && <span>· {category}</span>}
            {days_of_week && days_of_week !== 'todos' && <span>· {days_of_week}</span>}
            <ExpiryBadge validUntil={valid_until} />
          </div>
        </div>
      </div>
    </a>
  )
}
