# Estación C — Procedimiento de análisis ECG con PhysioNet

## Objetivo

Aprender el procedimiento que después se aplicará a los registros de BIOPAC y Vernier.

## Datos de PhysioNet

Para esta práctica se utilizará un registro de la **MIT-BIH Normal Sinus Rhythm Database (NSRDB)** de PhysioNet.

Base de datos:

https://physionet.org/content/nsrdb/1.0.0/

El programa está configurado inicialmente para trabajar con el registro:

```text
16265
```

## Actividad

1. Abrir el registro asignado con `src/visualizar_physionet.py`.
2. Anotar:
   - registro;
   - canal;
   - frecuencia de muestreo;
   - unidades.
3. Seleccionar aproximadamente 10 s con:
   - línea basal razonablemente estable;
   - complejos QRS identificables;
   - ausencia de artefactos grandes.
4. Identificar al menos cinco intervalos R–R.
5. Calcular:
   \[
   FC_i = \frac{60}{RR_i}
   \]
6. Obtener RR medio y frecuencia cardíaca media.
7. Medir aproximadamente la amplitud de una onda R representativa.
8. Evaluar:
   - estabilidad de línea basal;
   - claridad del QRS;
   - ruido de alta frecuencia;
   - artefactos.
9. Completar únicamente la columna PhysioNet de la plantilla.

## Producto

Primera versión del reporte comparativo ECG.
