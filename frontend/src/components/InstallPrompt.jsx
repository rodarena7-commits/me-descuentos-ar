import { useState, useEffect } from 'react'

const DISMISSED_KEY = 'install-prompt-dismissed'

function isIOS() {
  return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream
}

function isInStandaloneMode() {
  return window.matchMedia('(display-mode: standalone)').matches
    || window.navigator.standalone === true
}

export default function InstallPrompt() {
  const [deferredPrompt, setDeferredPrompt] = useState(null)
  const [show, setShow] = useState(false)
  const [ios, setIos] = useState(false)
  const [imgOk, setImgOk] = useState(true)

  useEffect(() => {
    // No mostrar si ya está instalada o fue descartada
    if (isInStandaloneMode()) return
    if (localStorage.getItem(DISMISSED_KEY)) return

    const iosDevice = isIOS()
    setIos(iosDevice)

    if (iosDevice) {
      // En iOS no hay beforeinstallprompt; mostrar instrucciones manuales
      const t = setTimeout(() => setShow(true), 5000)
      return () => clearTimeout(t)
    }

    const handler = e => {
      e.preventDefault()
      setDeferredPrompt(e)
      const t = setTimeout(() => setShow(true), 4000)
      return () => clearTimeout(t)
    }

    window.addEventListener('beforeinstallprompt', handler)
    window.addEventListener('appinstalled', () => setShow(false))
    return () => window.removeEventListener('beforeinstallprompt', handler)
  }, [])

  function dismiss() {
    localStorage.setItem(DISMISSED_KEY, '1')
    setShow(false)
  }

  async function install() {
    if (!deferredPrompt) return
    deferredPrompt.prompt()
    const { outcome } = await deferredPrompt.userChoice
    if (outcome === 'accepted') setShow(false)
    setDeferredPrompt(null)
  }

  if (!show) return null

  return (
    <>
      {/* Overlay semi-transparente */}
      <div
        className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm"
        onClick={dismiss}
      />

      {/* Bottom sheet */}
      <div
        className="fixed bottom-0 left-0 right-0 z-50 animate-[slide-up_0.4s_cubic-bezier(0.34,1.56,0.64,1)_forwards]"
        style={{ animation: 'slide-up 0.4s cubic-bezier(0.34,1.56,0.64,1) forwards' }}
      >
        <div className="bg-slate-900 border border-slate-700 border-b-0 rounded-t-3xl px-6 pt-5 pb-8 mx-auto max-w-lg shadow-2xl shadow-violet-500/20">

          {/* Handle bar */}
          <div className="w-10 h-1 bg-slate-700 rounded-full mx-auto mb-6" />

          {/* Header con ícono y texto */}
          <div className="flex items-center gap-4 mb-5">
            {imgOk ? (
              <img
                src="/app.png"
                alt="Ahorro Inteligente"
                onError={() => setImgOk(false)}
                className="w-16 h-16 rounded-2xl border border-slate-700 flex-shrink-0 object-cover shadow-lg"
              />
            ) : (
              <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center flex-shrink-0 shadow-lg">
                <span className="text-white font-black text-lg">AI</span>
              </div>
            )}
            <div>
              <h2 className="text-white font-bold text-lg leading-tight">
                Instalá Ahorro Inteligente
              </h2>
              <p className="text-slate-400 text-sm mt-0.5">
                Accedé rápido a todos tus descuentos
              </p>
            </div>
          </div>

          {/* Beneficios */}
          <div className="space-y-2.5 mb-6">
            {[
              { icon: '⚡', text: 'Abre al instante, sin abrir el browser' },
              { icon: '🔔', text: 'Notificaciones de nuevas promos' },
              { icon: '📴', text: 'Funciona incluso sin conexión' },
            ].map(({ icon, text }) => (
              <div key={text} className="flex items-center gap-3">
                <span className="text-lg">{icon}</span>
                <span className="text-slate-300 text-sm">{text}</span>
              </div>
            ))}
          </div>

          {ios ? (
            /* Instrucciones para iOS */
            <div className="bg-slate-800/60 border border-slate-700 rounded-2xl p-4 mb-4">
              <p className="text-slate-300 text-sm font-medium mb-2">
                Para instalar en iPhone / iPad:
              </p>
              <ol className="text-slate-400 text-sm space-y-1.5 list-none">
                <li className="flex items-start gap-2">
                  <span className="text-violet-400 font-bold mt-0.5">1.</span>
                  <span>Tocá el botón <strong className="text-slate-300">Compartir</strong> <span className="inline-block">⬆️</span> en Safari</span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-violet-400 font-bold mt-0.5">2.</span>
                  <span>Elegí <strong className="text-slate-300">"Agregar a pantalla de inicio"</strong></span>
                </li>
                <li className="flex items-start gap-2">
                  <span className="text-violet-400 font-bold mt-0.5">3.</span>
                  <span>Tocá <strong className="text-slate-300">"Agregar"</strong> — ¡listo!</span>
                </li>
              </ol>
            </div>
          ) : (
            /* Botón de instalación para Android / Chrome */
            <button
              onClick={install}
              className="w-full py-4 rounded-2xl bg-violet-600 hover:bg-violet-500 active:bg-violet-700 text-white font-bold text-base transition-all shadow-lg shadow-violet-500/30 mb-3"
            >
              Instalar app
            </button>
          )}

          <button
            onClick={dismiss}
            className="w-full py-2.5 text-slate-500 text-sm hover:text-slate-300 transition-colors"
          >
            Ahora no
          </button>
        </div>
      </div>
    </>
  )
}
