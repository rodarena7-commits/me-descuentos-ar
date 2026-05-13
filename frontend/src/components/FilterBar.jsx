import { useSources, useCategories } from '../hooks/useDiscounts'

const TYPE_OPTIONS = [
  { value: '', label: 'Todos' },
  { value: 'descuento', label: 'Descuento' },
  { value: 'reintegro', label: 'Reintegro' },
  { value: 'promocion', label: 'Promoción' },
]

const SOURCE_TYPE_OPTIONS = [
  { value: '', label: 'Todos' },
  { value: 'banco', label: 'Bancos' },
  { value: 'fintech', label: 'Fintechs' },
  { value: 'prepaga', label: 'Prepagas' },
]

const QUICK_FILTERS = [
  { key: 'is_new', label: '🆕 Nuevos', value: true },
  { key: 'expiring_soon', label: '⏰ Por vencerse', value: true },
  { key: 'is_limited_stock', label: '⚡ Hasta agotar stock', value: true },
]

export default function FilterBar({ filters, onChange }) {
  const sources = useSources()
  const categories = useCategories()

  function set(key, value) {
    onChange({ ...filters, [key]: value })
  }

  function toggleQuick(key) {
    set(key, filters[key] ? null : true)
  }

  return (
    <div className="bg-white rounded-xl border border-slate-200 p-4 mb-6 space-y-4">
      <div className="flex flex-wrap gap-2">
        {QUICK_FILTERS.map(({ key, label }) => (
          <button
            key={key}
            onClick={() => toggleQuick(key)}
            className={`px-3 py-1.5 rounded-full text-sm font-medium border transition-all ${
              filters[key]
                ? 'bg-indigo-600 text-white border-indigo-600'
                : 'bg-white text-slate-600 border-slate-300 hover:border-indigo-400'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        <select
          className="border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 bg-white"
          value={filters.discount_type || ''}
          onChange={e => set('discount_type', e.target.value)}
        >
          <option value="" disabled>Tipo</option>
          {TYPE_OPTIONS.map(o => <option key={o.value} value={o.value}>{o.label}</option>)}
        </select>

        <select
          className="border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 bg-white"
          value={filters.source_type || ''}
          onChange={e => set('source_type', e.target.value)}
        >
          <option value="" disabled>Entidad</option>
          {SOURCE_TYPE_OPTIONS.map(o => <option key={o.value} value={o.value}>{o.label}</option>)}
        </select>

        <select
          className="border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 bg-white"
          value={filters.source || ''}
          onChange={e => set('source', e.target.value)}
        >
          <option value="">Todos los emisores</option>
          {sources.map(s => <option key={s.source} value={s.source}>{s.source}</option>)}
        </select>

        <select
          className="border border-slate-200 rounded-lg px-3 py-2 text-sm text-slate-700 bg-white"
          value={filters.category || ''}
          onChange={e => set('category', e.target.value)}
        >
          <option value="">Todas las categorías</option>
          {categories.map(c => <option key={c} value={c} className="capitalize">{c}</option>)}
        </select>
      </div>
    </div>
  )
}
