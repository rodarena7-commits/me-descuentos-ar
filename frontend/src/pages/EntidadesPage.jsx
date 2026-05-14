import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { ENTIDADES, TIPOS_ENTIDAD } from '../data/entidades'

const TIPO_STYLES = {
  Banco:    'bg-sky-500/20 text-sky-400 border-sky-500/30',
  Fintech:  'bg-violet-500/20 text-violet-400 border-violet-500/30',
  Exchange: 'bg-amber-500/20 text-amber-400 border-amber-500/30',
}

const TIPO_SECTION_COLOR = {
  Banco:    'text-sky-400',
  Fintech:  'text-violet-400',
  Exchange: 'text-amber-400',
}

function EntidadCard({ entidad }) {
  const navigate = useNavigate()
  const [imgOk, setImgOk] = useState(true)

  return (
    <button
      onClick={() => navigate(`/entidades/${entidad.id}`)}
      className="group flex flex-col items-center gap-3 p-4 bg-slate-900/60 border border-slate-800 rounded-2xl hover:border-violet-500/50 hover:bg-slate-800/60 transition-all duration-200 hover:shadow-lg hover:shadow-violet-500/5 cursor-pointer"
    >
      {imgOk && entidad.logo ? (
        <img
          src={entidad.logo}
          alt={entidad.name}
          onError={() => setImgOk(false)}
          className="w-12 h-12 object-contain bg-white rounded-xl p-1.5 border border-slate-700"
        />
      ) : (
        <div className="w-12 h-12 rounded-xl bg-violet-600/20 border border-violet-500/30 flex items-center justify-center text-violet-400 font-bold text-lg">
          {entidad.name[0]}
        </div>
      )}
      <div className="flex flex-col items-center gap-1">
        <span className="text-slate-300 text-sm font-medium text-center group-hover:text-violet-300 transition-colors leading-tight">
          {entidad.name}
        </span>
        <span className={`text-xs px-2 py-0.5 rounded-full border font-medium ${TIPO_STYLES[entidad.tipo]}`}>
          {entidad.tipo}
        </span>
      </div>
    </button>
  )
}

export default function EntidadesPage() {
  const [tipoFilter, setTipoFilter] = useState('')
  const [search, setSearch] = useState('')

  const visible = ENTIDADES.filter(e => {
    const matchTipo = !tipoFilter || e.tipo === tipoFilter
    const matchSearch = !search || e.name.toLowerCase().includes(search.toLowerCase())
    return matchTipo && matchSearch
  })

  const grouped = TIPOS_ENTIDAD.reduce((acc, tipo) => {
    const items = visible.filter(e => e.tipo === tipo)
    if (items.length) acc[tipo] = items
    return acc
  }, {})

  return (
    <div>
      {/* Header */}
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-white mb-1">
          Bancos, Fintechs y Exchanges
        </h2>
        <p className="text-slate-400 text-sm">
          Seleccioná una entidad para ver todos sus descuentos, promos y reintegros.
        </p>
      </div>

      {/* Filtros */}
      <div className="flex flex-wrap gap-3 mb-8">
        <div className="relative flex-1 min-w-[180px] max-w-xs">
          <input
            type="text"
            value={search}
            onChange={e => setSearch(e.target.value)}
            placeholder="Buscar entidad..."
            className="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-slate-200 text-sm placeholder-slate-500 focus:outline-none focus:border-violet-500 transition-colors"
          />
        </div>
        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => setTipoFilter('')}
            className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all cursor-pointer ${
              !tipoFilter
                ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                : 'bg-slate-800/60 text-slate-500 border-slate-700 hover:text-slate-300'
            }`}
          >
            Todos
          </button>
          {TIPOS_ENTIDAD.map(tipo => (
            <button
              key={tipo}
              onClick={() => setTipoFilter(t => t === tipo ? '' : tipo)}
              className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all cursor-pointer ${
                tipoFilter === tipo
                  ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                  : 'bg-slate-800/60 text-slate-500 border-slate-700 hover:text-slate-300'
              }`}
            >
              {tipo === 'Banco' ? 'Bancos' : tipo === 'Fintech' ? 'Fintechs' : 'Exchanges'}
            </button>
          ))}
        </div>
      </div>

      {/* Grilla por tipo */}
      {Object.entries(grouped).map(([tipo, items]) => (
        <div key={tipo} className="mb-10">
          <h3 className={`text-sm font-semibold uppercase tracking-widest mb-4 ${TIPO_SECTION_COLOR[tipo]}`}>
            {tipo === 'Banco' ? 'Bancos' : tipo === 'Fintech' ? 'Fintechs' : 'Exchanges & Crypto'}
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
            {items.map(e => <EntidadCard key={e.id} entidad={e} />)}
          </div>
        </div>
      ))}

      {visible.length === 0 && (
        <div className="text-center py-16">
          <p className="text-5xl mb-4">🔍</p>
          <p className="text-slate-300 font-medium">Sin resultados para "{search}"</p>
          <button
            onClick={() => { setSearch(''); setTipoFilter('') }}
            className="text-violet-400 text-sm mt-2 hover:underline"
          >
            Limpiar filtros
          </button>
        </div>
      )}
    </div>
  )
}
