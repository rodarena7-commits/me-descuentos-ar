import { useSources, useCategories } from '../hooks/useDiscounts'

const TYPE_OPTIONS = [
  { value: '', label: 'Todos los tipos' },
  { value: 'descuento', label: 'Descuento' },
  { value: 'reintegro', label: 'Reintegro' },
  { value: 'promocion', label: 'Promoción' },
]

const SOURCE_TYPE_OPTIONS = [
  { value: '', label: 'Todas las entidades' },
  { value: 'banco', label: 'Bancos' },
  { value: 'fintech', label: 'Fintechs' },
  { value: 'prepaga', label: 'Prepagas' },
]

const DAY_OPTIONS = [
  { value: '', label: 'Todos los días' },
  { value: 'lunes', label: 'Lunes' },
  { value: 'martes', label: 'Martes' },
  { value: 'miercoles', label: 'Miércoles' },
  { value: 'jueves', label: 'Jueves' },
  { value: 'viernes', label: 'Viernes' },
  { value: 'sabado', label: 'Sábado' },
  { value: 'domingo', label: 'Domingo' },
]

const QUICK_FILTERS = [
  { key: 'is_new', label: '🆕 Nuevos', activeColor: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/50' },
  { key: 'expiring_soon', label: '⏰ Por vencerse', activeColor: 'bg-amber-500/20 text-amber-400 border-amber-500/50' },
  { key: 'is_limited_stock', label: '⚡ Stock limitado', activeColor: 'bg-red-500/20 text-red-400 border-red-500/50' },
]

const selectClass =
  'bg-slate-800/80 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-300 w-full focus:outline-none focus:border-violet-500 transition-colors'

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
    <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 mb-6 space-y-4 backdrop-blur-sm">
      <div className="flex flex-wrap gap-2">
        {QUICK_FILTERS.map(({ key, label, activeColor }) => (
          <button
            key={key}
            onClick={() => toggleQuick(key)}
            className={`px-4 py-1.5 rounded-full text-sm font-medium border transition-all cursor-pointer ${
              filters[key]
                ? activeColor
                : 'bg-slate-800/50 text-slate-400 border-slate-700 hover:border-slate-500 hover:text-slate-300'
            }`}
          >
            {label}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3">
        <select className={selectClass} value={filters.discount_type || ''} onChange={e => set('discount_type', e.target.value)}>
          {TYPE_OPTIONS.map(o => <option key={o.value} value={o.value} className="bg-slate-800">{o.label}</option>)}
        </select>

        <select className={selectClass} value={filters.source_type || ''} onChange={e => set('source_type', e.target.value)}>
          {SOURCE_TYPE_OPTIONS.map(o => <option key={o.value} value={o.value} className="bg-slate-800">{o.label}</option>)}
        </select>

        <select className={selectClass} value={filters.source || ''} onChange={e => set('source', e.target.value)}>
          <option value="" className="bg-slate-800">Todos los emisores</option>
          {sources.map(s => <option key={s.source} value={s.source} className="bg-slate-800">{s.source}</option>)}
        </select>

        <select className={selectClass} value={filters.category || ''} onChange={e => set('category', e.target.value)}>
          <option value="" className="bg-slate-800">Todas las categorías</option>
          {categories.map(c => <option key={c} value={c} className="bg-slate-800 capitalize">{c}</option>)}
        </select>

        <select className={selectClass} value={filters.day || ''} onChange={e => set('day', e.target.value)}>
          {DAY_OPTIONS.map(o => <option key={o.value} value={o.value} className="bg-slate-800">{o.label}</option>)}
        </select>
      </div>
    </div>
  )
}
