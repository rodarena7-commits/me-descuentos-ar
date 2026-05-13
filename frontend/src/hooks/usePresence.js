import { useEffect, useState } from 'react'
import { ref, onValue, set, remove, onDisconnect } from 'firebase/database'
import { rtdb } from '../firebase'
import { useAuth } from '../contexts/AuthContext'

// Registra al usuario como "online" y devuelve el total de conectados en tiempo real.
// Firebase RTDB elimina el registro automáticamente al desconectarse (cierra tab, pierde red).
export function usePresence() {
  const { user } = useAuth()
  const [onlineCount, setOnlineCount] = useState(null)

  // Registrar presencia del usuario actual
  useEffect(() => {
    if (!user) return

    const connectedRef = ref(rtdb, '.info/connected')
    const presenceRef  = ref(rtdb, `/presence/${user.uid}`)

    const unsub = onValue(connectedRef, (snap) => {
      if (snap.val() !== true) return
      // Escribir presencia
      set(presenceRef, {
        displayName: user.displayName ?? 'Anónimo',
        connectedAt: Date.now(),
      })
      // Eliminar al desconectarse (manejado por el servidor de Firebase)
      onDisconnect(presenceRef).remove()
    })

    return () => {
      unsub()
      // Limpiar al desmontar (logout, navegación)
      remove(presenceRef)
    }
  }, [user])

  // Escuchar el total de usuarios online
  useEffect(() => {
    const allRef = ref(rtdb, '/presence')
    const unsub = onValue(allRef, (snap) => {
      const val = snap.val()
      setOnlineCount(val ? Object.keys(val).length : 0)
    })
    return () => unsub()
  }, [])

  return onlineCount
}
