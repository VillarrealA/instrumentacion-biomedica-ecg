# Git en la práctica ECG

## ¿Por qué usar Git?

En una práctica experimental el resultado final no aparece de una sola vez.
El análisis cambia conforme se incorporan nuevas señales, mediciones y correcciones.

Git permite conservar:

- qué cambió;
- cuándo cambió;
- por qué cambió;
- versiones anteriores;
- evolución del análisis.

## Secuencia mínima sugerida

Después de PhysioNet:

```bash
git add .
git commit -m "Agrega análisis del ECG de referencia PhysioNet"
```

Después de BIOPAC:

```bash
git add .
git commit -m "Agrega mediciones del registro BIOPAC"
```

Después de Vernier:

```bash
git add .
git commit -m "Agrega mediciones del registro Vernier"
```

Al terminar:

```bash
git add .
git commit -m "Completa comparación BIOPAC Vernier PhysioNet"
```

Para consultar la historia:

```bash
git log --oneline --graph
```

## Qué sí debe subir el equipo

- reporte comparativo;
- tablas;
- figuras sin información identificable;
- cambios al procedimiento cuando sean necesarios.

## Qué no debe subir a un repositorio público

- nombres de voluntarios;
- datos personales;
- archivos fisiológicos crudos identificables;
- bases completas de PhysioNet.
