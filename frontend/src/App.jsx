import { useState } from 'react'
import StatsBar from './components/StatsBar'
import FilterBar from './components/FilterBar'
import DiscountCard from './components/DiscountCard'
import { useDiscounts } from './hooks/useDiscounts'
import './index.css'

export default function App() {
  const [filters, setFilters] = useState({})
  const { discounts, loading, error } = useDiscounts(filters)

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="bg-white border-b border-slate-200 sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center gap-3">
          <div className="text-2xl font-bold text-indigo-600">Me</div>
          <div className="text-slate-400 text-sm">Descuentos y promociones de bancos y fintechs Argentina</div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-6">
        <StatsBar />
        <FilterBar filters={filters} onChange={setFilters} />

        {loading && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Array.from({ length: 6 }).map((_, i) => (
              <div key={i} className="bg-white rounded-xl border border-slate-200 p-4 h-36 animate-pulse">
                <div className="flex gap-3">
                  <div className="w-10 h-10 bg-slate-200 rounded-lg" />
                  <div className="flex-1 space-y-2">
                    <div className="h-3 bg-slate-200 rounded w-1/3" />
                    <div className="h-4 bg-slate-200 rounded w-3/4" />
                    <div className="h-3 bg-slate-200 rounded w-1/2" />
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {error && (
          <div className="text-center py-12 text-red-500">
            <p className="text-lg font-medium">No se pudieron cargar los descuentos</p>
            <p className="text-sm mt-1">{error}</p>
          </div>
        )}

        {!loading && !error && discounts.length === 0 && (
          <div className="text-center py-16 text-slate-400">
            <p className="text-5xl mb-4">🔍</p>
            <p className="text-lg font-medium">No hay descuentos con esos filtros</p>
            <p className="text-sm mt-1">Probá cambiando los filtros</p>
          </div>
        )}

        {!loading && !error && discounts.length > 0 && (
          <>
            <p className="text-sm text-slate-500 mb-4">{discounts.length} descuentos encontrados</p>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {discounts.map(d => <DiscountCard key={d.id} discount={d} />)}
            </div>
          </>
        )}
      </main>
    </div>
  )
}
