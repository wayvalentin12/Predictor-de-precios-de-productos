import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
#Este es el modulo en donde se guardan los datos historicos del usuario
meses = int(input("Ingrese la cantidad de meses que tiene de datos historicos: "))
meses_lista = []
precios_lista = []
for i in range(meses):
    precio_por_mes = float(input(f"ingrese el precio del producto por cada mes {i + 1}: "))
    precios_lista.append(precio_por_mes)
    meses_lista.append(i + 1)

precios_array = np.array(precios_lista)
meses_array = np.array(meses_lista)
print("El array de precios es: ", precios_array)
print("El array de meses es: ", meses_array)

#Modulo para hacer las funciones

parametros_lineal = np.polyfit(meses_array, precios_array, 1)
print(parametros_lineal)
parametros_cuadratica = np.polyfit(meses_array, precios_array, 2)
print(parametros_cuadratica)

def exponencial(x, a, b):
    return a * np.exp(b * x)
parametros_exponencial, _ = curve_fit(exponencial, meses_array, precios_array)
print(parametros_exponencial)

#Modulo para hacer las pruebas en x de las funciones

funcion_lineal = np.polyval(parametros_lineal, meses_array)
funcion_cuadratica = np.polyval(parametros_cuadratica, meses_array)
funcion_exponencial = exponencial(meses_array, parametros_exponencial[0], parametros_exponencial[1])

#Modulo para calcular el r2 de cada funcion

r1_lineal = r2_score(precios_array, funcion_lineal)
r2_cuadratica = r2_score(precios_array, funcion_cuadratica)
r3_exponencial = r2_score(precios_array, funcion_exponencial)

meses_futuros = int(input("Ingrese la cantidad de meses que desea predecir: "))
meses_futuros_lista = []
for i in range(meses_futuros):
    meses_futuros_lista.append(meses + i + 1)
meses_futuros_array = np.array(meses_futuros_lista)

if r1_lineal > r2_cuadratica and r1_lineal > r3_exponencial:
    print(f"Esta es la funcion lineal{r1_lineal:.2f}")
    precios_futuros = np.polyval(parametros_lineal, meses_futuros_array)
    for i in range(meses_futuros):
        print(f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f}")
    
    plt.scatter(meses_array, precios_array, label="Datos historicos")
    x_curva = np.linspace(1, meses + meses_futuros, 100)
    y_curva = np.polyval(parametros_lineal, x_curva)
    plt.plot(x_curva, y_curva, label="Funcion lineal")

elif r2_cuadratica > r1_lineal and r2_cuadratica > r3_exponencial:
      print(f"Esta es la funcion cuadratica{r2_cuadratica:.2f}")
      precios_futuros = np.polyval(parametros_cuadratica, meses_futuros_array)
      for i in range(meses_futuros):
          print(f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f}")
      plt.scatter(meses_array, precios_array, label="Datos historicos")
      x_curva = np.linspace(1, meses + meses_futuros, 100)
      y_curva = np.polyval(parametros_cuadratica, x_curva)
      plt.plot(x_curva, y_curva, label="Funcion cuadratica")
else:
     print(f"Esta es la funcion exponencial{r3_exponencial:.2f}")
     precios_futuros = exponencial(meses_futuros_array, parametros_exponencial[0], parametros_exponencial[1])
     for i in range(meses_futuros):
         print(f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f}")
     plt.scatter(meses_array, precios_array, label="Datos historicos")
     x_curva = np.linspace(1, meses + meses_futuros, 100)
     y_curva = exponencial(x_curva, parametros_exponencial[0], parametros_exponencial[1])
     plt.plot(x_curva, y_curva, label="Funcion exponencial")

plt.title("Prediccion de precios de productos")
plt.xlabel("Meses")
plt.ylabel("Precios")
plt.legend()
plt.show()





    


