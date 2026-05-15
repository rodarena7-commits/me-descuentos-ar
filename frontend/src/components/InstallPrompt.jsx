import { useState, useEffect, useRef } from 'react'

const NEVER_KEY   = 'install-never-show'
const SESSION_KEY = 'install-skipped'

function isIOS() {
  return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream
}

function isStandalone() {
  return window.matchMedia('(display-mode: standalone)').matches
    || window.navigator.standalone === true
}

export default function InstallPrompt() {
  const [visible, setVisible]   = useState(false)
  const [prompt, setPrompt]     = useState(null)   // deferredPrompt (Android/Chrome)
  const [ios, setIos]           = useState(false)
  const [imgSrc, setImgSrc]     = useState('/app.png')
  const [imgFailed, setImgFailed] = useState(false)
  const timerRef = useRef(null)

  useEffect(() => {
    // Si ya está instalada como app, nunca mostrar
    if (isStandalone()) return

    const iosDevice = isIOS()
    setIos(iosDevice)

    const shouldAutoShow =
      !localStorage.getItem(NEVER_KEY) &&
      !sessionStorage.getItem(SESSION_KEY)

    // ── Trigger manual desde el menú de perfil ──────────────────────────────
    const onManual = () => {
      localStorage.removeItem(NEVER_KEY)
      sessionStorage.removeItem(SESSION_KEY)
      setVisible(true)
    }
    window.addEventListener('show-install-prompt', onManual)

    // ── iOS: mostrar instrucciones manuales ─────────────────────────────────
    if (iosDevice) {
      if (shouldAutoShow) {
        timerRef.current = setTimeout(() => setVisible(true), 5000)
      }
      return () => {
        clearTimeout(timerRef.current)
        window.removeEventListener('show-install-prompt', onManual)
      }
    }

    // ── Android / Chrome: capturar el evento nativo ─────────────────────────
    const onBeforeInstall = e => {
      e.preventDefault()
      setPrompt(e)
      window.__pwaPrompt = e          // por si UserMenu lo necesita
      if (shouldAutoShow) {
        timerRef.current = setTimeout(() => setVisible(true), 3000)
      }
    }

    const onInstalled = () => {
      clearTimeout(timerRef.current)
      setVisible(false)
      setPrompt(null)
    }

    window.addEventListener('beforeinstallprompt', onBeforeInstall)
    window.addEventListener('appinstalled', onInstalled)

    return () => {
      clearTimeout(timerRef.current)
      window.removeEventListener('beforeinstallprompt', onBeforeInstall)
      window.removeEventListener('appinstalled', onInstalled)
      window.removeEventListener('show-install-prompt', onManual)
    }
  }, [])

  // ── Acciones ───────────────────────────────────────────────────────────────
  async function handleInstall() {
    if (!prompt) return
    await prompt.prompt()
    const { outcome } = await prompt.userChoice
    if (outcome === 'accepted') {
      setVisible(false)
      setPrompt(null)
      window.__pwaPrompt = null
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

  function handleImgError() {
    if (imgSrc === '/app.png') {
      setImgSrc('/favicon.svg')
    } else {
      setImgFailed(true)
    }
  }

  if (!visible) return null

  return (
    <>
      {/* Overlay solo en mobile */}
      <div
        className="fixed inset-0 z-50 bg-black/40 backdrop-blur-sm sm:hidden"
        onClick={handleSkip}
      />

      {/*
        Mobile  → bottom sheet ancho completo, sube desde abajo
        Desktop → tarjeta 340px, esquina inferior derecha
      */}
      <div
        className="fixed z-50 bg-slate-900 border border-slate-700 shadow-2xl shadow-violet-500/10
          bottom-0 left-0 right-0 rounded-t-3xl
          sm:bottom-6 sm:right-6 sm:left-auto sm:rounded-2xl sm:w-[340px]"
        style={{ animation: 'prompt-in 0.4s cubic-bezier(0.34,1.56,0.64,1) forwards' }}
      >
        {/* Handle — solo mobile */}
        <div className="w-10 h-1 bg-slate-700 rounded-full mx-auto mt-4 sm:hidden" />

        <div className="px-6 pt-5 pb-7 sm:px-5 sm:pt-5 sm:pb-5">

          {/* Header */}
          <div className="flex items-center gap-4 mb-5">
            {!imgFailed ? (
              <img
                src={imgSrc}
                alt="Ahorro Inteligente"
                onError={handleImgError}
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
            {[
              { icon: '⚡', label: 'Acceso\ninstantáneo' },
              { icon: '🔔', label: 'Nuevas\npromos' },
              { icon: '📴', label: 'Sin\ninternet' },
            ].map(({ icon, label }, i) => (
              <div key={i} className="text-center flex-1">
                <p className="text-lg">{icon}</p>
                <p className="text-slate-400 text-[10px] mt-0.5 leading-tight whitespace-pre-line">
                  {label}
                </p>
              </div>
            ))}
          </div>

          {ios ? (
            /* iOS: instrucciones paso a paso */
            <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-3.5 mb-4 space-y-2.5">
              <p className="text-slate-300 text-xs font-semibold mb-1">
                Cómo instalar en iPhone / iPad:
              </p>
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
          ) : (
            /* Android / Chrome */
            <button
              onClick={handleInstall}
              disabled={!prompt}
              className="w-full py-3.5 rounded-xl bg-violet-600 hover:bg-violet-500 active:bg-violet-700 disabled:opacity-40 disabled:cursor-not-allowed text-white font-bold text-sm transition-all shadow-lg shadow-violet-500/25 mb-3"
            >
              {prompt ? 'Instalar app' : 'Instalá desde el menú del browser ⋮'}
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
