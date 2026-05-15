import { useState, useRef, useEffect } from 'react'

const BOT_URL = import.meta.env.VITE_BOT_URL || 'https://descuentostuyos.onrender.com'

// Genera un session ID único por visita
function getSessionId() {
    let id = sessionStorage.getItem('chat-session-id')
    if (!id) {
        id = Math.random().toString(36).slice(2)
        sessionStorage.setItem('chat-session-id', id)
    }
    return id
}

const SUGERENCIAS = [
    '¿Qué descuentos hay en supermercados?',
    '¿Descuentos del 30% o más?',
    '¿Qué ofertas hay los martes?',
    '¿Qué hace Galicia esta semana?',
    '¿Dónde hay reintegros en combustible?',
]

function MensajeBot({ texto }) {
    return (
        <div className="flex items-start gap-2 mb-3">
            <div className="w-7 h-7 rounded-full bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center flex-shrink-0 mt-0.5 shadow">
                <span className="text-white text-[10px] font-black">AI</span>
            </div>
            <div className="bg-slate-800 border border-slate-700 rounded-2xl rounded-tl-sm px-4 py-3 max-w-[85%]">
                <p className="text-slate-200 text-sm leading-relaxed whitespace-pre-wrap">{texto}</p>
            </div>
        </div>
    )
}

function MensajeUsuario({ texto }) {
    return (
        <div className="flex justify-end mb-3">
            <div className="bg-violet-600 rounded-2xl rounded-tr-sm px-4 py-3 max-w-[85%]">
                <p className="text-white text-sm leading-relaxed">{texto}</p>
            </div>
        </div>
    )
}

function TypingDots() {
    return (
        <div className="flex items-start gap-2 mb-3">
            <div className="w-7 h-7 rounded-full bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center flex-shrink-0 mt-0.5 shadow">
                <span className="text-white text-[10px] font-black">AI</span>
            </div>
            <div className="bg-slate-800 border border-slate-700 rounded-2xl rounded-tl-sm px-4 py-3">
                <div className="flex gap-1 items-center h-4">
                    {[0, 1, 2].map(i => (
                        <div
                            key={i}
                            className="w-1.5 h-1.5 rounded-full bg-violet-400"
                            style={{ animation: `bounce 1s ease-in-out ${i * 0.2}s infinite` }}
                        />
                    ))}
                </div>
            </div>
        </div>
    )
}

