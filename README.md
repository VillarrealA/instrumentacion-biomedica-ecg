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

### BIOPAC o Vernier exportado a CSV

Coloque el archivo dentro de:

```text
data/experimental/
```

y ejecute:

```bash
python src/visualizar_csv.py
```

El código se utiliza únicamente como **herramienta de visualización**. La práctica evalúa la interpretación instrumental, la trazabilidad y las mediciones realizadas por el equipo.

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
