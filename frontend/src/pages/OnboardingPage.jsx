import { useState } from 'react'
import AppLogo from '../components/AppLogo'
import { useNavigate } from 'react-router-dom'
import { doc, setDoc } from 'firebase/firestore'
import { ref, set } from 'firebase/database'
import { db, rtdb } from '../firebase'
import { useAuth } from '../contexts/AuthContext'

const SHOPPING_ITEMS = [
  'Carnes (res, pollo, cerdo)', 'Lácteos (leche, yogurt, queso)',
  'Verduras y frutas', 'Panificados (pan, galletitas)',
  'Bebidas (agua, gaseosas, jugos)', 'Limpieza y detergentes',
  'Perfumería e higiene', 'Snacks y golosinas',
  'Pastas, arroz y legumbres', 'Conservas y enlatados',
  'Bebidas alcohólicas', 'Medicamentos y farmacia',
  'Combustible', 'Delivery de comida', 'Ropa y calzado',
  'Electrónica y tecnología',
]

const DAYS = [
  { value: 'lunes', label: 'Lunes' },
  { value: 'martes', label: 'Martes' },
  { value: 'miercoles', label: 'Miércoles' },
  { value: 'jueves', label: 'Jueves' },
  { value: 'viernes', label: 'Viernes' },
  { value: 'sabado', label: 'Sábado' },
  { value: 'domingo', label: 'Domingo' },
]

const ALL_DAY_VALUES = DAYS.map(d => d.value)

const BANKS = [
  'Banco Galicia', 'Santander', 'BBVA', 'Banco Nación (BNA+)',
  'Banco Macro', 'Banco Patagonia', 'Cuenta DNI (Banco Provincia)',
  'HSBC', 'ICBC', 'Brubank', 'Banco Ciudad', 'Credicoop', 'Supervielle', 'Banco Comafi',
]

const FINTECHS = [
  'MercadoPago', 'Naranja X', 'Lemon', 'MODO', 'Ualá',
  'Personal Pay', 'Binance', 'Ripio', 'AstroPay', "Let'sBit", 'Bimo', 'Prex',
]

const TOTAL_STEPS = 6

const inputClass =
  'w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-slate-200 text-sm placeholder-slate-600 focus:outline-none focus:border-violet-500 transition-colors'

function StepIndicator({ step }) {
  return (
    <div className="flex items-center gap-2 mb-8">
      {Array.from({ length: TOTAL_STEPS }).map((_, i) => (
        <div
          key={i}
          className={`h-1.5 flex-1 rounded-full transition-all duration-300 ${
            i < step ? 'bg-violet-500' : i === step - 1 ? 'bg-violet-400' : 'bg-slate-700'
          }`}
        />
      ))}
    </div>
  )
}

function CheckChip({ label, selected, onToggle, highlight }) {
  return (
    <button
      type="button"
      onClick={onToggle}
      className={`px-3 py-2 rounded-lg text-sm font-medium border transition-all text-left ${
        selected
          ? highlight
            ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50'
            : 'bg-violet-500/20 text-violet-300 border-violet-500/50'
          : 'bg-slate-800/60 text-slate-400 border-slate-700 hover:border-slate-500'
      }`}
    >
      {selected && <span className="mr-1">✓</span>}{label}
    </button>
  )
}

