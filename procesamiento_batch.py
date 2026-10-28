from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, round as spark_round
from pyspark.sql.types import DoubleType

def main():
    spark = (
        SparkSession.builder
        .appName("Tarea3_Procesamiento_Batch")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    # El archivo CSV debe estar en la carpeta datos/ y tener encabezados.
    ruta = "datos/ventas.csv"
    df = spark.read.option("header", True).option("inferSchema", True).csv(ruta)

    print("\n=== ESQUEMA ORIGINAL ===")
    df.printSchema()
    print("\n=== MUESTRA DE DATOS ===")
    df.show(10, truncate=False)

    print("\n=== LIMPIEZA ===")
    # Elimina filas completamente duplicadas y filas sin datos en ninguna columna.
    limpio = df.dropDuplicates().na.drop(how="all")
    print(f"Filas originales: {df.count()}")
    print(f"Filas después de limpieza básica: {limpio.count()}")

    print("\n=== ANÁLISIS EXPLORATORIO ===")
    limpio.describe().show(truncate=False)

    # Si el CSV contiene las columnas 'categoria' y 'importe',
    # calcula cantidad de registros e importe promedio por categoría.
    columnas = set(limpio.columns)
    if {"categoria", "importe"}.issubset(columnas):
        analisis = (
            limpio.withColumn("importe", col("importe").cast(DoubleType()))
            .groupBy("categoria")
            .agg(
                count("*").alias("cantidad_registros"),
                spark_round(avg("importe"), 2).alias("importe_promedio")
            )
            .orderBy(col("cantidad_registros").desc())
        )
        print("\n=== RESULTADO POR CATEGORÍA ===")
        analisis.show(50, truncate=False)
        analisis.coalesce(1).write.mode("overwrite").option("header", True).csv("resultados/por_categoria")
        print("Resultados guardados en la carpeta resultados/por_categoria")
    else:
        print("\nEl archivo no tiene las columnas 'categoria' e 'importe'.")
        print("Se completó la limpieza y el análisis descriptivo general.")

    spark.stop()

if __name__ == "__main__":
    main()
