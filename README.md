# Tarea 3: Procesamiento de datos con Apache Spark

## Descripción
Este proyecto es una plantilla de procesamiento por lotes (Batch) con PySpark. Lee un archivo CSV, muestra su esquema y una muestra de los datos, elimina duplicados, realiza un análisis descriptivo y, cuando existen las columnas `categoria` e `importe`, calcula estadísticas por categoría.

> **Importante:** `datos/ventas.csv` es un archivo pequeño de ejemplo para probar la estructura. Para la entrega académica, reemplázalo por el conjunto de datos público que selecciones y describe en el informe su fuente original, problema y pertinencia. No presentes el archivo de ejemplo como un conjunto de datos grande real.

## Estructura
- `procesamiento_batch.py`: código PySpark.
- `datos/ventas.csv`: datos pequeños de ejemplo para una prueba inicial.
- `requirements.txt`: dependencias de Python para el entorno donde corresponda.
- `INSTRUCCIONES.md`: pasos de ejecución.

## Requisitos
- Python 3
- Apache Spark instalado y configurado
- Java compatible con la versión de Spark
- `spark-submit` disponible en la terminal

## Ejecución
Desde la carpeta del proyecto, ejecuta:

```bash
spark-submit procesamiento_batch.py
```

El programa lee `datos/ventas.csv`. Si cambias el conjunto de datos, actualiza la ruta en la variable `ruta` del código. Para el análisis por categoría, el CSV debe incluir las columnas `categoria` e `importe`; si tus columnas tienen otros nombres, adapta esa parte del código.

## Resultados
El programa muestra en la terminal el esquema, una muestra, conteos antes y después de la limpieza y estadísticas descriptivas. Si encuentra `categoria` e `importe`, guarda el análisis agregado en `resultados/por_categoria`.

## Fuente de datos
El CSV incluido es solo de ejemplo creado para comprobar el funcionamiento inicial. Agrega aquí la URL y la referencia del conjunto de datos público que utilices en la versión final.
