import { useState, useEffect } from 'react'

const NEVER_KEY    = 'install-never-show'
const SESSION_KEY  = 'install-skipped'

function isIOS() {
  return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream
}

function isStandalone() {
  return window.matchMedia('(display-mode: standalone)').matches
    || window.navigator.standalone === true
}

export default function InstallPrompt() {
  const [deferredPrompt, setDeferredPrompt] = useState(null)
  const [visible, setVisible]               = useState(false)
  const [ios, setIos]                       = useState(false)
  const [imgOk, setImgOk]                   = useState(true)

  useEffect(() => {
    // No mostrar si: ya instalada, marcada como "nunca", o saltada esta sesión
    if (isStandalone())                          return
    if (localStorage.getItem(NEVER_KEY))         return
    if (sessionStorage.getItem(SESSION_KEY))     return

    const iosDevice = isIOS()
    setIos(iosDevice)

    if (iosDevice) {
      const t = setTimeout(() => setVisible(true), 5000)
      return () => clearTimeout(t)
    }

    const handler = e => {
      e.preventDefault()
      setDeferredPrompt(e)
      const t = setTimeout(() => setVisible(true), 4000)
      return () => clearTimeout(t)
    }

    window.addEventListener('beforeinstallprompt', handler)
    window.addEventListener('appinstalled', () => setVisible(false))
    return () => window.removeEventListener('beforeinstallprompt', handler)
  }, [])

  // Instalar (Android/Chrome)
  async function handleInstall() {
    if (!deferredPrompt) return
    deferredPrompt.prompt()
    const { outcome } = await deferredPrompt.userChoice
    setDeferredPrompt(null)
    setVisible(false)
  }

  // Omitir — no mostrar en esta sesión, sí en la próxima visita
  function handleSkip() {
    sessionStorage.setItem(SESSION_KEY, '1')
    setVisible(false)
  }

  // No volver a mostrar — nunca más
  function handleNever() {
    localStorage.setItem(NEVER_KEY, '1')
    setVisible(false)
  }

  if (!visible) return null

  return (
    <>
      {/* Overlay — solo en mobile para el bottom sheet */}
      <div
        className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm sm:hidden"
        onClick={handleSkip}
      />

      {/*
        MOBILE  : bottom sheet sube desde abajo (ancho completo)
        DESKTOP : tarjeta flotante en la esquina inferior derecha
      */}
      <div className={[
        'fixed z-50 bg-slate-900 border border-slate-700 shadow-2xl shadow-violet-500/10',
        // Mobile: bottom sheet
        'bottom-0 left-0 right-0 rounded-t-3xl',
        // Desktop: tarjeta esquina inferior derecha
        'sm:bottom-6 sm:right-6 sm:left-auto sm:rounded-2xl sm:w-[340px]',
      ].join(' ')}
        style={{ animation: 'prompt-in 0.4s cubic-bezier(0.34,1.56,0.64,1) forwards' }}
      >
        {/* Handle — solo mobile */}
        <div className="w-10 h-1 bg-slate-700 rounded-full mx-auto mt-4 sm:hidden" />

        <div className="px-6 pt-5 pb-6 sm:px-5 sm:pt-5 sm:pb-5">

          {/* Header: ícono + textos */}
          <div className="flex items-center gap-4 mb-5">
            {imgOk ? (
              <img
                src="/app.png"
                alt="Ahorro Inteligente"
                onError={() => setImgOk(false)}
                className="w-14 h-14 rounded-2xl border border-slate-700 object-cover shadow-lg flex-shrink-0"
              />
            ) : (
              <div className="w-14 h-14 rounded-2xl bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center flex-shrink-0 shadow-lg">
                <span className="text-white font-black text-lg">AI</span>
              </div>
            )}
            <div>
              <p className="text-slate-500 text-xs font-medium uppercase tracking-wide mb-0.5">
                Aplicación disponible
              </p>
              <h2 className="text-white font-bold text-base leading-snug">
                Ahorro Inteligente (AI)
              </h2>
              <p className="text-slate-400 text-sm mt-0.5">
                Todos tus descuentos, siempre a mano
              </p>
            </div>
          </div>

          {/* Beneficios */}
          <div className="flex items-center gap-4 mb-5 py-3 bg-slate-800/50 rounded-xl px-3">
            <div className="text-center flex-1">
              <p className="text-lg">⚡</p>
              <p className="text-slate-400 text-[10px] mt-0.5 leading-tight">Acceso<br/>instantáneo</p>
            </div>
            <div className="w-px h-8 bg-slate-700" />
            <div className="text-center flex-1">
              <p className="text-lg">🔔</p>
              <p className="text-slate-400 text-[10px] mt-0.5 leading-tight">Nuevas<br/>promos</p>
            </div>
            <div className="w-px h-8 bg-slate-700" />
            <div className="text-center flex-1">
              <p className="text-lg">📴</p>
              <p className="text-slate-400 text-[10px] mt-0.5 leading-tight">Sin<br/>internet</p>
            </div>
          </div>

          {ios ? (
            /* iOS: instrucciones manuales */
            <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-3.5 mb-4 space-y-2">
              {[
                { n: 1, text: <>Tocá <strong className="text-slate-300">Compartir</strong> ⬆️ en Safari</> },
                { n: 2, text: <>Elegí <strong className="text-slate-300">"Agregar a inicio"</strong></> },
                { n: 3, text: <>Tocá <strong className="text-slate-300">"Agregar"</strong> — ¡listo!</> },
              ].map(({ n, text }) => (
                <div key={n} className="flex items-center gap-2.5">
                  <span className="w-5 h-5 rounded-full bg-violet-600/30 text-violet-400 text-[10px] font-bold flex items-center justify-center flex-shrink-0">
                    {n}
                  </span>
                  <span className="text-slate-400 text-sm">{text}</span>
                </div>
              ))}
            </div>
          ) : (
            /* Android / Chrome: botón nativo */
            <button
              onClick={handleInstall}
              className="w-full py-3.5 rounded-xl bg-violet-600 hover:bg-violet-500 active:bg-violet-700 text-white font-bold text-sm transition-all shadow-lg shadow-violet-500/25 mb-3"
            >
              Instalar app
            </button>
          )}

          {/* Omitir */}
          <button
            onClick={handleSkip}
            className="w-full py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-medium transition-all mb-2"
          >
            Omitir
          </button>

          {/* No volver a mostrar */}
          <button
            onClick={handleNever}
            className="w-full py-1.5 text-slate-600 text-xs hover:text-slate-400 transition-colors"
          >
            No volver a mostrar
          </button>
        </div>
      </div>
    </>
  )
}
