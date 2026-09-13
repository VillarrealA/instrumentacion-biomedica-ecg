"""
Visor genérico para señales ECG exportadas a CSV.

Puede emplearse con BIOPAC o Vernier cuando el software permita
exportar la señal.

No realiza diagnóstico ni detección automática de QRS.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Parámetros que debe revisar el estudiante
# ------------------------------------------------------------
CSV_FILE = "registro.csv"
SIGNAL_COLUMN = None     # Ejemplo: "ECG". None -> primera columna numérica
TIME_COLUMN = None       # Ejemplo: "Time". None -> se construye con FS
FS = 500.0               # Hz; usar sólo si no hay columna de tiempo
START_TIME = 0.0         # s
DURATION = 10.0          # s
# ------------------------------------------------------------

BASE = Path(__file__).resolve().parents[1]
path = BASE / "data" / "experimental" / CSV_FILE

df = pd.read_csv(path)

if SIGNAL_COLUMN is None:
    numeric = df.select_dtypes(include="number").columns.tolist()
    if not numeric:
        raise ValueError("No se encontró ninguna columna numérica.")
    signal_col = numeric[0]
else:
    signal_col = SIGNAL_COLUMN

signal_all = df[signal_col].to_numpy(dtype=float)

if TIME_COLUMN is not None:
    time_all = df[TIME_COLUMN].to_numpy(dtype=float)
    mask = (time_all >= START_TIME) & (time_all < START_TIME + DURATION)
    time = time_all[mask]
    signal = signal_all[mask]

    if len(time) > 1:
        fs_est = 1.0 / np.median(np.diff(time))
    else:
        fs_est = float("nan")
else:
    fs_est = float(FS)
    start = int(START_TIME * fs_est)
    stop = min(start + int(DURATION * fs_est), len(signal_all))
    signal = signal_all[start:stop]
    time = np.arange(start, stop) / fs_est

print(f"Archivo: {CSV_FILE}")
print(f"Columna de señal: {signal_col}")
print(f"Frecuencia de muestreo usada/estimada: {fs_est:.3f} Hz")
print(f"Número de muestras mostradas: {len(signal)}")

plt.figure(figsize=(11, 4))
plt.plot(time, signal)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title(f"ECG experimental — {CSV_FILE}")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
