import { useState, useEffect } from 'react'
import { TASAS_PLAZO_FIJO, TASAS_REMUNERATIVAS, ULTIMA_ACTUALIZACION } from '../data/tasas'

// ── Dólar ────────────────────────────────────────────────────────────
function useDolar() {
  const [dolares, setDolares] = useState([])
  const [loading, setLoading] = useState(true)
  const [error,   setError]   = useState(null)

  useEffect(() => {
    fetch('https://dolarapi.com/v1/dolares')
      .then(r => { if (!r.ok) throw new Error('Error al obtener cotización'); return r.json() })
      .then(data => { setDolares(data); setLoading(false) })
      .catch(e => { setError(e.message); setLoading(false) })
  }, [])

  return { dolares, loading, error }
}

const DOLARES_MOSTRAR = ['oficial', 'blue', 'bolsa', 'contadoconliqui', 'cripto', 'mayorista']
const DOLAR_LABEL = {
  oficial:          'Oficial',
  blue:             'Blue',
  bolsa:            'Bolsa (MEP)',
  contadoconliqui:  'CCL',
  cripto:           'Cripto',
  mayorista:        'Mayorista',
}
const DOLAR_COLOR = {
  oficial:         'violet',
  blue:            'blue',
  bolsa:           'emerald',
  contadoconliqui: 'amber',
  cripto:          'indigo',
  mayorista:       'slate',
}

function fmt(n) {
  if (n == null) return '—'
  return new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(n)
}

