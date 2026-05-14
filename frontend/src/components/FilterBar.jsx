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

const PERCENTAGE_OPTIONS = [
  { value: '', label: '% Cualquiera' },
  { value: '10', label: '10% o más' },
  { value: '15', label: '15% o más' },
  { value: '20', label: '20% o más' },
  { value: '25', label: '25% o más' },
  { value: '30', label: '30% o más' },
  { value: '40', label: '40% o más' },
  { value: '50', label: '50% o más' },
]

const QUICK_FILTERS = [
  { key: 'is_new', label: '🆕 Nuevos', activeColor: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/50' },
  { key: 'expiring_soon', label: '⏰ Por vencerse', activeColor: 'bg-amber-500/20 text-amber-400 border-amber-500/50' },
]

const selectClass =
  'bg-slate-800/80 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-300 w-full focus:outline-none focus:border-violet-500 transition-colors'

export default function FilterBar({ filters, onChange }) {
  const sources = useSources()

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

      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
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
          <option value="supermercados" className="bg-slate-800">Supermercados</option>
          <option value="combustible" className="bg-slate-800">Combustible</option>
          <option value="gastronomia" className="bg-slate-800">Gastronomía</option>
          <option value="farmacias" className="bg-slate-800">Farmacias</option>
          <option value="transporte" className="bg-slate-800">Transporte</option>
          <option value="indumentaria" className="bg-slate-800">Indumentaria</option>
          <option value="electronica" className="bg-slate-800">Electrónica</option>
          <option value="entretenimiento" className="bg-slate-800">Entretenimiento</option>
          <option value="viajes" className="bg-slate-800">Viajes</option>
          <option value="librerias" className="bg-slate-800">Librerías</option>
          <option value="servicios" className="bg-slate-800">Servicios públicos</option>
          <option value="educacion" className="bg-slate-800">Educación</option>
          <option value="hogar" className="bg-slate-800">Hogar</option>
          <option value="neumaticos" className="bg-slate-800">Neumáticos</option>
          <option value="varios" className="bg-slate-800">Varios</option>
        </select>

        <select className={selectClass} value={filters.day || ''} onChange={e => set('day', e.target.value)}>
          {DAY_OPTIONS.map(o => <option key={o.value} value={o.value} className="bg-slate-800">{o.label}</option>)}
        </select>

        <select className={selectClass} value={filters.min_percentage || ''} onChange={e => set('min_percentage', e.target.value)}>
          {PERCENTAGE_OPTIONS.map(o => <option key={o.value} value={o.value} className="bg-slate-800">{o.label}</option>)}
        </select>
      </div>
    </div>
  )
}
