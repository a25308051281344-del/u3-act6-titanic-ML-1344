
# ==============================================
# PRACTICA 6: IDENTIFICACION DE PROBLEMAS EN DATOS
# CASO 1: PASAJEROS DEL TITANIC
# Alumno: Hinojos Adrian
# Numero de control: 1344
# Numero de lista: 28
# ==============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==============================================
# 1. CONFIGURAR CARPETAS
# ==============================================

BASE_DIR = Path(__file__).resolve().parent

RUTA_DATOS = BASE_DIR / "caso1-titanic" / "datos" / "titanic.csv"

RUTA_RESULTADOS = BASE_DIR / "caso1-titanic" / "resultados"

RUTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

print("============================================")
print("PRACTICA 6 - ANALISIS DEL TITANIC")
print("Alumno: Hinojos Adrian")
print("NC: 1344")
print("Numero de lista: 28")
print("============================================")

# ==============================================
# 2. IMPORTAR EL DATASET
# ==============================================

if not RUTA_DATOS.exists():
    raise FileNotFoundError(
        "No se encontro el archivo titanic.csv en la carpeta datos."
    )

df = pd.read_csv(RUTA_DATOS)

print("\n===== 1. VISTA PREVIA DE LOS DATOS =====")
print(df.head())

# ==============================================
# 3. IDENTIFICAR DIMENSIONES
# ==============================================

print("\n===== 2. DIMENSIONES DEL DATASET =====")

print("Numero de filas:", df.shape[0])
print("Numero de columnas:", df.shape[1])

# ==============================================
# 4. IDENTIFICAR TIPOS DE DATOS
# ==============================================

print("\n===== 3. TIPOS DE DATOS =====")

print(df.dtypes)

# Revisar si existen datos de edad que no sean numericos

edad_convertida = pd.to_numeric(df["age"], errors="coerce")

errores_tipo = (
    df["age"].notnull() & edad_convertida.isnull()
).sum()

print("\nErrores de tipo detectados en edad:", errores_tipo)

# ==============================================
# 5. IDENTIFICAR DATOS NULOS
# ==============================================

print("\n===== 4. DATOS NULOS =====")

nulos = df.isnull().sum()

print(nulos[nulos > 0])

# ==============================================
# 6. PORCENTAJE DE DATOS NULOS
# ==============================================

print("\n===== 5. PORCENTAJE DE DATOS NULOS =====")

porcentaje = (df.isnull().mean() * 100).round(2)

print(porcentaje[porcentaje > 0])

# ==============================================
# 7. IDENTIFICAR DUPLICADOS
# ==============================================

print("\n===== 6. REGISTROS DUPLICADOS =====")

duplicados = df.duplicated().sum()

print("Cantidad de duplicados:", duplicados)

# ==============================================
# 8. IDENTIFICAR VALORES ATIPICOS
# METODO IQR EN LA EDAD
# ==============================================

print("\n===== 7. VALORES ATIPICOS EN EDAD =====")

edades = edad_convertida.dropna()

Q1 = edades.quantile(0.25)
Q3 = edades.quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

atipicos = edades[
    (edades < limite_inferior) |
    (edades > limite_superior)
]

print("Primer cuartil:", Q1)
print("Tercer cuartil:", Q3)
print("Rango intercuartil:", IQR)

print("Limite inferior:", limite_inferior)
print("Limite superior:", limite_superior)

print("Cantidad de valores atipicos:", len(atipicos))

# ==============================================
# 9. GRAFICA DE DATOS NULOS
# ==============================================

plt.figure(figsize=(12, 5))

sns.heatmap(
    df.isnull(),
    cbar=False,
    cmap="viridis",
    yticklabels=False
)

plt.title("Mapa de calor de datos faltantes - Titanic")
plt.xlabel("Columnas")
plt.ylabel("Pasajeros")

plt.tight_layout()

plt.savefig(
    RUTA_RESULTADOS / "mapa_nulos_titanic.png",
    dpi=150
)

plt.close()

print("\nGrafica de datos nulos guardada.")

# ==============================================
# 10. GRAFICA DE VALORES ATIPICOS
# ==============================================

plt.figure(figsize=(9, 4))

sns.boxplot(x=edades)

plt.title("Valores atipicos en la edad de pasajeros Titanic")
plt.xlabel("Edad")

plt.tight_layout()

plt.savefig(
    RUTA_RESULTADOS / "atipicos_edad_titanic.png",
    dpi=150
)

plt.close()

print("Grafica de valores atipicos guardada.")

# ==============================================
# 11. LIMPIEZA DE LOS DATOS
# ==============================================

print("\n===== 8. LIMPIEZA DEL DATASET =====")

df_limpio = df.copy()

# Eliminar registros duplicados
df_limpio = df_limpio.drop_duplicates()

# Convertir edad a tipo numerico
df_limpio["age"] = pd.to_numeric(
    df_limpio["age"],
    errors="coerce"
)

# Rellenar edades faltantes con la mediana
mediana_edad = df_limpio["age"].median()

df_limpio["age"] = df_limpio["age"].fillna(
    mediana_edad
)

# Rellenar ciudad de embarque con la moda
moda_embarque = df_limpio["embark_town"].mode()

if not moda_embarque.empty:
    df_limpio["embark_town"] = df_limpio[
        "embark_town"
    ].fillna(moda_embarque.iloc[0])

print("Duplicados eliminados.")
print("Edades faltantes rellenadas con la mediana.")
print("Ciudades de embarque faltantes rellenadas con la moda.")

# ==============================================
# 12. GUARDAR DATASET LIMPIO
# ==============================================

RUTA_LIMPIO = (
    RUTA_RESULTADOS / "titanic_limpio_1344.csv"
)

df_limpio.to_csv(RUTA_LIMPIO, index=False)

print("\nDataset limpio guardado correctamente.")

# ==============================================
# 13. GENERAR REPORTE
# ==============================================

RUTA_REPORTE = (
    RUTA_RESULTADOS / "reporte_calidad_titanic_1344.txt"
)

with open(RUTA_REPORTE, "w", encoding="utf-8") as archivo:

    archivo.write("REPORTE DE CALIDAD DE DATOS - TITANIC\n")
    archivo.write("Alumno: Hinojos Adrian\n")
    archivo.write("Numero de control: 1344\n")
    archivo.write("Numero de lista: 28\n\n")

    archivo.write(f"Filas originales: {df.shape[0]}\n")
    archivo.write(f"Columnas originales: {df.shape[1]}\n")
    archivo.write(f"Duplicados encontrados: {duplicados}\n")
    archivo.write(f"Errores de tipo en edad: {errores_tipo}\n")
    archivo.write(f"Valores atipicos en edad: {len(atipicos)}\n\n")

    archivo.write("DATOS NULOS ORIGINALES:\n")
    archivo.write(nulos.to_string())
    archivo.write("\n\n")

    archivo.write("DATOS NULOS DESPUES DE LA LIMPIEZA:\n")
    archivo.write(df_limpio.isnull().sum().to_string())

print("Reporte de calidad generado.")

# ==============================================
# 14. RESULTADOS FINALES
# ==============================================

print("\n===== 9. RESULTADOS FINALES =====")

print("Filas originales:", df.shape[0])
print("Filas despues de limpieza:", df_limpio.shape[0])

print("\nDatos nulos despues de la limpieza:")

print(df_limpio.isnull().sum())

print("\n============================================")
print("PRACTICA TERMINADA CORRECTAMENTE")
print("Alumno: Hinojos Adrian")
print("NC: 1344")
print("Lista: 28")
print("============================================")
