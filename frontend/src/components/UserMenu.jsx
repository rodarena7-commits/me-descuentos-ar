import { useState, useRef, useEffect, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import { ref, onValue } from 'firebase/database'
import { collection, getDocs } from 'firebase/firestore'
import { rtdb, db } from '../firebase'
import { useAuth } from '../contexts/AuthContext'

const ADMIN_EMAIL = 'rodrigo.n.arena@hotmail.com'

// ── Hook: carga usuarios de Firestore + online de RTDB ───────────────────────
function useAdminStats(isAdmin) {
  const [allUsers, setAllUsers]   = useState([])   // todos los perfiles de Firestore
  const [onlineUids, setOnlineUids] = useState([]) // UIDs activos en RTDB /presence
  const [fsLoading, setFsLoading] = useState(true)
  const [error, setError]         = useState(null)

  useEffect(() => {
    if (!isAdmin) return

    // 1. Cargar TODOS los perfiles de Firestore /users
    getDocs(collection(db, 'users'))
      .then(snap => {
        const users = []
        snap.forEach(d => users.push({ uid: d.id, ...d.data() }))
        users.sort((a, b) => (a.displayName || a.email || '').localeCompare(b.displayName || b.email || ''))
        setAllUsers(users)
        setError(null)
      })
      .catch(err => setError(err.code || err.message))
      .finally(() => setFsLoading(false))

    // 2. Escuchar online en RTDB /presence
    const unsubPres = onValue(
      ref(rtdb, '/presence'),
      snap => setOnlineUids(snap.val() ? Object.keys(snap.val()) : []),
      () => {},
    )

    return () => unsubPres()
  }, [isAdmin])

  return { allUsers, onlineUids, error, fsLoading }
}

// ── Modal de usuarios — fetchea directo de Firestore ─────────────────────────
function UsersModal({ title, filterUids, onClose }) {
  const [users, setUsers]     = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    getDocs(collection(db, 'users'))
      .then(snap => {
        const all = []
        snap.forEach(d => all.push({ uid: d.id, ...d.data() }))
        // Si filterUids está definido → solo mostrar esos UIDs (online)
        const result = filterUids
          ? all.filter(u => filterUids.includes(u.uid))
          : all
        result.sort((a, b) =>
          (a.displayName || a.email || '').localeCompare(b.displayName || b.email || '')
        )
        setUsers(result)
      })
      .catch(err => console.error('UsersModal fetch error:', err))
      .finally(() => setLoading(false))
  }, [])

  return (
    <>
      {/* Overlay */}
      <div
        className="fixed inset-0 z-[60] bg-black/50 backdrop-blur-sm"
        onClick={onClose}
      />

      {/* Panel lateral */}
      <div className="fixed top-0 right-0 bottom-0 z-[70] w-full max-w-sm bg-slate-900 border-l border-slate-800 shadow-2xl flex flex-col"
        style={{ animation: 'slide-left 0.3s ease forwards' }}
      >
        {/* Header */}
        <div className="flex items-center justify-between px-5 py-4 border-b border-slate-800">
          <div>
            <h3 className="text-white font-semibold text-base">{title}</h3>
            {!loading && (
              <p className="text-slate-500 text-xs mt-0.5">
                {users.length} {users.length === 1 ? 'usuario' : 'usuarios'}
              </p>
            )}
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 flex items-center justify-center rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-all"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Lista */}
        <div className="flex-1 overflow-y-auto px-4 py-3 space-y-2">
          {loading && (
            <div className="space-y-2 mt-2">
              {[...Array(5)].map((_, i) => (
                <div key={i} className="flex items-center gap-3 p-3 bg-slate-800/40 rounded-xl animate-pulse">
                  <div className="w-9 h-9 rounded-full bg-slate-700 flex-shrink-0" />
                  <div className="flex-1 space-y-1.5">
                    <div className="h-3 bg-slate-700 rounded w-3/5" />
                    <div className="h-2.5 bg-slate-700 rounded w-4/5" />
                  </div>
                </div>
              ))}
            </div>
          )}

          {!loading && users.length === 0 && (
            <div className="text-center py-16">
              <p className="text-4xl mb-3">👤</p>
              <p className="text-slate-400 text-sm">No hay usuarios para mostrar</p>
            </div>
          )}

          {!loading && users.map(u => (
            <div key={u.uid} className="flex items-center gap-3 p-3 bg-slate-800/40 rounded-xl border border-slate-800 hover:border-slate-700 transition-colors">
              {u.photoURL ? (
                <img src={u.photoURL} alt={u.displayName}
                  className="w-9 h-9 rounded-full flex-shrink-0 border border-slate-700" />
              ) : (
                <div className="w-9 h-9 rounded-full bg-violet-600/30 border border-violet-500/30 flex items-center justify-center text-violet-400 font-bold text-sm flex-shrink-0">
                  {(u.displayName || u.email || '?')[0].toUpperCase()}
                </div>
              )}
              <div className="flex-1 min-w-0">
                <p className="text-slate-200 text-sm font-medium truncate">
                  {u.nombre || u.displayName || '—'}
                </p>
                <p className="text-slate-500 text-xs truncate">{u.email}</p>
                {u.edad && (
                  <p className="text-slate-600 text-[10px]">{u.edad} años</p>
                )}
              </div>
              {u.location && (
                <span className="text-[10px] text-slate-500 flex-shrink-0">📍 {u.location}</span>
              )}
            </div>
          ))}
        </div>
      </div>
    </>
  )
}

