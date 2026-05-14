import { useStats } from '../hooks/useDiscounts'

export default function StatsBar() {
  const stats = useStats()

  return (
    <div className="flex items-center justify-center gap-3 mb-6 bg-violet-500/5 border border-violet-500/20 rounded-2xl px-6 py-5">
      <span className="text-3xl select-none">🎯</span>
      <p className="text-slate-300 text-sm md:text-base text-center leading-relaxed">
        Ya llevamos registrados{' '}
        <span className="text-violet-400 font-bold text-xl md:text-2xl">
          {stats ? stats.total.toLocaleString('es-AR') : '…'}
        </span>{' '}
        descuentos que te pueden ayudar a ahorrar más cada día
      </p>
    </div>
  )
}
