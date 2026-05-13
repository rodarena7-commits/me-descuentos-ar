import { useState, useMemo, useEffect } from 'react'
import { Navigate } from 'react-router-dom'
import StatsBar from './components/StatsBar'
import FilterBar from './components/FilterBar'
import DiscountCard from './components/DiscountCard'
import UserMenu from './components/UserMenu'
import OnlineCounter from './components/OnlineCounter'
import { useDiscounts } from './hooks/useDiscounts'
import { usePresence } from './hooks/usePresence'
import { useAuth } from './contexts/AuthContext'
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
  const ITEMS_PER_PAGE = 12

  const { user, loading } = useAuth()
  const [filters, setFilters] = useState({})
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(1)
  const { discounts, loading: discLoading, error } = useDiscounts(filters)
  const onlineCount = usePresence()

  // Client-side search filter
  const filtered = useMemo(() => {
    if (!search.trim()) return discounts
    const q = search.toLowerCase()
    return discounts.filter(d =>
      [d.title, d.description, d.source, d.category]
        .some(f => f?.toLowerCase().includes(q))
    )
  }, [discounts, search])

  // Reset page when filters or search change
  useEffect(() => { setPage(1) }, [filters, search])

  const totalPages = Math.ceil(filtered.length / ITEMS_PER_PAGE)
  const paginated = filtered.slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE)

  if (loading) {
    return (
      <div className="min-h-screen bg-[#020617] flex items-center justify-center">
        <div className="w-8 h-8 rounded-xl bg-gradient-to-br from-violet-600 to-indigo-700 animate-pulse" />
      </div>
    )
  }

  if (!user) return <Navigate to="/login" replace />

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
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 text-xs text-slate-500">
              <span className="w-2 h-2 rounded-full bg-emerald-500 inline-block animate-pulse" />
              <span className="hidden sm:inline">En vivo</span>
            </div>
            <UserMenu />
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8">
        {/* Hero + Search */}
        <div className="mb-8 text-center">
          <h1 className="text-3xl md:text-4xl font-bold text-white mb-2">
            Ahorro Inteligente{' '}
            <span className="text-violet-400">— AI</span>
          </h1>
          <p className="text-slate-400 text-sm md:text-base mb-6">
            Todos los descuentos, promos y reintegros de bancos y billeteras de Argentina
          </p>

          {/* Search bar */}
          <div className="relative max-w-xl mx-auto">
            <div className="absolute inset-y-0 left-4 flex items-center pointer-events-none">
              <svg className="w-4 h-4 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                  d="M21 21l-4.35-4.35M17 11A6 6 0 1 1 5 11a6 6 0 0 1 12 0z" />
              </svg>
            </div>
            <input
              type="text"
              value={search}
              onChange={e => setSearch(e.target.value)}
              placeholder="¿Qué descuento estás buscando?"
              className="w-full bg-slate-900/80 border border-slate-700 rounded-2xl pl-11 pr-4 py-3.5 text-slate-200 text-sm placeholder-slate-500 focus:outline-none focus:border-violet-500 focus:ring-1 focus:ring-violet-500/30 transition-all backdrop-blur-sm"
            />
            {search && (
              <button
                onClick={() => setSearch('')}
                className="absolute inset-y-0 right-4 flex items-center text-slate-500 hover:text-slate-300 transition-colors"
              >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            )}
          </div>
        </div>

        <StatsBar />
        <FilterBar filters={filters} onChange={setFilters} />

        {discLoading && (
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

        {!discLoading && !error && filtered.length === 0 && (
          <div className="text-center py-16">
            <p className="text-5xl mb-4">🔍</p>
            <p className="text-slate-300 font-medium">
              {search ? `Sin resultados para "${search}"` : 'No hay descuentos con esos filtros'}
            </p>
            <p className="text-slate-500 text-sm mt-1">Probá con otro término o cambiá los filtros</p>
          </div>
        )}

        {!discLoading && !error && filtered.length > 0 && (
          <>
            <div className="flex items-center justify-between mb-4">
              <p className="text-xs text-slate-600 uppercase tracking-wide">
                {filtered.length} descuentos · página {page} de {totalPages}
              </p>
              {totalPages > 1 && (
                <p className="text-xs text-slate-600">
                  Mostrando {(page - 1) * ITEMS_PER_PAGE + 1}–{Math.min(page * ITEMS_PER_PAGE, filtered.length)}
                </p>
              )}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {paginated.map(d => <DiscountCard key={d.id} discount={d} />)}
            </div>

            {/* Paginación */}
            {totalPages > 1 && (
              <div className="flex items-center justify-center gap-2 mt-8">
                <button
                  onClick={() => { setPage(p => Math.max(1, p - 1)); window.scrollTo({ top: 0, behavior: 'smooth' }) }}
                  disabled={page === 1}
                  className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 text-sm font-medium hover:bg-slate-700 hover:border-slate-600 disabled:opacity-30 disabled:cursor-not-allowed transition-all"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                  </svg>
                  Anterior
                </button>

                <div className="flex items-center gap-1">
                  {Array.from({ length: totalPages }, (_, i) => i + 1)
                    .filter(p => p === 1 || p === totalPages || Math.abs(p - page) <= 1)
                    .reduce((acc, p, idx, arr) => {
                      if (idx > 0 && p - arr[idx - 1] > 1) acc.push('…')
                      acc.push(p)
                      return acc
                    }, [])
                    .map((p, i) =>
                      p === '…' ? (
                        <span key={`gap-${i}`} className="w-8 text-center text-slate-600 text-sm">…</span>
                      ) : (
                        <button
                          key={p}
                          onClick={() => { setPage(p); window.scrollTo({ top: 0, behavior: 'smooth' }) }}
                          className={`w-9 h-9 rounded-xl text-sm font-medium transition-all ${
                            p === page
                              ? 'bg-violet-600 text-white border border-violet-500'
                              : 'bg-slate-800/80 border border-slate-700 text-slate-400 hover:bg-slate-700 hover:text-slate-200'
                          }`}
                        >
                          {p}
                        </button>
                      )
                    )
                  }
                </div>

                <button
                  onClick={() => { setPage(p => Math.min(totalPages, p + 1)); window.scrollTo({ top: 0, behavior: 'smooth' }) }}
                  disabled={page === totalPages}
                  className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 text-sm font-medium hover:bg-slate-700 hover:border-slate-600 disabled:opacity-30 disabled:cursor-not-allowed transition-all"
                >
                  Siguiente
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </button>
              </div>
            )}
          </>
        )}
      </main>

      <OnlineCounter count={onlineCount} />

      <footer className="border-t border-slate-800/50 mt-16 py-8">
        <div className="max-w-6xl mx-auto px-4 text-center space-y-2">
          <p className="text-xs text-slate-500">
            Los datos son informativos. Verificá condiciones vigentes en el sitio oficial de cada entidad antes de realizar una compra.
          </p>
          <p className="text-xs text-slate-600">
            © {new Date().getFullYear()} <span className="text-slate-500 font-medium">Ahorro Inteligente (AI)</span> — Todos los derechos reservados.
          </p>
          <p className="text-xs text-slate-700">
            Desarrollado por <span className="text-slate-600">Asociación Hermanos Arena</span> · Argentina
          </p>
        </div>
      </footer>
    </div>
  )
}