// ── Sección Dólar ────────────────────────────────────────────────────
function SeccionDolar() {
  const { dolares, loading, error } = useDolar()

  const visibles = dolares.filter(d => DOLARES_MOSTRAR.includes(d.casa))
    .sort((a, b) => DOLARES_MOSTRAR.indexOf(a.casa) - DOLARES_MOSTRAR.indexOf(b.casa))

  return (
    <div className="mb-10">
      <div className="flex items-center gap-2 mb-4">
        <span className="text-2xl">💵</span>
        <h2 className="text-lg font-bold text-white">Cotización del Dólar</h2>
        {!loading && !error && (
          <span className="text-[10px] text-emerald-400 flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse inline-block" />
            en vivo
          </span>
        )}
      </div>

      {loading && (
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 animate-pulse h-24" />
          ))}
        </div>
      )}

      {error && (
        <p className="text-slate-500 text-sm">No se pudo cargar la cotización. Intentá más tarde.</p>
      )}

      {!loading && !error && (
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
          {visibles.map(d => {
            const color = DOLAR_COLOR[d.casa] || 'slate'
            return (
              <div key={d.casa}
                className={`bg-slate-900/60 border border-slate-800 hover:border-${color}-500/40 rounded-xl p-4 transition-all`}>
                <p className={`text-xs font-bold text-${color}-400 uppercase tracking-wide mb-2`}>
                  {DOLAR_LABEL[d.casa] || d.nombre}
                </p>
                <div className="flex justify-between items-end">
                  <div>
                    <p className="text-[10px] text-slate-500 mb-0.5">Compra</p>
                    <p className="text-sm font-bold text-white">{fmt(d.compra)}</p>
                  </div>
                  <div className="text-right">
                    <p className="text-[10px] text-slate-500 mb-0.5">Venta</p>
                    <p className="text-sm font-bold text-white">{fmt(d.venta)}</p>
                  </div>
                </div>
                {d.compra && d.venta && (
                  <p className="text-[9px] text-slate-600 mt-2 text-center">
                    Spread: {(((d.venta - d.compra) / d.compra) * 100).toFixed(1)}%
                  </p>
                )}
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}

// ── Tabla de tasas ───────────────────────────────────────────────────
function TablaTasas({ data, campo, titulo, icono, descripcion }) {
  const [filtro, setFiltro] = useState('todos') // 'todos' | 'banco' | 'fintech'

  const visible = data.filter(r => filtro === 'todos' || r.tipo === filtro)

  return (
    <div className="mb-10">
      <div className="flex flex-wrap items-center gap-3 mb-4">
        <span className="text-2xl">{icono}</span>
        <div className="flex-1 min-w-0">
          <h2 className="text-lg font-bold text-white">{titulo}</h2>
          <p className="text-xs text-slate-500">{descripcion}</p>
        </div>
        {/* Filtro tipo */}
        <div className="flex gap-1">
          {['todos','banco','fintech'].map(t => (
            <button key={t} onClick={() => setFiltro(t)}
              className={`px-3 py-1 rounded-lg text-xs font-medium border transition-all ${
                filtro === t
                  ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                  : 'bg-slate-800/60 text-slate-500 border-slate-700 hover:text-slate-300'
              }`}>
              {t === 'todos' ? 'Todos' : t === 'banco' ? '🏦 Bancos' : '📱 Fintechs'}
            </button>
          ))}
        </div>
      </div>

      <div className="overflow-hidden rounded-xl border border-slate-800">
        <table className="w-full text-sm">
          <thead>
            <tr className="bg-slate-900/80 border-b border-slate-800">
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase tracking-wide">#</th>
              <th className="text-left px-4 py-3 text-xs font-semibold text-slate-400 uppercase tracking-wide">Entidad</th>
              <th className="text-center px-4 py-3 text-xs font-semibold text-slate-400 uppercase tracking-wide">Tipo</th>
              <th className="text-right px-4 py-3 text-xs font-semibold text-slate-400 uppercase tracking-wide">
                {campo === 'tna' ? 'TNA %' : 'APR %'}
              </th>
              <th className="text-right px-4 py-3 text-xs font-semibold text-slate-400 uppercase tracking-wide hidden sm:table-cell">$1M / mes</th>
            </tr>
          </thead>
          <tbody>
            {visible.map((r, i) => {
              const tasa = r[campo]
              const ganancia30 = Math.round(1_000_000 * (tasa / 100 / 365) * 30)
              const esTop = i === 0
              return (
                <tr key={r.nombre}
                  className={`border-b border-slate-800/50 transition-colors hover:bg-slate-800/30 ${esTop ? 'bg-violet-500/5' : ''}`}>
                  <td className="px-4 py-3 text-slate-600 text-xs">{i + 1}</td>
                  <td className="px-4 py-3">
                    <a href={r.url} target="_blank" rel="noopener noreferrer"
                      className="text-slate-200 font-medium hover:text-violet-300 transition-colors flex items-center gap-1.5">
                      {esTop && <span className="text-xs">🏆</span>}
                      {r.nombre}
                    </a>
                  </td>
                  <td className="px-4 py-3 text-center">
                    <span className={`text-[10px] px-2 py-0.5 rounded-full font-medium ${
                      r.tipo === 'fintech'
                        ? 'bg-violet-500/20 text-violet-400'
                        : 'bg-blue-500/20 text-blue-400'
                    }`}>
                      {r.tipo === 'fintech' ? 'Fintech' : 'Banco'}
                    </span>
                  </td>
                  <td className="px-4 py-3 text-right">
                    <span className={`text-base font-bold ${esTop ? 'text-violet-300' : 'text-white'}`}>
                      {tasa.toFixed(1)}%
                    </span>
                  </td>
                  <td className="px-4 py-3 text-right hidden sm:table-cell">
                    <span className="text-emerald-400 text-sm font-medium">
                      +{new Intl.NumberFormat('es-AR').format(ganancia30)}
                    </span>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
      <p className="text-[10px] text-slate-600 mt-2 text-right">
        * Tasas orientativas al {ULTIMA_ACTUALIZACION}. Verificá en el sitio oficial de cada entidad.
      </p>
    </div>
  )
}

// ── Simulador de Plazo Fijo ──────────────────────────────────────────
function Simulador() {
  const [monto,    setMonto]    = useState('100000')
  const [dias,     setDias]     = useState(30)
  const [bancoIdx, setBancoIdx] = useState(0)

  const banco    = TASAS_PLAZO_FIJO[bancoIdx]
  const montoNum = parseFloat(monto.replace(/\./g, '').replace(',', '.')) || 0
  const intereses = montoNum * (banco.tna / 100 / 365) * dias
  const total     = montoNum + intereses
  const rendPct   = montoNum > 0 ? (intereses / montoNum) * 100 : 0

  const PLAZOS = [7, 14, 30, 60, 90, 180, 365]

  function formatInput(val) {
    const num = val.replace(/\D/g, '')
    return num.replace(/\B(?=(\d{3})+(?!\d))/g, '.')
  }

  return (
    <div className="mb-10">
      <div className="flex items-center gap-2 mb-4">
        <span className="text-2xl">🧮</span>
        <div>
          <h2 className="text-lg font-bold text-white">Simulador de Plazo Fijo</h2>
          <p className="text-xs text-slate-500">Calculá cuánto ganarías con los datos actuales</p>
        </div>
      </div>

      <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-5 space-y-5">
        {/* Entidad */}
        <div>
          <label className="text-xs font-semibold text-slate-400 uppercase tracking-wide block mb-2">Entidad</label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
            {TASAS_PLAZO_FIJO.slice(0, 6).map((b, i) => (
              <button key={b.nombre} onClick={() => setBancoIdx(i)}
                className={`px-3 py-2 rounded-xl text-xs font-medium border transition-all text-left ${
                  bancoIdx === i
                    ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                    : 'bg-slate-800/60 text-slate-400 border-slate-700 hover:text-slate-300'
                }`}>
                <span className="block font-semibold">{b.nombre}</span>
                <span className="text-[10px] text-slate-500">{b.tna}% TNA</span>
              </button>
            ))}
          </div>
          <select
            value={bancoIdx}
            onChange={e => setBancoIdx(Number(e.target.value))}
            className="mt-2 w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-slate-300 outline-none focus:border-violet-500 sm:hidden"
          >
            {TASAS_PLAZO_FIJO.map((b, i) => (
              <option key={b.nombre} value={i}>{b.nombre} — {b.tna}% TNA</option>
            ))}
          </select>
        </div>

        {/* Monto */}
        <div>
          <label className="text-xs font-semibold text-slate-400 uppercase tracking-wide block mb-2">
            Monto a invertir
          </label>
          <div className="relative">
            <span className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 text-sm font-bold">$</span>
            <input
              type="text"
              inputMode="numeric"
              value={monto}
              onChange={e => setMonto(formatInput(e.target.value))}
              className="w-full bg-slate-800 border border-slate-700 rounded-xl pl-8 pr-4 py-3 text-white text-lg font-bold outline-none focus:border-violet-500 transition-colors"
              placeholder="100.000"
            />
          </div>
        </div>

        {/* Plazo */}
        <div>
          <label className="text-xs font-semibold text-slate-400 uppercase tracking-wide block mb-2">Plazo</label>
          <div className="flex flex-wrap gap-2">
            {PLAZOS.map(d => (
              <button key={d} onClick={() => setDias(d)}
                className={`px-4 py-2 rounded-xl text-sm font-medium border transition-all ${
                  dias === d
                    ? 'bg-violet-600/20 text-violet-300 border-violet-500/50'
                    : 'bg-slate-800/60 text-slate-500 border-slate-700 hover:text-slate-300'
                }`}>
                {d === 365 ? '1 año' : `${d} días`}
              </button>
            ))}
          </div>
        </div>

        {/* Resultado */}
        {montoNum > 0 && (
          <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-4 space-y-3">
            <p className="text-xs font-semibold text-slate-400 uppercase tracking-wide">Resultado estimado</p>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
              <div>
                <p className="text-[10px] text-slate-500 mb-1">Capital inicial</p>
                <p className="text-base font-bold text-white">
                  {new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(montoNum)}
                </p>
              </div>
              <div>
                <p className="text-[10px] text-slate-500 mb-1">Intereses ganados</p>
                <p className="text-base font-bold text-emerald-400">
                  +{new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(intereses)}
                </p>
              </div>
              <div className="col-span-2 sm:col-span-1">
                <p className="text-[10px] text-slate-500 mb-1">Total al vencimiento</p>
                <p className="text-xl font-bold text-violet-300">
                  {new Intl.NumberFormat('es-AR', { style: 'currency', currency: 'ARS', maximumFractionDigits: 0 }).format(total)}
                </p>
              </div>
            </div>
            <div className="flex items-center gap-3 pt-1 border-t border-slate-700">
              <div className="flex-1 bg-slate-700 rounded-full h-2">
                <div className="bg-violet-500 h-2 rounded-full transition-all" style={{ width: `${Math.min(rendPct * 5, 100)}%` }} />
              </div>
              <span className="text-sm font-bold text-violet-300 tabular-nums whitespace-nowrap">
                +{rendPct.toFixed(2)}% en {dias} días
              </span>
            </div>
            <p className="text-[10px] text-slate-600">
              {banco.nombre} · {banco.tna}% TNA · {dias} días · cálculo simple sin reinversión
            </p>
          </div>
        )}
      </div>
    </div>
  )
}

// ── Página principal ─────────────────────────────────────────────────
export default function InversionPage() {
  return (
    <div>
      <div className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-white mb-2">
          Inversión <span className="text-violet-400">en Pesos</span>
        </h1>
        <p className="text-slate-400 text-sm">
          Tasas de plazo fijo, cuentas remunerativas, cotización del dólar y simulador
        </p>
      </div>

      <SeccionDolar />
      <TablaTasas
        data={TASAS_PLAZO_FIJO}
        campo="tna"
        titulo="Plazo Fijo — TNA anual"
        icono="🏛️"
        descripcion="Tasa Nominal Anual para plazo fijo a 30 días. Mayor TNA = más ganancia."
      />
      <TablaTasas
        data={TASAS_REMUNERATIVAS}
        campo="apr"
        titulo="Cuenta Remunerativa — APR"
        icono="💳"
        descripcion="Rendimiento anual de cuentas remunerativas (acreditan diariamente)."
      />
      <Simulador />
    </div>
  )
}
