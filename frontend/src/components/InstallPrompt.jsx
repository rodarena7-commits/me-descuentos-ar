import { useState, useEffect, useRef } from 'react'

const FIRST_VISIT_KEY = 'app-install-shown'   // se marca en la primera visita
const NEVER_KEY       = 'install-never-show'   // el usuario dijo "no mostrar más"
const SESSION_KEY     = 'install-skipped'      // omitido esta sesión

function isIOS() {
  return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream
}
function isStandalone() {
  return window.matchMedia('(display-mode: standalone)').matches
    || window.navigator.standalone === true
}

export default function InstallPrompt() {
  const [visible, setVisible] = useState(false)
  const [prompt, setPrompt]   = useState(null)    // deferredPrompt nativo de Chrome
  const [ios, setIos]         = useState(false)
  const timerRef              = useRef(null)

  useEffect(() => {
    if (isStandalone()) return   // ya está instalada como app

    const iosDevice = isIOS()
    setIos(iosDevice)

    // ── Captura el prompt nativo si Chrome lo ofrece ─────────────────────────
    const onBeforeInstall = e => {
      e.preventDefault()
      setPrompt(e)
      window.__pwaPrompt = e
    }
    window.addEventListener('beforeinstallprompt', onBeforeInstall)
    window.addEventListener('appinstalled', () => {
      setVisible(false)
      setPrompt(null)
    })

    // ── Trigger manual desde el menú de perfil ───────────────────────────────
    const onManual = () => {
      localStorage.removeItem(NEVER_KEY)
      sessionStorage.removeItem(SESSION_KEY)
      setVisible(true)
    }
    window.addEventListener('show-install-prompt', onManual)

    // ── Mostrar automáticamente ──────────────────────────────────────────────
    const neverShow   = localStorage.getItem(NEVER_KEY)
    const sessionSkip = sessionStorage.getItem(SESSION_KEY)

    if (!neverShow && !sessionSkip) {
      const firstVisit = !localStorage.getItem(FIRST_VISIT_KEY)
      if (firstVisit) {
        // Primera vez que entra: guardar marca y mostrar a los 4 segundos
        localStorage.setItem(FIRST_VISIT_KEY, '1')
        timerRef.current = setTimeout(() => setVisible(true), 4000)
      }
    }

    return () => {
      clearTimeout(timerRef.current)
      window.removeEventListener('beforeinstallprompt', onBeforeInstall)
      window.removeEventListener('appinstalled', () => {})
      window.removeEventListener('show-install-prompt', onManual)
    }
  }, [])

  // ── Acciones ─────────────────────────────────────────────────────────────
  async function handleInstall() {
    if (prompt) {
      await prompt.prompt()
      const { outcome } = await prompt.userChoice
      if (outcome === 'accepted') {
        setVisible(false)
        setPrompt(null)
        window.__pwaPrompt = null
      }
    }
  }

  function handleSkip() {
    sessionStorage.setItem(SESSION_KEY, '1')
    setVisible(false)
  }

  function handleNever() {
    localStorage.setItem(NEVER_KEY, '1')
    setVisible(false)
  }

  if (!visible) return null

  return (
    <>
      {/* Overlay en mobile */}
      <div
        className="fixed inset-0 z-50 bg-black/50 backdrop-blur-sm sm:hidden"
        onClick={handleSkip}
      />

      {/* Mobile: bottom sheet │ Desktop: tarjeta esquina inferior derecha */}
      <div
        className="fixed z-50 bg-slate-900 border border-slate-700 shadow-2xl shadow-violet-500/15
                   bottom-0 left-0 right-0 rounded-t-3xl
                   sm:bottom-6 sm:right-6 sm:left-auto sm:rounded-2xl sm:w-[360px]"
        style={{ animation: 'prompt-in 0.4s cubic-bezier(0.34,1.56,0.64,1) forwards' }}
      >
        {/* Handle mobile */}
        <div className="w-10 h-1 bg-slate-700 rounded-full mx-auto mt-4 mb-1 sm:hidden" />

        <div className="px-6 pt-5 pb-7 sm:px-5 sm:pt-5 sm:pb-5">

          {/* Header */}
          <div className="flex items-start gap-4 mb-5">
            <img
              src="/app.png"
              alt="Ahorro Inteligente"
              className="w-16 h-16 rounded-2xl border border-slate-700 object-cover shadow-lg flex-shrink-0"
            />
            <div className="pt-0.5">
              <p className="text-violet-400 text-[11px] font-semibold uppercase tracking-widest mb-0.5">
                Aplicación disponible
              </p>
              <h2 className="text-white font-bold text-lg leading-tight">
                Ahorro Inteligente
              </h2>
              <p className="text-slate-400 text-sm mt-0.5">
                Todos tus descuentos, siempre a mano
              </p>
            </div>
          </div>

          {/* Beneficios */}
          <div className="grid grid-cols-3 gap-2 mb-5">
            {[
              { icon: '⚡', text: 'Acceso instantáneo' },
              { icon: '🔔', text: 'Nuevas promos' },
              { icon: '📴', text: 'Sin internet' },
            ].map(({ icon, text }) => (
              <div key={text} className="bg-slate-800/60 rounded-xl py-3 px-2 text-center border border-slate-700/50">
                <p className="text-xl mb-1">{icon}</p>
                <p className="text-slate-400 text-[10px] leading-tight">{text}</p>
              </div>
            ))}
          </div>

          {/* ── Android / Chrome con prompt nativo ── */}
          {!ios && prompt && (
            <button
              onClick={handleInstall}
              className="w-full py-3.5 rounded-2xl bg-violet-600 hover:bg-violet-500 active:bg-violet-700 text-white font-bold text-base transition-all shadow-lg shadow-violet-500/30 mb-3"
            >
              Instalar app
            </button>
          )}

          {/* ── Android / Chrome sin prompt nativo (instrucciones) ── */}
          {!ios && !prompt && (
            <div className="bg-slate-800/50 border border-slate-700 rounded-2xl p-4 mb-4">
              <p className="text-slate-300 text-sm font-semibold mb-2">
                Cómo instalar en Android:
              </p>
              <div className="space-y-2">
                {[
                  <>Tocá el menú <strong className="text-slate-200">⋮</strong> de Chrome</>,
                  <>Elegí <strong className="text-slate-200">"Agregar a pantalla de inicio"</strong></>,
                  <>Confirmá tocando <strong className="text-slate-200">"Agregar"</strong></>,
                ].map((step, i) => (
                  <div key={i} className="flex items-center gap-2.5">
                    <span className="w-5 h-5 rounded-full bg-violet-600/30 text-violet-400 text-[10px] font-bold flex items-center justify-center flex-shrink-0">
                      {i + 1}
                    </span>
                    <span className="text-slate-400 text-sm">{step}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* ── iOS / Safari ── */}
          {ios && (
            <div className="bg-slate-800/50 border border-slate-700 rounded-2xl p-4 mb-4">
              <p className="text-slate-300 text-sm font-semibold mb-2">
                Cómo instalar en iPhone / iPad:
              </p>
              <div className="space-y-2">
                {[
                  <>Tocá <strong className="text-slate-200">Compartir ⬆️</strong> en Safari</>,
                  <>Elegí <strong className="text-slate-200">"Agregar a inicio"</strong></>,
                  <>Tocá <strong className="text-slate-200">"Agregar"</strong> — ¡listo!</>,
                ].map((step, i) => (
                  <div key={i} className="flex items-center gap-2.5">
                    <span className="w-5 h-5 rounded-full bg-violet-600/30 text-violet-400 text-[10px] font-bold flex items-center justify-center flex-shrink-0">
                      {i + 1}
                    </span>
                    <span className="text-slate-400 text-sm">{step}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Omitir */}
          <button
            onClick={handleSkip}
            className="w-full py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-sm font-semibold transition-all mb-2 border border-slate-700"
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
