# Práctica ECG — BIOPAC, Vernier y PhysioNet

## Propósito

Aplicar un mismo procedimiento de documentación y análisis a tres fuentes de señal ECG.

## Estaciones

- **A — BIOPAC:** adquisición experimental.
- **B — Vernier:** adquisición experimental con un segundo sistema.
- **C — PhysioNet:** aprendizaje inicial del procedimiento de análisis sobre un registro de referencia.

## Procedimiento común

Para cada fuente:

1. Documentar el origen del registro.
2. Anotar el montaje o derivación.
3. Anotar frecuencia de muestreo y unidades.
4. Seleccionar un segmento de aproximadamente 10 s con calidad aceptable.
5. Identificar al menos cinco intervalos R–R.
6. Calcular:
   \[
   FC_i = \frac{60}{RR_i}
   \]
7. Obtener RR promedio y frecuencia cardíaca promedio.
8. Medir aproximadamente la amplitud de una onda R representativa.
9. Evaluar estabilidad de línea basal, ruido de alta frecuencia y artefactos.
10. Comparar los tres registros justificando las diferencias desde el punto de vista instrumental.

## Importante

PhysioNet corresponde a otro sujeto. Por tanto, no se espera que la frecuencia cardíaca o la amplitud coincidan con BIOPAC y Vernier.

Una diferencia entre dos registros no significa automáticamente que uno esté mal. Debe revisarse qué cambió: sujeto, derivación, colocación de electrodos, filtros, escala, frecuencia de muestreo o cadena de adquisición.