export default function OnboardingPage() {
  const { user, setProfile } = useAuth()
  const navigate = useNavigate()
  const [step, setStep] = useState(1)
  const [saving, setSaving] = useState(false)

  // Step 1
  const [location, setLocation] = useState('')
  // Step 2 — nuevo
  const [nombre, setNombre] = useState(user?.displayName?.split(' ')[0] ?? '')
  const [edad, setEdad] = useState('')
  // Step 3
  const [items, setItems] = useState([])
  // Step 4
  const [days, setDays] = useState([])
  // Step 5
  const [banks, setBanks] = useState([])
  // Step 6
  const [fintechs, setFintechs] = useState([])

  function toggle(list, setList, value) {
    setList(prev => prev.includes(value) ? prev.filter(x => x !== value) : [...prev, value])
  }

  function toggleAllItems() {
    setItems(prev => prev.length === SHOPPING_ITEMS.length ? [] : [...SHOPPING_ITEMS])
  }

  function toggleAllDays() {
    setDays(prev => prev.length === ALL_DAY_VALUES.length ? [] : [...ALL_DAY_VALUES])
  }

  async function finish() {
    setSaving(true)
    const profile = {
      displayName: user.displayName,
      nombre: nombre.trim() || user.displayName,
      edad: edad ? parseInt(edad, 10) : null,
      email: user.email,
      photoURL: user.photoURL,
      location: location.trim() || null,
      shoppingItems: items,
      shoppingDays: days,
      banks,
      fintechs,
      onboardingComplete: true,
      createdAt: new Date().toISOString(),
    }
    await setDoc(doc(db, 'users', user.uid), profile)
    await set(ref(rtdb, `/registrations/${user.uid}`), true)
    setProfile(profile)
    navigate('/')
  }

  const allItemsSelected = items.length === SHOPPING_ITEMS.length
  const allDaysSelected = days.length === ALL_DAY_VALUES.length

  const canNext =
    step === 1 ? true
    : step === 2 ? true
    : step === 3 ? items.length > 0
    : step === 4 ? days.length > 0
    : step === 5 ? banks.length > 0
    : fintechs.length > 0

  return (
    <div className="min-h-screen bg-[#020617] flex flex-col items-center justify-center px-4 py-8">
      <div className="w-full max-w-lg">
        {/* Header */}
        <div className="flex items-center gap-3 mb-8">
          <AppLogo className="w-10 h-10" />
          <div>
            <p className="text-slate-400 text-xs">Paso {step} de {TOTAL_STEPS}</p>
            <p className="text-white font-semibold text-sm">Configurando tu perfil</p>
          </div>
        </div>

        <StepIndicator step={step} />

        <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-6 backdrop-blur-sm">

          {/* Step 1 — Bienvenida + Ubicación */}
          {step === 1 && (
            <div>
              <div className="flex items-center gap-4 mb-6">
                {user?.photoURL && (
                  <img src={user.photoURL} alt="avatar"
                    className="w-16 h-16 rounded-full border-2 border-violet-500/50" />
                )}
                <div>
                  <h2 className="text-xl font-bold text-white">¡Hola, {user?.displayName?.split(' ')[0]}!</h2>
                  <p className="text-slate-400 text-sm">{user?.email}</p>
                </div>
              </div>
              <p className="text-slate-300 text-sm mb-6">
                En unos pasos te configuramos para mostrarte solo los descuentos que te sirven de verdad.
              </p>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Tu dirección o barrio <span className="text-slate-500">(opcional)</span>
              </label>
              <input
                type="text"
                value={location}
                onChange={e => setLocation(e.target.value)}
                placeholder="Ej: Palermo, Buenos Aires"
                className={inputClass}
              />
              <p className="text-slate-600 text-xs mt-2">
                Usamos esto para mostrarte descuentos cercanos.
              </p>
            </div>
          )}

          {/* Step 2 — Nombre y edad (nuevo) */}
          {step === 2 && (
            <div className="space-y-5">
              <div>
                <h2 className="text-lg font-bold text-white mb-1">¿Cómo te llamás?</h2>
                <p className="text-slate-400 text-sm mb-4">Podés usar tu nombre o un apodo.</p>
                <input
                  type="text"
                  value={nombre}
                  onChange={e => setNombre(e.target.value)}
                  placeholder="Tu nombre o apodo"
                  className={inputClass}
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-300 mb-2">
                  ¿Cuántos años tenés? <span className="text-slate-500">(opcional)</span>
                </label>
                <input
                  type="number"
                  value={edad}
                  onChange={e => setEdad(e.target.value)}
                  placeholder="Ej: 28"
                  min="1"
                  max="110"
                  className={inputClass}
                />
                <p className="text-slate-600 text-xs mt-2">
                  Nos ayuda a personalizar mejor tus descuentos.
                </p>
              </div>
            </div>
          )}

          {/* Step 3 — Lista de compras */}
          {step === 3 && (
            <div>
              <h2 className="text-lg font-bold text-white mb-1">¿Qué es lo que más comprás?</h2>
              <p className="text-slate-400 text-sm mb-4">Seleccioná todo lo que aplique.</p>
              {/* "Todos los productos" — ocupa todo el ancho */}
              <button
                type="button"
                onClick={toggleAllItems}
                className={`w-full mb-3 px-3 py-2.5 rounded-lg text-sm font-semibold border transition-all text-center ${
                  allItemsSelected
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50'
                    : 'bg-slate-800/60 text-slate-400 border-slate-700 hover:border-slate-500'
                }`}
              >
                {allItemsSelected ? '✓ Todos los productos' : 'Seleccionar todos los productos'}
              </button>
              <div className="grid grid-cols-2 gap-2 max-h-72 overflow-y-auto pr-1">
                {SHOPPING_ITEMS.map(item => (
                  <CheckChip key={item} label={item}
                    selected={items.includes(item)}
                    onToggle={() => toggle(items, setItems, item)} />
                ))}
              </div>
            </div>
          )}

          {/* Step 4 — Días de compra */}
          {step === 4 && (
            <div>
              <h2 className="text-lg font-bold text-white mb-1">¿Qué días solés hacer las compras?</h2>
              <p className="text-slate-400 text-sm mb-4">Podés seleccionar varios días.</p>
              {/* "Todos los días" — ocupa todo el ancho */}
              <button
                type="button"
                onClick={toggleAllDays}
                className={`w-full mb-3 px-3 py-2.5 rounded-lg text-sm font-semibold border transition-all text-center ${
                  allDaysSelected
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/50'
                    : 'bg-slate-800/60 text-slate-400 border-slate-700 hover:border-slate-500'
                }`}
              >
                {allDaysSelected ? '✓ Todos los días' : 'Todos los días'}
              </button>
              <div className="grid grid-cols-2 gap-2">
                {DAYS.map(d => (
                  <CheckChip key={d.value} label={d.label}
                    selected={days.includes(d.value)}
                    onToggle={() => toggle(days, setDays, d.value)} />
                ))}
              </div>
            </div>
          )}

          {/* Step 5 — Bancos */}
          {step === 5 && (
            <div>
              <h2 className="text-lg font-bold text-white mb-1">¿Con qué bancos operás?</h2>
              <p className="text-slate-400 text-sm mb-5">Seleccioná todos los que uses.</p>
              <div className="grid grid-cols-2 gap-2 max-h-72 overflow-y-auto pr-1">
                {BANKS.map(b => (
                  <CheckChip key={b} label={b}
                    selected={banks.includes(b)}
                    onToggle={() => toggle(banks, setBanks, b)} />
                ))}
              </div>
            </div>
          )}

          {/* Step 6 — Fintechs */}
          {step === 6 && (
            <div>
              <h2 className="text-lg font-bold text-white mb-1">¿Qué billeteras o fintechs usás?</h2>
              <p className="text-slate-400 text-sm mb-5">Seleccioná todas las que uses.</p>
              <div className="grid grid-cols-2 gap-2">
                {FINTECHS.map(f => (
                  <CheckChip key={f} label={f}
                    selected={fintechs.includes(f)}
                    onToggle={() => toggle(fintechs, setFintechs, f)} />
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Navigation */}
        <div className="flex gap-3 mt-4">
          {step > 1 && (
            <button
              onClick={() => setStep(s => s - 1)}
              className="flex-1 py-3 rounded-xl border border-slate-700 text-slate-400 hover:text-slate-200 hover:border-slate-500 transition-all text-sm font-medium"
            >
              Atrás
            </button>
          )}
          {step < TOTAL_STEPS ? (
            <button
              onClick={() => setStep(s => s + 1)}
              disabled={!canNext}
              className="flex-1 py-3 rounded-xl bg-violet-600 hover:bg-violet-500 text-white font-semibold transition-all text-sm disabled:opacity-40 disabled:cursor-not-allowed"
            >
              Siguiente
            </button>
          ) : (
            <button
              onClick={finish}
              disabled={!canNext || saving}
              className="flex-1 py-3 rounded-xl bg-violet-600 hover:bg-violet-500 text-white font-semibold transition-all text-sm disabled:opacity-40 disabled:cursor-not-allowed"
            >
              {saving ? 'Guardando...' : '¡Listo, empezar!'}
            </button>
          )}
        </div>

        {/* Skip */}
        {step === 1 && (
          <button onClick={finish} className="w-full text-center text-slate-600 text-xs mt-3 hover:text-slate-400 transition-colors">
            Omitir configuración y entrar directamente
          </button>
        )}
      </div>
    </div>
  )
}
