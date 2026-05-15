import { useState, useEffect } from 'react'

function WalletSVG() {
  return (
    <svg viewBox="0 0 120 100" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full">
      <defs>
        <linearGradient id="walletBody" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#7c3aed" />
          <stop offset="100%" stopColor="#4338ca" />
        </linearGradient>
        <linearGradient id="walletFlap" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#6d28d9" />
          <stop offset="100%" stopColor="#3730a3" />
        </linearGradient>
        <linearGradient id="coinGrad" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="#fbbf24" />
          <stop offset="100%" stopColor="#d97706" />
        </linearGradient>
        <filter id="glow">
          <feGaussianBlur stdDeviation="2.5" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      {/* Wallet body */}
      <rect x="8" y="38" width="104" height="58" rx="10" fill="url(#walletBody)" />

      {/* Card slot */}
      <rect x="18" y="52" width="50" height="8" rx="4" fill="rgba(255,255,255,0.18)" />
      <rect x="18" y="65" width="35" height="5" rx="2.5" fill="rgba(255,255,255,0.12)" />

      {/* Coin compartment */}
      <circle cx="88" cy="70" r="16" fill="rgba(255,255,255,0.08)" />
      <circle cx="88" cy="70" r="11" fill="url(#coinGrad)" filter="url(#glow)" />
      <text x="84" y="74" fontSize="10" fill="#92400e" fontWeight="bold">$</text>

      {/* Wallet flap — se abre con animación */}
      <g className="flap-anim">
        <rect x="8" y="18" width="104" height="26" rx="10" fill="url(#walletFlap)" />
        {/* Clasp */}
        <rect x="50" y="32" width="20" height="7" rx="3.5" fill="rgba(255,255,255,0.45)" />
        <circle cx="60" cy="35.5" r="2" fill="rgba(255,255,255,0.7)" />
      </g>
    </svg>
  )
}

function ButterflySVG() {
  return (
    <svg viewBox="0 0 80 64" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-20 h-16">
      <defs>
        <radialGradient id="wingUL">
          <stop offset="0%" stopColor="#e879f9" />
          <stop offset="100%" stopColor="#a855f7" />
        </radialGradient>
        <radialGradient id="wingUR">
          <stop offset="0%" stopColor="#c084fc" />
          <stop offset="100%" stopColor="#7c3aed" />
        </radialGradient>
        <radialGradient id="wingLL">
          <stop offset="0%" stopColor="#a855f7" />
          <stop offset="100%" stopColor="#6d28d9" />
        </radialGradient>
        <radialGradient id="wingLR">
          <stop offset="0%" stopColor="#9333ea" />
          <stop offset="100%" stopColor="#581c87" />
        </radialGradient>
      </defs>

      {/* Ala superior izquierda */}
      <path
        className="wing-left-anim"
        d="M40 34 C28 18, 10 10, 10 24 C10 36, 28 38, 40 34Z"
        fill="url(#wingUL)"
        opacity="0.95"
      />
      {/* Ala superior derecha */}
      <path
        className="wing-right-anim"
        d="M40 34 C52 18, 70 10, 70 24 C70 36, 52 38, 40 34Z"
        fill="url(#wingUR)"
        opacity="0.95"
      />
      {/* Ala inferior izquierda */}
      <path
        className="wing-left-anim"
        d="M40 36 C22 38, 8 52, 16 58 C24 63, 38 48, 40 36Z"
        fill="url(#wingLL)"
        opacity="0.88"
      />
      {/* Ala inferior derecha */}
      <path
        className="wing-right-anim"
        d="M40 36 C58 38, 72 52, 64 58 C56 63, 42 48, 40 36Z"
        fill="url(#wingLR)"
        opacity="0.88"
      />

      {/* Cuerpo */}
      <ellipse cx="40" cy="36" rx="3" ry="10" fill="#3b0764" />
      <ellipse cx="40" cy="28" rx="2" ry="4" fill="#581c87" />

      {/* Antenas */}
      <path d="M38 25 C35 17, 28 11, 25 7" stroke="#7c3aed" strokeWidth="1.5" strokeLinecap="round" fill="none"/>
      <circle cx="25" cy="7" r="2.5" fill="#c084fc" />
      <path d="M42 25 C45 17, 52 11, 55 7" stroke="#7c3aed" strokeWidth="1.5" strokeLinecap="round" fill="none"/>
      <circle cx="55" cy="7" r="2.5" fill="#c084fc" />

      {/* Detalles en las alas */}
      <circle cx="22" cy="26" r="3" fill="rgba(255,255,255,0.2)" />
      <circle cx="58" cy="26" r="3" fill="rgba(255,255,255,0.2)" />
    </svg>
  )
}

function Sparkle({ className, style }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" className={`w-5 h-5 ${className}`} style={style}>
      <path d="M12 2 L13.5 9 L20 12 L13.5 15 L12 22 L10.5 15 L4 12 L10.5 9 Z"
        fill="#c084fc" opacity="0.8" />
    </svg>
  )
}

export default function LoadingScreen({ show }) {
  const [visible, setVisible] = useState(show)
  const [fadingOut, setFadingOut] = useState(false)
  const [dots, setDots] = useState('')

  // Animación de puntos
  useEffect(() => {
    const seq = ['', '.', '..', '...']
    let i = 0
    const t = setInterval(() => {
      i = (i + 1) % seq.length
      setDots(seq[i])
    }, 500)
    return () => clearInterval(t)
  }, [])

  // Fade-out cuando termina de cargar
  useEffect(() => {
    if (!show && visible) {
      setFadingOut(true)
      const t = setTimeout(() => setVisible(false), 600)
      return () => clearTimeout(t)
    }
    if (show) {
      setVisible(true)
      setFadingOut(false)
    }
  }, [show])

  if (!visible) return null

  return (
    <div
      className={`fixed inset-0 z-40 bg-[#020617] flex flex-col items-center justify-center px-6 ${fadingOut ? 'screen-fade-out' : ''}`}
    >
      {/* Contenedor principal de la animación */}
      <div className="relative flex flex-col items-center select-none">

        {/* Chispas alrededor de la mariposa */}
        <div className="absolute -top-6 -left-8">
          <Sparkle className="sparkle-1" />
        </div>
        <div className="absolute -top-10 right-0">
          <Sparkle className="sparkle-2" style={{ width: '14px', height: '14px' }} />
        </div>
        <div className="absolute top-0 -right-10">
          <Sparkle className="sparkle-3" />
        </div>

        {/* Mariposa — emerge y flota */}
        <div className="butterfly-emerge-anim butterfly-hover-anim mb-[-16px] z-10">
          <ButterflySVG />
        </div>

        {/* Billetera */}
        <div className="wallet-anim wallet-shake-anim w-36 h-28">
          <WalletSVG />
        </div>
      </div>

      {/* Texto de carga */}
      <div className="mt-10 text-center space-y-2">
        <p className="text-white font-semibold text-lg">
          Buscando los mejores descuentos
        </p>
        <p className="text-violet-400 text-sm font-medium h-5">
          para vos{dots}
        </p>
      </div>

      {/* Barra de progreso */}
      <div className="mt-6 w-48 h-1 bg-slate-800 rounded-full overflow-hidden">
        <div
          className="h-full rounded-full bg-gradient-to-r from-violet-500 to-fuchsia-500"
          style={{ animation: 'shimmer 1.8s ease-in-out infinite', width: '60%' }}
        />
      </div>
    </div>
  )
}
