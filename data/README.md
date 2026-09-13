# Datos

Los datos crudos se mantienen localmente y no forman parte del repositorio público.

Estructura local sugerida:

```text
data/
├── physionet/
│   ├── 16265.hea
│   └── 16265.dat
│
└── experimental/
    ├── biopac_equipo03.csv
    └── vernier_equipo03.csv
```

## Registro PhysioNet utilizado

Los datos de referencia se obtienen de:

**MIT-BIH Normal Sinus Rhythm Database v1.0.0**

https://physionet.org/content/nsrdb/1.0.0/

Para el ejemplo de esta práctica se utiliza el registro `16265`.

Descargue:

```text
16265.hea
16265.dat

El `.gitignore` evita que el contenido de `data/` sea incorporado accidentalmente al repositorio.

Los nombres anteriores son únicamente ejemplos. Use identificadores sin datos personales.
