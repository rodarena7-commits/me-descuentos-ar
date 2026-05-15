import { useState } from 'react'

export default function AppLogo({ className = 'w-9 h-9', textSize = 'text-xs' }) {
  // Intenta app.png primero; si falla, usa favicon.svg; si falla, muestra "AI"
  const [src, setSrc] = useState('/app.png')
  const [failed, setFailed] = useState(false)

  function handleError() {
    if (src === '/app.png') {
      setSrc('/favicon.svg')
    } else {
      setFailed(true)
    }
  }

  if (!failed) {
    return (
      <img
        src={src}
        alt="Ahorro Inteligente"
        onError={handleError}
        className={`${className} rounded-xl object-cover shadow-lg shadow-violet-500/20`}
      />
    )
  }

  return (
    <div className={`${className} rounded-xl bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center text-white font-black ${textSize} tracking-tight shadow-lg shadow-violet-500/30`}>
      AI
    </div>
  )
}
