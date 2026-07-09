import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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








    