export default function ChatBot() {
    const [open, setOpen] = useState(false)
    const [messages, setMessages] = useState([
        { role: 'bot', text: '¡Hola! 👋 Soy tu asistente de descuentos. Preguntame lo que quieras: por banco, categoría, día de la semana o porcentaje.' }
    ])
    const [input, setInput] = useState('')
    const [loading, setLoading] = useState(false)
    const [shown, setShown] = useState(false)
    const bottomRef = useRef(null)
    const inputRef = useRef(null)
    const sessionId = useRef(getSessionId())

    // Auto-scroll al último mensaje
    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
    }, [messages, loading])

    // Focus input al abrir
    useEffect(() => {
        if (open) setTimeout(() => inputRef.current?.focus(), 100)
    }, [open])

    // Mostrar badge "nuevo" brevemente
    useEffect(() => {
        const t = setTimeout(() => setShown(true), 8000)
        return () => clearTimeout(t)
    }, [])

    async function enviar(texto) {
        const msg = texto || input.trim()
        if (!msg || loading) return
        setInput('')
        setMessages(prev => [...prev, { role: 'user', text: msg }])
        setLoading(true)

        try {
            const res = await fetch(`${BOT_URL}/api/chat`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: msg, sessionId: sessionId.current }),
            })
            const data = await res.json()
            setMessages(prev => [...prev, { role: 'bot', text: data.respuesta || '⚠️ Sin respuesta del bot.' }])
        } catch {
            setMessages(prev => [...prev, { role: 'bot', text: '⚠️ No pude conectarme con el bot. Intentá de nuevo.' }])
        } finally {
            setLoading(false)
        }
    }

    function handleKey(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault()
            enviar()
        }
    }

    return (
        <>
            {/* ── Ventana de chat ── */}
            {open && (
                <div className="fixed bottom-16 left-4 right-4 sm:left-auto sm:right-4 sm:w-[360px] z-40 flex flex-col bg-slate-900 border border-slate-700 rounded-2xl shadow-2xl shadow-violet-500/10 overflow-hidden"
                    style={{ maxHeight: '70vh', animation: 'slide-up 0.3s ease forwards' }}
                >
                    {/* Header */}
                    <div className="flex items-center gap-3 px-4 py-3 bg-slate-950/80 border-b border-slate-800">
                        <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-violet-600 to-indigo-700 flex items-center justify-center shadow">
                            <span className="text-white text-xs font-black">AI</span>
                        </div>
                        <div className="flex-1">
                            <p className="text-white text-sm font-semibold">Asistente de Descuentos</p>
                            <div className="flex items-center gap-1.5">
                                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                                <span className="text-emerald-400 text-[10px]">En línea</span>
                            </div>
                        </div>
                        <button
                            onClick={() => setOpen(false)}
                            className="w-7 h-7 flex items-center justify-center rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-all"
                        >
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>

                    {/* Mensajes */}
                    <div className="flex-1 overflow-y-auto px-4 py-4 space-y-1">
                        {messages.map((m, i) =>
                            m.role === 'bot'
                                ? <MensajeBot key={i} texto={m.text} />
                                : <MensajeUsuario key={i} texto={m.text} />
                        )}
                        {loading && <TypingDots />}
                        <div ref={bottomRef} />
                    </div>

                    {/* Sugerencias rápidas (solo si no hay muchos mensajes) */}
                    {messages.length <= 2 && !loading && (
                        <div className="px-4 pb-2 flex gap-2 overflow-x-auto scrollbar-hide">
                            {SUGERENCIAS.slice(0, 3).map(s => (
                                <button
                                    key={s}
                                    onClick={() => enviar(s)}
                                    className="flex-shrink-0 text-[10px] text-violet-400 border border-violet-500/30 bg-violet-500/5 hover:bg-violet-500/15 rounded-full px-3 py-1.5 transition-all whitespace-nowrap"
                                >
                                    {s}
                                </button>
                            ))}
                        </div>
                    )}

                    {/* Input */}
                    <div className="px-3 py-3 border-t border-slate-800 bg-slate-950/40">
                        <div className="flex items-end gap-2">
                            <textarea
                                ref={inputRef}
                                rows={1}
                                value={input}
                                onChange={e => setInput(e.target.value)}
                                onKeyDown={handleKey}
                                placeholder="Preguntá sobre descuentos..."
                                disabled={loading}
                                className="flex-1 bg-slate-800 border border-slate-700 rounded-xl px-3 py-2.5 text-sm text-slate-200 placeholder-slate-500 resize-none focus:outline-none focus:border-violet-500 transition-colors disabled:opacity-50"
                                style={{ maxHeight: '100px' }}
                            />
                            <button
                                onClick={() => enviar()}
                                disabled={!input.trim() || loading}
                                className="w-10 h-10 rounded-xl bg-violet-600 hover:bg-violet-500 disabled:opacity-40 disabled:cursor-not-allowed flex items-center justify-center transition-all flex-shrink-0"
                            >
                                <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                                </svg>
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* ── Botón flotante ── esquina inferior derecha */}
            <button
                onClick={() => setOpen(o => !o)}
                className="fixed bottom-4 right-4 z-40 w-9 h-9 rounded-xl bg-gradient-to-br from-violet-600 to-indigo-700 shadow-lg shadow-violet-500/40 flex items-center justify-center hover:scale-110 active:scale-95 transition-transform"
                aria-label="Abrir asistente de descuentos"
            >
                {open ? (
                    <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                ) : (
                    <>
                        <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2}
                                d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                        </svg>
                        {shown && !open && (
                            <span className="absolute -top-0.5 -right-0.5 w-2.5 h-2.5 bg-emerald-500 rounded-full border border-slate-900 animate-pulse" />
                        )}
                    </>
                )}
            </button>
        </>
    )
}
