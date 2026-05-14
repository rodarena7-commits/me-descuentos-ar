import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { getEntidad } from '../data/entidades'
import DiscountCard from '../components/DiscountCard'

const TIPO_STYLES = {
  Banco:    'bg-sky-500/20 text-sky-400 border-sky-500/30',
  Fintech:  'bg-violet-500/20 text-violet-400 border-violet-500/30',
  Exchange: 'bg-amber-500/20 text-amber-400 border-amber-500/30',
}

function useEntidadDiscounts(source) {
  const [discounts, setDiscounts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (!source) return
    setLoading(true)
    setError(null)
    const BASE = import.meta.env.VITE_API_URL ?? ''
    fetch(`${BASE}/api/discounts/?source=${encodeURIComponent(source)}&limit=300`)
      .then(r => { if (!r.ok) throw new Error(); return r.json() })
      .then(setDiscounts)
      .catch(() => setError('No se pudieron cargar los descuentos'))
      .finally(() => setLoading(false))
  }, [source])

  return { discounts, loading, error }
}

export default function EntidadDetailPage() {
  const { slug } = useParams()
  const navigate = useNavigate()
  const entidad = getEntidad(slug)
  const [imgOk, setImgOk] = useState(true)

  const { discounts, loading, error } = useEntidadDiscounts(entidad?.source)

  if (!entidad) {
    return (
      <div className="py-16 text-center">
        <p className="text-5xl mb-4">❓</p>
        <p className="text-slate-300 font-medium">Entidad no encontrada</p>
        <button
          onClick={() => navigate('/entidades')}
          className="text-violet-400 text-sm mt-3 hover:underline"
        >
          ← Volver a Entidades
        </button>
      </div>
    )
  }

  return (
    <div>
      {/* Breadcrumb */}
      <button
        onClick={() => navigate('/entidades')}
        className="flex items-center gap-1.5 text-slate-500 hover:text-violet-400 transition-colors text-sm mb-6"
      >
        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
        </svg>
        Bancos, Fintechs y Exchanges
      </button>

      {/* Header de la entidad */}
      <div className="flex items-center gap-5 mb-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
        {imgOk && entidad.logo ? (
          <img
            src={entidad.logo}
            alt={entidad.name}
            onError={() => setImgOk(false)}
            className="w-16 h-16 object-contain bg-white rounded-2xl p-2 border border-slate-700 flex-shrink-0"
          />
        ) : (
          <div className="w-16 h-16 rounded-2xl bg-violet-600/20 border border-violet-500/30 flex items-center justify-center text-violet-400 font-bold text-2xl flex-shrink-0">
            {entidad.name[0]}
          </div>
        )}
        <div>
          <span className={`text-xs font-semibold px-2 py-0.5 rounded-full border ${TIPO_STYLES[entidad.tipo]}`}>
            {entidad.tipo}
          </span>
          <h2 className="text-2xl font-bold text-white mt-1">{entidad.name}</h2>
          {!loading && (
            <p className="text-slate-400 text-sm mt-0.5">
              {discounts.length > 0
                ? `${discounts.length} descuento${discounts.length !== 1 ? 's' : ''} disponible${discounts.length !== 1 ? 's' : ''}`
                : 'Sin descuentos activos por el momento'}
            </p>
          )}
        </div>
      </div>

      {/* Descuentos */}
      {loading && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 animate-pulse h-32" />
          ))}
        </div>
      )}

      {error && (
        <div className="text-center py-12">
          <p className="text-slate-400">{error}</p>
        </div>
      )}

      {!loading && !error && discounts.length === 0 && (
        <div className="text-center py-16 bg-slate-900/40 border border-slate-800 rounded-2xl">
          <p className="text-4xl mb-4">🔍</p>
          <p className="text-slate-300 font-medium">No hay descuentos activos para {entidad.name}</p>
          <p className="text-slate-500 text-sm mt-1">
            Los descuentos de esta entidad pueden estar disponibles próximamente.
          </p>
        </div>
      )}

      {!loading && !error && discounts.length > 0 && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {discounts.map(d => <DiscountCard key={d.id} discount={d} />)}
        </div>
      )}
    </div>
  )
}
