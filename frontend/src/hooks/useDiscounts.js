import { useState, useEffect, useCallback } from 'react'

const API = '/api/discounts'

export function useDiscounts(filters = {}) {
  const [discounts, setDiscounts] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const fetchDiscounts = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const params = new URLSearchParams()
      Object.entries(filters).forEach(([k, v]) => {
        if (v !== null && v !== undefined && v !== '') params.append(k, v)
      })
      const res = await fetch(`${API}?${params}`)
      if (!res.ok) throw new Error('Error al cargar descuentos')
      setDiscounts(await res.json())
    } catch (e) {
      setError(e.message)
    } finally {
      setLoading(false)
    }
  }, [JSON.stringify(filters)])

  useEffect(() => { fetchDiscounts() }, [fetchDiscounts])

  return { discounts, loading, error, refetch: fetchDiscounts }
}

export function useStats() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    fetch(`${API}/stats`)
      .then(r => r.json())
      .then(setStats)
      .catch(() => {})
  }, [])

  return stats
}

export function useSources() {
  const [sources, setSources] = useState([])

  useEffect(() => {
    fetch(`${API}/sources`)
      .then(r => r.json())
      .then(setSources)
      .catch(() => {})
  }, [])

  return sources
}

export function useCategories() {
  const [categories, setCategories] = useState([])

  useEffect(() => {
    fetch(`${API}/categories`)
      .then(r => r.json())
      .then(setCategories)
      .catch(() => {})
  }, [])

  return categories
}
