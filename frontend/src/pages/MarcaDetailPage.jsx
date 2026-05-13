import { useState, useEffect, useMemo } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { getMarca } from '../data/marcas'
import DiscountCard from '../components/DiscountCard'

function useMarcaDiscounts(keywords) {
  const [discounts, setDiscounts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    setLoading(true)
    setError(null)
    const BASE = import.meta.env.VITE_API_URL ?? ''
    fetch(`${BASE}/api/discounts/?limit=300`)
      .then(r => { if (!r.ok) throw new Error(); return r.json() })
      .then(all => {
        const q = keywords.map(k => k.toLowerCase())
        const matched = all.filter(d => {
          const haystack = `${d.title} ${d.description ?? ''} ${d.source}`.toLowerCase()
          return q.some(k => haystack.includes(k))
        })
        setDiscounts(matched)
      })
      .catch(() => setError('No se pudieron cargar los descuentos'))
      .finally(() => setLoading(false))
  }, [keywords.join(',')])

  return { discounts, loading, error }
}

export default function MarcaDetailPage() {
  const { slug } = useParams()
  const navigate = useNavigate()
  const marca = getMarca(slug)

  const { discounts, loading, error } = useMarcaDiscounts(marca?.keywords ?? [])
  const [imgOk, setImgOk] = useState(true)

  if (!marca) {
    return (
      <div className="max-w-6xl mx-auto px-4 py-16 text-center">
        <p className="text-5xl mb-4">❓</p>
        <p className="text-slate-300 font-medium">Marca no encontrada</p>
        <button onClick={() => navigate('/marcas')} className="text-violet-400 text-sm mt-3 hover:underline">
          ← Volver a Multi Marcas
        </button>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Breadcrumb */}
      <button
        onClick={() => navigate('/marcas')}
        className="flex items-center gap-1.5 text-slate-500 hover:text-violet-400 transition-colors text-sm mb-6"
      >
        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
        </svg>
        Multi Marcas
      </button>

      {/* Brand header */}
      <div className="flex items-center gap-5 mb-8 bg-slate-900/60 border border-slate-800 rounded-2xl p-6">
        {imgOk && marca.logo ? (
          <img
            src={marca.logo}
            alt={marca.name}
            onError={() => setImgOk(false)}
            className="w-16 h-16 object-contain bg-white rounded-2xl p-2 border border-slate-700 flex-shrink-0"
          />
        ) : (
          <div className="w-16 h-16 rounded-2xl bg-violet-600/20 border border-violet-500/30 flex items-center justify-center text-violet-400 font-bold text-2xl flex-shrink-0">
            {marca.name[0]}
          </div>
        )}
        <div>
          <span className="text-xs text-slate-500 uppercase tracking-wide">{marca.categoria}</span>
          <h2 className="text-2xl font-bold text-white">{marca.name}</h2>
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
          {Array.from({ length: 3 }).map((_, i) => (
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
          <p className="text-slate-300 font-medium">No hay descuentos activos para {marca.name}</p>
          <p className="text-slate-500 text-sm mt-1">
            Puede que los descuentos de esta marca estén disponibles próximamente.
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