// ── Componente principal ──────────────────────────────────────────────────────
export default function UserMenu() {
  const { user, profile, logout } = useAuth()
  const navigate = useNavigate()
  const [open, setOpen]         = useState(false)
  const [modal, setModal]       = useState(null)  // null | 'registered' | 'online'
  const menuRef = useRef(null)

  const isAdmin = user?.email?.toLowerCase() === ADMIN_EMAIL.toLowerCase()
  const { allUsers, onlineUids, error, fsLoading } = useAdminStats(isAdmin)

  // Usuarios online = los que están en /presence Y tienen perfil en Firestore
  const onlineUsers = allUsers.filter(u => onlineUids.includes(u.uid))

  // Estado reactivo: ¿la app ya está instalada como PWA?
  const [appInstalled, setAppInstalled] = useState(
    () => window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true
  )
  useEffect(() => {
    const mq = window.matchMedia('(display-mode: standalone)')
    const onChange = e => setAppInstalled(e.matches)
    mq.addEventListener('change', onChange)
    const onInstalled = () => setAppInstalled(true)
    window.addEventListener('pwa-app-installed', onInstalled)
    return () => {
      mq.removeEventListener('change', onChange)
      window.removeEventListener('pwa-app-installed', onInstalled)
    }
  }, [])

  useEffect(() => {
    function handler(e) {
      if (menuRef.current && !menuRef.current.contains(e.target)) setOpen(false)
    }
    document.addEventListener('mousedown', handler)
    return () => document.removeEventListener('mousedown', handler)
  }, [])

  if (!user) return null

  const initials = user.displayName
    ? user.displayName.split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase()
    : user.email[0].toUpperCase()

  return (
    <>
      <div className="relative" ref={menuRef}>
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
          <div className="absolute right-0 top-full mt-2 w-72 bg-slate-900 border border-slate-800 rounded-xl shadow-xl z-50 overflow-hidden">

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
                {isAdmin && (
                  <span className="text-[10px] bg-violet-500/20 text-violet-400 border border-violet-500/30 px-1.5 py-0.5 rounded-full font-medium mt-0.5 inline-block">
                    Admin
                  </span>
                )}
              </div>
            </div>

            {/* Admin stats — solo visible para rodrigo.n.arena@hotmail.com */}
            {isAdmin && (
              <div className="px-4 py-3 border-b border-slate-800 bg-slate-950/40">
                <p className="text-[10px] text-slate-500 uppercase tracking-wider mb-2 font-medium">
                  Panel de administración
                </p>
                {error ? (
                  <div className="bg-red-900/20 border border-red-500/30 rounded-lg p-2.5">
                    <p className="text-[10px] text-red-400 text-center">
                      ⚠️ Error al cargar datos: {error}
                    </p>
                    <p className="text-[9px] text-red-400/60 text-center mt-0.5">
                      Revisá las reglas de Firestore
                    </p>
                  </div>
                ) : (
                  <div className="grid grid-cols-2 gap-2">
                    {/* Registrados — clickeable */}
                    <button
                      onClick={() => { setModal('registered'); setOpen(false) }}
                      className="bg-slate-800/60 rounded-lg p-2.5 text-center hover:bg-slate-700/60 hover:border-violet-500/40 border border-transparent transition-all group cursor-pointer"
                    >
                      <p className="text-lg font-bold text-violet-400 tabular-nums group-hover:text-violet-300">
                        {fsLoading ? '…' : allUsers.length}
                      </p>
                      <p className="text-[10px] text-slate-500 group-hover:text-slate-400">Registrados</p>
                      <p className="text-[9px] text-violet-600 group-hover:text-violet-400 mt-0.5">ver lista →</p>
                    </button>

                    {/* Online ahora — clickeable */}
                    <button
                      onClick={() => { setModal('online'); setOpen(false) }}
                      className="bg-slate-800/60 rounded-lg p-2.5 text-center hover:bg-slate-700/60 hover:border-emerald-500/40 border border-transparent transition-all group cursor-pointer"
                    >
                      <div className="flex items-center justify-center gap-1">
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                        <p className="text-lg font-bold text-emerald-400 tabular-nums group-hover:text-emerald-300">
                          {onlineUids.length}
                        </p>
                      </div>
                      <p className="text-[10px] text-slate-500 group-hover:text-slate-400">Online ahora</p>
                      <p className="text-[9px] text-emerald-700 group-hover:text-emerald-500 mt-0.5">ver lista →</p>
                    </button>
                  </div>
                )}
              </div>
            )}

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
                    <span className="truncate">
                      {profile.banks.slice(0, 3).join(', ')}
                      {profile.banks.length > 3 ? ` +${profile.banks.length - 3}` : ''}
                    </span>
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

              {/* Instalar app — solo visible si la app NO está instalada */}
              {!appInstalled && (
                <button
                  onClick={() => {
                    setOpen(false)
                    window.dispatchEvent(new CustomEvent('show-install-prompt'))
                  }}
                  className="w-full text-left px-3 py-2 text-sm text-violet-400 hover:bg-slate-800 rounded-lg transition-colors flex items-center gap-2"
                >
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                      d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Instalar app
                </button>
              )}

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

      {/* Modal de usuarios registrados — todos los perfiles de Firestore */}
      {modal === 'registered' && (
        <UsersModal
          title="Usuarios registrados"
          filterUids={null}
          onClose={() => setModal(null)}
        />
      )}

      {/* Modal de usuarios online — solo los UIDs de RTDB /presence */}
      {modal === 'online' && (
        <UsersModal
          title="Usuarios online ahora"
          filterUids={onlineUids}
          onClose={() => setModal(null)}
        />
      )}
    </>
  )
}
