import { useState, useEffect } from 'react'

// Mantenimiento: domingos 1:00–7:00 AM Argentina (UTC-3) = 04:00–10:00 UTC
function isMaintenanceWindow() {
  const now = new Date()
  const utcDay = now.getUTCDay()    // 0 = domingo
  const utcHour = now.getUTCHours() // 0-23
  return utcDay === 0 && utcHour >= 4 && utcHour < 10
}

export default function MaintenanceBanner() {
  const [show, setShow] = useState(false)
  const [dots, setDots] = useState(0)

  useEffect(() => {
    setShow(isMaintenanceWindow())
    const check = setInterval(() => setShow(isMaintenanceWindow()), 60_000)
    return () => clearInterval(check)
  }, [])

  // Animación de puntos "buscando..."
  useEffect(() => {
    if (!show) return
    const anim = setInterval(() => setDots(d => (d + 1) % 4), 600)
    return () => clearInterval(anim)
  }, [show])

  if (!show) return null

  const dotsStr = '.'.repeat(dots)

  return (
    <div className="fixed inset-0 z-50 bg-[#020617] flex flex-col items-center justify-center px-6">
      <div className="max-w-md w-full text-center space-y-8">

        {/* Icono animado */}
        <div className="relative mx-auto w-24 h-24">
          <div className="absolute inset-0 rounded-3xl bg-violet-600/20 animate-ping" />
          <div className="relative w-24 h-24 rounded-3xl bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center shadow-2xl shadow-violet-500/40">
            <span className="text-4xl">🔄</span>
          </div>
        </div>

        {/* Texto principal */}
        <div>
          <h1 className="text-2xl md:text-3xl font-bold text-white mb-2">
            Estamos actualizando
          </h1>
          <p className="text-violet-400 font-semibold text-lg">
            Buscando nuevos descuentos para vos{dotsStr}
          </p>
        </div>

        {/* Descripción */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-5 text-left space-y-3">
          <div className="flex items-start gap-3">
            <span className="text-lg mt-0.5">🏦</span>
            <p className="text-slate-300 text-sm">
              Revisando banco por banco, fintech por fintech y exchange crypto por exchange.
            </p>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-lg mt-0.5">✨</span>
            <p className="text-slate-300 text-sm">
              Agregando descuentos nuevos y eliminando los que ya vencieron.
            </p>
          </div>
          <div className="flex items-start gap-3">
            <span className="text-lg mt-0.5">⏰</span>
            <p className="text-slate-300 text-sm">
              Este proceso corre todos los domingos entre la <span className="text-white font-medium">1:00</span> y las <span className="text-white font-medium">7:00 AM</span>.
            </p>
          </div>
        </div>

        {/* Aviso de disculpa */}
        <p className="text-slate-500 text-sm">
          Disculpá las molestias. Volvé después de las{' '}
          <span className="text-slate-300 font-medium">7:00 AM</span>{' '}
          para ver todos los descuentos actualizados.
        </p>

        {/* Barra de progreso animada */}
        <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
          <div className="h-full bg-gradient-to-r from-violet-600 to-indigo-500 rounded-full animate-[shimmer_2s_linear_infinite] w-1/2" />
        </div>

      </div>
    </div>
  )
}
