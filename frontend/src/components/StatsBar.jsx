import { useStats } from '../hooks/useDiscounts'

export default function StatsBar({ onClose }) {
  const stats = useStats()

  return (
    <div className="relative flex items-center justify-center gap-3 mb-6 bg-violet-500/5 border border-violet-500/20 rounded-2xl px-6 py-5 pr-10">
      <span className="text-3xl select-none">🎯</span>
      <p className="text-slate-300 text-sm md:text-base text-center leading-relaxed">
        Ya llevamos registrados{' '}
        <span className="text-violet-400 font-bold text-xl md:text-2xl">
          {stats ? stats.total.toLocaleString('es-AR') : '…'}
        </span>{' '}
        descuentos que te pueden ayudar a ahorrar más cada día
      </p>

      {/* Botón cerrar */}
      {onClose && (
        <button
          onClick={onClose}
          aria-label="Cerrar"
          className="absolute right-3 top-1/2 -translate-y-1/2 w-6 h-6 flex items-center justify-center rounded-full text-slate-600 hover:text-slate-300 hover:bg-slate-800 transition-all"
        >
          <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2.5} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      )}
    </div>
  )
}
