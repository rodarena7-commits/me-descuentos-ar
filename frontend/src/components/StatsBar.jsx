import { useStats } from '../hooks/useDiscounts'

const cards = [
  {
    key: 'total',
    label: 'Activos',
    icon: '💳',
    gradient: 'from-violet-600/20 to-violet-600/5',
    border: 'border-violet-500/30',
    text: 'text-violet-400',
  },
  {
    key: 'new_today',
    label: 'Nuevos hoy',
    icon: '🆕',
    gradient: 'from-emerald-600/20 to-emerald-600/5',
    border: 'border-emerald-500/30',
    text: 'text-emerald-400',
  },
  {
    key: 'expiring_soon',
    label: 'Por vencerse',
    icon: '⏰',
    gradient: 'from-amber-600/20 to-amber-600/5',
    border: 'border-amber-500/30',
    text: 'text-amber-400',
  },
]

export default function StatsBar() {
  const stats = useStats()

  return (
    <div className="grid grid-cols-3 gap-3 mb-6">
      {cards.map(({ key, label, icon, gradient, border, text }) => (
        <div
          key={key}
          className={`rounded-xl border ${border} bg-gradient-to-br ${gradient} p-4 text-center backdrop-blur-sm`}
        >
          <div className="text-2xl mb-1">{icon}</div>
          <div className={`text-3xl font-bold ${text}`}>
            {stats ? stats[key] : '—'}
          </div>
          <div className="text-xs text-slate-400 mt-1 font-medium uppercase tracking-wide">
            {label}
          </div>
        </div>
      ))}
    </div>
  )
}
