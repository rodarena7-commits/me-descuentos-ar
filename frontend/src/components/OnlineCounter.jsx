// Widget desapercibido en esquina inferior derecha — solo visible cuando hay datos.
export default function OnlineCounter({ count }) {
  if (count === null) return null

  return (
    <div
      title={`${count} usuario${count !== 1 ? 's' : ''} conectado${count !== 1 ? 's' : ''} ahora`}
      className="fixed bottom-5 right-5 z-30 flex items-center gap-1.5 bg-slate-950/70 border border-slate-800/50 rounded-full px-2.5 py-1 backdrop-blur-sm select-none"
    >
      <span className="w-1.5 h-1.5 rounded-full bg-emerald-500/80 animate-pulse flex-shrink-0" />
      <span className="text-slate-600 text-[10px] font-medium tabular-nums">{count}</span>
    </div>
  )
}
