import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { MARCAS, CATEGORIAS_MARCA } from '../data/marcas'

function BrandCard({ marca }) {
  const navigate = useNavigate()
  const [imgOk, setImgOk] = useState(true)

  return (
    <button
      onClick={() => navigate(`/marcas/${marca.id}`)}
      className="group flex flex-col items-center gap-3 p-4 bg-slate-900/60 border border-slate-800 rounded-2xl hover:border-violet-500/50 hover:bg-slate-800/60 transition-all duration-200 hover:shadow-lg hover:shadow-violet-500/5 cursor-pointer"
    >
      {imgOk && marca.logo ? (
        <img
          src={marca.logo}
          alt={marca.name}
          onError={() => setImgOk(false)}
          className="w-12 h-12 object-contain bg-white rounded-xl p-1.5 border border-slate-700"
        />
      ) : (
        <div className="w-12 h-12 rounded-xl bg-violet-600/20 border border-violet-500/30 flex items-center justify-center text-violet-400 font-bold text-lg">
          {marca.name[0]}
        </div>
      )}
      <span className="text-slate-300 text-sm font-medium text-center group-hover:text-violet-300 transition-colors leading-tight">
        {marca.name}
      </span>
    </button>
  )
}

export default function MarcasPage() {
  const [catFilter, setCatFilter] = useState('')
  const [search, setSearch] = useState('')

  const visible = MARCAS.filter(m => {
    const matchCat = !catFilter || m.categoria === catFilter
    const matchSearch = !search || m.name.toLowerCase().includes(search.toLowerCase())
    return matchCat && matchSearch
  })

  const grouped = CATEGORIAS_MARCA.reduce((acc, cat) => {
    const items = visible.filter(m => m.categoria === cat)
    if (items.length) acc[cat] = items
    return acc
  }, {})

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-white mb-1">
          Multi Marcas
        </h2>
        <p className="text-slate-400 text-sm">
          Seleccioná una marca para ver todos sus descuentos disponibles.
        </p>
      </div>

      {/* Filtros */}
      <div className="flex flex-wrap gap-3 mb-8">
        <div className="relative flex-1 min-w-[180px] max-w-xs">
          <input
            type="text"
            value={search}
            onChange={e => setSearch(e.target.value)}
            placeholder="Buscar marca..."
            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm placeholder-slate-500 focus:outline-none focus:border-violet-500 transition-colors"
          />
        </div>
        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => setCatFilter('')}
            className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all cursor-pointer ${
              !catFilter
                ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                : 'bg-slate-800/60 text-slate-500 border-slate-700 hover:text-slate-300'
            }`}
          >
            Todas
          </button>
          {CATEGORIAS_MARCA.map(cat => (
            <button
              key={cat}
              onClick={() => setCatFilter(c => c === cat ? '' : cat)}
              className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all cursor-pointer ${
                catFilter === cat
                  ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                  : 'bg-slate-800/60 text-slate-500 border-slate-700 hover:text-slate-300'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {/* Grilla por categoría */}
      {Object.entries(grouped).map(([cat, items]) => (
        <div key={cat} className="mb-10">
          <h3 className="text-sm font-semibold text-slate-400 uppercase tracking-widest mb-4">
            {cat}
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3">
            {items.map(m => <BrandCard key={m.id} marca={m} />)}
          </div>
        </div>
      ))}

      {visible.length === 0 && (
        <div className="text-center py-16">
          <p className="text-5xl mb-4">🔍</p>
          <p className="text-slate-300 font-medium">Sin marcas para "{search}"</p>
          <button onClick={() => { setSearch(''); setCatFilter('') }} className="text-violet-400 text-sm mt-2 hover:underline">
            Limpiar filtros
          </button>
        </div>
      )}
    </div>
  )
}
