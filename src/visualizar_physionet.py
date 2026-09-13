"""
Visor sencillo de un registro ECG local en formato WFDB.

Uso docente:
- no realiza diagnóstico;
- no detecta automáticamente los complejos QRS;
- permite visualizar un segmento para que el estudiante haga las mediciones.

Coloque los archivos .hea/.dat del registro dentro de:
data/physionet/
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import wfdb

# ------------------------------------------------------------
# Parámetros que puede modificar el estudiante
# ------------------------------------------------------------
RECORD_NAME = "16265"
CHANNEL = 0
START_TIME = 0.0       # s
DURATION = 10.0        # s
# ------------------------------------------------------------

BASE = Path(__file__).resolve().parents[1]
record_path = BASE / "data" / "physionet" / RECORD_NAME

record = wfdb.rdrecord(str(record_path))

fs = float(record.fs)
start = int(START_TIME * fs)
stop = min(start + int(DURATION * fs), record.p_signal.shape[0])

signal = record.p_signal[start:stop, CHANNEL]
time = (start + np.arange(len(signal))) / fs

sig_name = (
    record.sig_name[CHANNEL]
    if getattr(record, "sig_name", None)
    else f"Canal {CHANNEL}"
)

units = (
    record.units[CHANNEL]
    if getattr(record, "units", None)
    else "unidad no indicada"
)

print(f"Registro: {RECORD_NAME}")
print(f"Canal: {CHANNEL} ({sig_name})")
print(f"Frecuencia de muestreo: {fs:g} Hz")
print(f"Unidad: {units}")
print(f"Segmento mostrado: {START_TIME:g} s a {time[-1]:.3f} s")

plt.figure(figsize=(11, 4))
plt.plot(time, signal)
plt.xlabel("Tiempo (s)")
plt.ylabel(units)
plt.title(f"PhysioNet — {RECORD_NAME} — {sig_name}")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
