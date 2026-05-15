import { useState } from 'react'

export default function AppLogo({ className = 'w-9 h-9', textSize = 'text-xs' }) {
  const [ok, setOk] = useState(true)

  if (ok) {
    return (
      <img
        src="/app.png"
        alt="Ahorro Inteligente"
        onError={() => setOk(false)}
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
