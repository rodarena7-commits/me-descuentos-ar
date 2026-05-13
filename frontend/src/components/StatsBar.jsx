import { useStats } from '../hooks/useDiscounts'

const cards = [
  { key: 'total', label: 'Descuentos activos', color: 'bg-blue-50 text-blue-700 border-blue-200' },
  { key: 'new_today', label: 'Nuevos hoy', color: 'bg-green-50 text-green-700 border-green-200' },
  { key: 'expiring_soon', label: 'Por vencerse', color: 'bg-amber-50 text-amber-700 border-amber-200' },
  { key: 'limited_stock', label: 'Hasta agotar stock', color: 'bg-red-50 text-red-700 border-red-200' },
]

export default function StatsBar() {
  const stats = useStats()

  return (
    <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
      {cards.map(({ key, label, color }) => (
        <div key={key} className={`rounded-xl border p-4 text-center ${color}`}>
          <div className="text-3xl font-bold">
            {stats ? stats[key] : '—'}
          </div>
          <div className="text-sm mt-1 font-medium">{label}</div>
        </div>
      ))}
    </div>
  )
}
