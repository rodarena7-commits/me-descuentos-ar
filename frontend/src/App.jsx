import { useState } from 'react'
import StatsBar from './components/StatsBar'
import FilterBar from './components/FilterBar'
import DiscountCard from './components/DiscountCard'
import { useDiscounts } from './hooks/useDiscounts'
import './index.css'

function Skeleton() {
  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 animate-pulse">
      <div className="flex gap-3">
        <div className="w-11 h-11 bg-slate-800 rounded-lg flex-shrink-0" />
        <div className="flex-1 space-y-2.5">
          <div className="flex gap-2">
            <div className="h-4 bg-slate-800 rounded-full w-20" />
            <div className="h-4 bg-slate-800 rounded-full w-14" />
          </div>
          <div className="h-4 bg-slate-800 rounded w-4/5" />
          <div className="h-3 bg-slate-800 rounded w-3/5" />
          <div className="h-6 bg-slate-800 rounded w-16 mt-1" />
        </div>
      </div>
    </div>
  )
}

export default function App() {
  const [filters, setFilters] = useState({})
  const { discounts, loading, error } = useDiscounts(filters)

  return (
    <div className="min-h-screen bg-[#020617]">
      {/* Header */}
      <header className="border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md sticky top-0 z-20">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center text-white font-black text-xs tracking-tight shadow-lg shadow-violet-500/30">
              AI
            </div>
            <div>
              <span className="text-white font-bold text-lg">Ahorro Inteligente</span>
              <span className="text-slate-500 text-sm ml-2 hidden sm:inline">
                Descuentos · Argentina
              </span>
            </div>
          </div>
          <div className="flex items-center gap-2 text-xs text-slate-500">
            <span className="w-2 h-2 rounded-full bg-emerald-500 inline-block animate-pulse" />
            En vivo
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Hero */}
        <div className="mb-8 text-center">
          <h1 className="text-3xl md:text-4xl font-bold text-white mb-2">
            Ahorro Inteligente{' '}
            <span className="text-violet-400">— AI</span>
          </h1>
          <p className="text-slate-400 text-sm md:text-base">
            Todos los descuentos, promos y reintegros de bancos y billeteras de Argentina
          </p>
        </div>

        <StatsBar />
        <FilterBar filters={filters} onChange={setFilters} />

        {loading && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Array.from({ length: 9 }).map((_, i) => <Skeleton key={i} />)}
          </div>
        )}

        {error && (
          <div className="text-center py-16">
            <p className="text-4xl mb-4">⚠️</p>
            <p className="text-slate-300 font-medium">No se pudieron cargar los descuentos</p>
            <p className="text-slate-500 text-sm mt-1">{error}</p>
          </div>
        )}

        {!loading && !error && discounts.length === 0 && (
          <div className="text-center py-16">
            <p className="text-5xl mb-4">🔍</p>
            <p className="text-slate-300 font-medium">No hay descuentos con esos filtros</p>
            <p className="text-slate-500 text-sm mt-1">Probá cambiando los filtros</p>
          </div>
        )}

        {!loading && !error && discounts.length > 0 && (
          <>
            <p className="text-xs text-slate-600 mb-4 uppercase tracking-wide">
              {discounts.length} descuentos encontrados
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {discounts.map(d => <DiscountCard key={d.id} discount={d} />)}
            </div>
          </>
        )}
      </main>

      <footer className="border-t border-slate-800/50 mt-16 py-6 text-center text-xs text-slate-600">
        Ahorro Inteligente (AI) · Descuentos Argentina · Los datos son informativos, verificá en el sitio oficial
      </footer>
    </div>
  )
}
