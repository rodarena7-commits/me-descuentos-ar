import { useState, useRef, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

export default function UserMenu() {
  const { user, profile, logout } = useAuth()
  const navigate = useNavigate()
  const [open, setOpen] = useState(false)
  const ref = useRef(null)

  useEffect(() => {
    function handler(e) {
      if (ref.current && !ref.current.contains(e.target)) setOpen(false)
    }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  if (!user) return null

  const initials = user.displayName
    ? user.displayName.split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase()
    : user.email[0].toUpperCase()

  return (
    <div className="relative" ref={ref}>
      <button
        onClick={() => setOpen(o => !o)}
        className="flex items-center gap-2 hover:opacity-80 transition-opacity"
      >
        {user.photoURL ? (
          <img src={user.photoURL} alt={user.displayName}
            className="w-8 h-8 rounded-full border border-slate-700" />
        ) : (
          <div className="w-8 h-8 rounded-full bg-violet-600 flex items-center justify-center text-white text-xs font-bold">
            {initials}
          </div>
        )}
        <span className="text-slate-300 text-sm font-medium hidden sm:block">
          {user.displayName?.split(' ')[0]}
        </span>
        <svg className="w-3 h-3 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      {open && (
        <div className="absolute right-0 top-full mt-2 w-64 bg-slate-900 border border-slate-800 rounded-xl shadow-xl z-50 overflow-hidden">
          {/* Profile header */}
          <div className="flex items-center gap-3 p-4 border-b border-slate-800">
            {user.photoURL ? (
              <img src={user.photoURL} alt="" className="w-10 h-10 rounded-full" />
            ) : (
              <div className="w-10 h-10 rounded-full bg-violet-600 flex items-center justify-center text-white font-bold">
                {initials}
              </div>
            )}
            <div className="min-w-0">
              <p className="text-white text-sm font-semibold truncate">{user.displayName}</p>
              <p className="text-slate-500 text-xs truncate">{user.email}</p>
            </div>
          </div>

          {/* Profile info */}
          {profile && (
            <div className="p-3 border-b border-slate-800 space-y-1.5">
              {profile.location && (
                <div className="flex items-center gap-2 text-xs text-slate-400">
                  <span>📍</span>
                  <span className="truncate">{profile.location}</span>
                </div>
              )}
              {profile.shoppingDays?.length > 0 && (
                <div className="flex items-center gap-2 text-xs text-slate-400">
                  <span>🛒</span>
                  <span>{profile.shoppingDays.join(', ')}</span>
                </div>
              )}
              {profile.banks?.length > 0 && (
                <div className="flex items-center gap-2 text-xs text-slate-400">
                  <span>🏦</span>
                  <span className="truncate">{profile.banks.join(', ')}</span>
                </div>
              )}
              {profile.fintechs?.length > 0 && (
                <div className="flex items-center gap-2 text-xs text-slate-400">
                  <span>💳</span>
                  <span className="truncate">{profile.fintechs.join(', ')}</span>
                </div>
              )}
            </div>
          )}

          {/* Actions */}
          <div className="p-2">
            <button
              onClick={() => { navigate('/onboarding'); setOpen(false) }}
              className="w-full text-left px-3 py-2 text-sm text-slate-300 hover:bg-slate-800 rounded-lg transition-colors"
            >
              Editar perfil
            </button>
            <button
              onClick={() => { logout(); navigate('/login') }}
              className="w-full text-left px-3 py-2 text-sm text-red-400 hover:bg-slate-800 rounded-lg transition-colors"
            >
              Cerrar sesión
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
