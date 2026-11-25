
# PRACTICA 6: IDENTIFICACION DE PROBLEMAS EN LOS DATOS

## Datos del alumno

- Alumno: Hinojos Adrian
- Numero de control: 1344
- Numero de lista: 28
- Materia: Machine Learning
- Caso asignado: Titanic
- Tema: Data Cleaning

---

## 1. Objetivo

El objetivo de esta practica es aprender a identificar los problemas mas comunes que existen dentro de un conjunto de datos antes de utilizarlo para entrenar un modelo de Machine Learning.

Se trabaja con el conjunto de datos de los pasajeros del Titanic utilizando Python, Pandas, NumPy, Matplotlib y Seaborn.

## 2. Conceptos principales

### Datos nulos
Son valores que no contienen informacion o que no fueron registrados. Por ejemplo, una edad que aparece vacia.

### Datos duplicados
Son registros que aparecen repetidos dentro del conjunto de datos y pueden afectar los resultados del analisis.

### Tipos de datos incorrectos
Ocurren cuando una columna contiene informacion con un tipo de dato que no corresponde. Por ejemplo, guardar una edad como texto en lugar de numero.

### Valores atipicos
Son valores que se alejan mucho del comportamiento normal de los datos. Por ejemplo, una edad demasiado elevada.

---

## 3. Herramientas utilizadas

- Python: lenguaje de programacion.
- Pandas: lectura y limpieza de datos.
- NumPy: operaciones numericas y manejo de valores nulos.
- Matplotlib: creacion de graficas.
- Seaborn: visualizacion y analisis de datos.

---

## 4. Desarrollo de la practica

Se importo el conjunto de datos del Titanic mediante un archivo CSV.

Se realizaron las siguientes actividades:

1. Importar el conjunto de datos.
2. Mostrar los primeros registros.
3. Identificar filas y columnas.
4. Revisar los tipos de datos.
5. Identificar y contar datos nulos.
6. Calcular el porcentaje de datos faltantes.
7. Identificar registros duplicados.
8. Detectar valores atipicos en la edad mediante el metodo IQR.
9. Crear graficas para visualizar los problemas.
10. Eliminar registros duplicados.
11. Rellenar las edades faltantes utilizando la mediana.
12. Rellenar las ciudades de embarque faltantes utilizando la moda.
13. Guardar una copia del conjunto de datos limpio.

## 5. Resultados

El analisis permite observar que el conjunto de datos del Titanic contiene informacion faltante en diferentes columnas.

La columna de edad contiene valores nulos que pueden corregirse utilizando la mediana. Tambien se revisan las ciudades de embarque y los registros duplicados.

Los valores atipicos se identifican mediante el rango intercuartil (IQR). Estos valores se detectan y se visualizan, pero no se eliminan automaticamente porque primero deben investigarse.

El programa genera los siguientes archivos:

- titanic_limpio_1344.csv
- mapa_nulos_titanic.png
- atipicos_edad_titanic.png
- reporte_calidad_titanic_1344.txt

## 6. Cuestionario

### 1. ¿Que es un dato nulo y por que le molesta a un algoritmo de Machine Learning?

Es un dato que no tiene informacion registrada. Puede causar errores o afectar el entrenamiento de un modelo porque el algoritmo necesita datos completos.

### 2. ¿Que diferencia practica hay entre un dato nulo y un dato duplicado?

Un dato nulo es informacion faltante, mientras que un duplicado es un registro que aparece repetido.

### 3. ¿Que funcion de Pandas nos da un resumen rapido de cuantos nulos hay por columna?

La funcion `df.isnull().sum()` permite contar los valores nulos de cada columna.

### 4. Si df.dtypes muestra que la columna Salario es object en lugar de float, ¿que problema hay?

Significa que los datos estan guardados como texto u objetos en lugar de numeros decimales. Esto puede dificultar las operaciones matematicas.

### 5. ¿Que hace exactamente errors="coerce" dentro de pd.to_numeric()?

Convierte los valores que no pueden interpretarse como numeros en valores nulos (NaN).

### 6. Define con un ejemplo que es un valor atipico (outlier).

Es un valor que se aleja demasiado de los demas. Por ejemplo, una persona que aparece registrada con una edad de 250 años.

### 7. ¿Por que no debemos eliminar automaticamente todos los valores atipicos sin investigarlos primero?

Porque algunos valores extremos pueden ser reales y contener informacion importante. Primero debemos revisar si son errores o datos verdaderos.

---

## 7. Reto final

¿Por que es peligroso dejar el valor 1000 en un modelo de Machine Learning?

Porque es un valor exageradamente alto y puede alterar los calculos estadisticos y provocar que el modelo aprenda patrones incorrectos.

## 8. Conclusion

Con esta practica aprendi que antes de entrenar un modelo de Machine Learning es importante revisar y limpiar los datos.

Tambien aprendi a detectar valores nulos, registros duplicados, tipos de datos incorrectos y valores atipicos utilizando Python y sus librerias.

La limpieza de datos permite obtener informacion mas confiable y mejorar los resultados de los modelos de inteligencia artificial.

---

**Alumno:** Hinojos Adrian  
**Numero de control:** 1344  
**Numero de lista:** 28
