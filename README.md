# Instrumentación Biomédica — Práctica ECG

Repositorio de apoyo para la práctica de ECG del Módulo 2 de Instrumentación Biomédica.

## Objetivo general

Comparar tres fuentes de señal ECG utilizando un procedimiento común de documentación y análisis:

1. **BIOPAC** — adquisición experimental.
2. **Vernier** — adquisición experimental con un segundo sistema.
3. **PhysioNet** — registro de referencia para aprender primero el procedimiento de análisis.

El objetivo no es decidir cuál sistema es "mejor", sino identificar qué diferencias pueden explicarse por el sujeto, el montaje, la derivación, la colocación de electrodos y la cadena de adquisición.

## Flujo de trabajo

```text
PhysioNet
   ↓
aprender el procedimiento común
   ↓
BIOPAC ──────┐
             ├── mismo análisis ── comparación final
Vernier ─────┘
```

## Qué se documenta

Para cada fuente se registran, cuando estén disponibles:

- identificación del registro;
- montaje o derivación;
- frecuencia de muestreo;
- unidades;
- filtros y configuración;
- duración del segmento analizado;
- intervalos R–R;
- frecuencia cardíaca;
- amplitud de R;
- estabilidad de línea basal;
- ruido y artefactos.

## Estructura del repositorio

```text
instrumentacion-biomedica-ecg/
├── README.md
├── requirements.txt
├── environment.yml
├── .gitignore
├── LICENSE
├── CITATION.cff
│
├── src/
│   ├── visualizar_physionet.py
│   └── visualizar_csv.py
│
├── docs/
│   ├── PRACTICA_ECG.md
│   ├── ESTACION_A_BIOPAC.md
│   ├── ESTACION_B_VERNIER.md
│   ├── ESTACION_C_PHYSIONET.md
│   └── GUIA_GIT.md
│
├── plantillas/
│   └── reporte_comparativo_ecg.md
│
├── resultados/
│   └── README.md
│
└── data/
    └── README.md
```

## Instalación

### Opción 1 — pip

```bash
pip install -r requirements.txt
```

### Opción 2 — Conda

```bash
conda env create -f environment.yml
conda activate ecg-instrumentacion
```

## Instrucciones de la práctica

La práctica está organizada en tres estaciones. Antes de comenzar, revisen las
instrucciones correspondientes:

- [Descripción general de la práctica](docs/PRACTICA_ECG.md)
- [Estación A — BIOPAC](docs/ESTACION_A_BIOPAC.md)
- [Estación B — Vernier](docs/ESTACION_B_VERNIER.md)
- [Estación C — PhysioNet](docs/ESTACION_C_PHYSIONET.md)

Durante las tres estaciones deberán completar progresivamente:

- [Reporte comparativo ECG](plantillas/reporte_comparativo_ecg.md)

Para documentar el avance mediante control de versiones consulten:

- [Guía de Git](docs/GUIA_GIT.md)

El código disponible en `src/` es únicamente una herramienta de visualización.
Las actividades, mediciones y preguntas que deben resolver se encuentran en
los documentos anteriores.

## Uso

### PhysioNet

Coloque localmente los archivos del registro dentro de:

```text
data/physionet/
```

y ejecute:

```bash
python src/visualizar_physionet.py
```

Después de abrir la señal, continúe con las instrucciones de:

[Estación C — Procedimiento de análisis ECG con PhysioNet](docs/ESTACION_C_PHYSIONET.md)

Ahí se indica cómo seleccionar el segmento, medir los intervalos R–R,
calcular la frecuencia cardíaca, medir la amplitud y evaluar la calidad
del registro.

### BIOPAC o Vernier exportado a CSV

Una vez realizada la adquisición, exporten la señal a formato CSV cuando el software del equipo lo permita.

Coloquen el archivo dentro de:

```text
data/experimental/
```

Por ejemplo:

```text
data/experimental/biopac_equipo03.csv
data/experimental/vernier_equipo03.csv
```

Después revisen los parámetros iniciales del programa:

```text
src/visualizar_csv.py
```

y ejecuten:

```bash
python src/visualizar_csv.py
```

Después de visualizar la señal, continúen con las instrucciones de la estación correspondiente:

- [Estación A — BIOPAC](docs/ESTACION_A_BIOPAC.md)
- [Estación B — Vernier](docs/ESTACION_B_VERNIER.md)

Para el análisis seleccionen aproximadamente 10 s de señal y apliquen el mismo procedimiento utilizado con el registro de PhysioNet:

- identificación de intervalos R–R;
- cálculo de frecuencia cardíaca;
- medición aproximada de la amplitud de R;
- evaluación de la estabilidad de la línea basal;
- identificación de ruido y artefactos;
- documentación de la configuración instrumental.

Registren los resultados en:

[Reporte comparativo ECG](plantillas/reporte_comparativo_ecg.md)

No modifiquen ni sobrescriban el archivo original exportado por el equipo. Conserven siempre una copia del registro crudo y trabajen sobre una copia para el análisis.

El código disponible en `src/` se utiliza únicamente como **herramienta de visualización**. La práctica evalúa la adquisición, documentación, interpretación instrumental, trazabilidad y comparación de los registros.

## Datos fisiológicos

Los archivos crudos de BIOPAC, Vernier y PhysioNet **no se incluyen en este repositorio público**.

No deben publicarse nombres ni otros datos identificables de los voluntarios.

## Control de versiones

Git permite conservar cómo evoluciona el trabajo experimental. Un historial posible sería:

```text
Completa comparación BIOPAC Vernier PhysioNet
Agrega mediciones del registro Vernier
Agrega mediciones del registro BIOPAC
Agrega análisis del ECG de referencia PhysioNet
```

Así se conserva no sólo el resultado final, sino también **cómo se construyó**.
