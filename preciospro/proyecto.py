import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score




def calcular(precios, meses_futuros):
    
   def exponencial(x, a, b):
       return a * np.exp(b * x)

   precios_lista = [float(p) for p in precios.split(",")]

   precios_array = np.array(precios_lista)

   meses_lista = []

   meses = len(precios_array)
   for m in range(meses):
      meses_lista.append(m)
   meses_array = np.array(meses_lista)  

   lista_meses_futuros = []

   meses_futuros_lista = [int(m) for m in range(meses, meses + meses_futuros)]
   for i in range(len(meses_futuros_lista)):
      lista_meses_futuros.append(meses_futuros_lista[i])

   meses_futuros_array = np.array(lista_meses_futuros)

   parametros_lineal = np.polyfit(meses_array, precios_array, 1)

   parametros_cuadratica = np.polyfit(meses_array, precios_array, 2)

   parametros_exponencial, _ = curve_fit(exponencial, meses_array, precios_array)




   funcion_lineal = np.polyval(parametros_lineal, meses_array)
   funcion_cuadratica = np.polyval(parametros_cuadratica, meses_array)
   funcion_exponencial = exponencial(meses_array, parametros_exponencial[0], parametros_exponencial[1])



   r1_lineal = r2_score(precios_array, funcion_lineal)
   r2_cuadratica = r2_score(precios_array, funcion_cuadratica)
   r3_exponencial = r2_score(precios_array, funcion_exponencial)


   if r1_lineal >= r2_cuadratica and r1_lineal >= r3_exponencial:
          
     precios_futuros = np.polyval(parametros_lineal, meses_futuros_array)
     lista_precios_futuros = []
     for i in range(len(meses_futuros_array)):
        texto = f"(Funcion lineal)El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        lista_precios_futuros.append(texto)
     return lista_precios_futuros
    

   elif r2_cuadratica >= r1_lineal and r2_cuadratica >= r3_exponencial:
      
      precios_futuros = np.polyval(parametros_cuadratica, meses_futuros_array)
      lista_precios_futuros = []
      for i in range(len(meses_futuros_array)):
        texto = f"(Funcion cuadratica) El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        lista_precios_futuros.append(texto)
      return lista_precios_futuros
        

   else:
     precios_futuros = exponencial(meses_futuros_array, parametros_exponencial[0], parametros_exponencial[1])
     lista_precios_futuros = []
     for i in range(len(meses_futuros_array)):
        texto = f"(Funcion exponencial)El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        lista_precios_futuros.append(texto)
     return lista_precios_futuros
     

calcular("100,150,200,250,300", 3)






    


