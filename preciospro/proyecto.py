import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import tkinter as tk

#formula de la funcion exponencial

def exponencial(x, a, b):
    return a * np.exp(b * x)

#Modulo para el proceso completo de obtener los precios futuros del producto
def calcular():
#Este modulo sirve para recolectar los datos que el usuario inserta en el programa
   precios = entry_precios.get()

   precios_lista = [float(p) for p in precios.split(",")]

   precios_array = np.array(precios_lista)

   meses_lista = []

   meses = len(precios_array)
   for m in range(meses):
      meses_lista.append(m)
   meses_array = np.array(meses_lista)  

   lista_meses_futuros = []

   meses_futuros = int(entry_meses_futuros.get())
   meses_futuros_lista = [int(m) for m in range(meses, meses + meses_futuros)]
   for i in range(len(meses_futuros_lista)):
      lista_meses_futuros.append(meses_futuros_lista[i])

   meses_futuros_array = np.array(lista_meses_futuros)
#Este modulo sirve para generar las 3 funciones usando los datos que nos dio el usuario(meses y precios)
   parametros_lineal = np.polyfit(meses_array, precios_array, 1)

   parametros_cuadratica = np.polyfit(meses_array, precios_array, 2)

   parametros_exponencial, _ = curve_fit(exponencial, meses_array, precios_array)


#Modulo para hacer las pruebas en x por cada uno de los meses 
#dados en las 3 funciones ya generadas(usando los parametros y )

   funcion_lineal = np.polyval(parametros_lineal, meses_array)
   funcion_cuadratica = np.polyval(parametros_cuadratica, meses_array)
   funcion_exponencial = exponencial(meses_array, parametros_exponencial[0], parametros_exponencial[1])

#Modulo para calcular el r2 de cada funcion

   r1_lineal = r2_score(precios_array, funcion_lineal)
   r2_cuadratica = r2_score(precios_array, funcion_cuadratica)
   r3_exponencial = r2_score(precios_array, funcion_exponencial)

   for widget in ventana.winfo_children():
        if isinstance(widget, tk.Label) and widget != label_precios and widget != label_meses_futuros:
            widget.destroy()
   
#En este modulo lo que hacemos es saber cual fue el coeficiente de determinacion mayor, es decir, saber
#cual funcion encaja mas para predecir los precios futuros

   if r1_lineal > r2_cuadratica and r1_lineal > r3_exponencial:

     print(f"Esta es la funcion lineal: {r1_lineal:.2f}")
     #Este modulo sirve para sustituir los valores en x por los meses futuros que el usuario quiere predecir
     #en la funcion que mas encaja
     precios_futuros = np.polyval(parametros_lineal, meses_futuros_array)
     #Este modulo sirve para mostrar el precio del producto por cada mes futuro dado
     for i in range(len(meses_futuros_array)):
        texto = f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        precios_meses = tk.Label(ventana, text=texto)
        precios_meses.pack()
     plt.scatter(meses_array, precios_array, label="Datos historicos")
     x_curva = np.linspace(0, meses + meses_futuros - 1, 100)
     y_curva = np.polyval(parametros_lineal, x_curva)
     plt.plot(x_curva, y_curva, label="Funcion lineal")

   elif r2_cuadratica > r1_lineal and r2_cuadratica > r3_exponencial:
      print(f"Esta es la funcion cuadratica: {r2_cuadratica:.2f}")
      precios_futuros = np.polyval(parametros_cuadratica, meses_futuros_array)
      for i in range(len(meses_futuros_array)):
        texto = f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        precios_meses = tk.Label(ventana, text=texto)
        precios_meses.pack()
      plt.scatter(meses_array, precios_array, label="Datos historicos")
      x_curva = np.linspace(0, meses + meses_futuros - 1, 100)
      y_curva = np.polyval(parametros_cuadratica, x_curva)
      plt.plot(x_curva, y_curva, label="Funcion cuadratica")
   else:
     print(f"Esta es la funcion exponencial:{r3_exponencial:.2f}")
     precios_futuros = exponencial(meses_futuros_array, parametros_exponencial[0], parametros_exponencial[1])
     for i in range(len(meses_futuros_array)):
        texto = f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        precios_meses = tk.Label(ventana, text=texto)
        precios_meses.pack()
     plt.scatter(meses_array, precios_array, label="Datos historicos")
     x_curva = np.linspace(0, meses + meses_futuros - 1, 100)
     y_curva = exponencial(x_curva, parametros_exponencial[0], parametros_exponencial[1])
     plt.plot(x_curva, y_curva, label="Funcion exponencial")

   plt.title("Prediccion de precios de productos")
   plt.xlabel("Meses")
   plt.ylabel("Precios")
   plt.legend()
   plt.show()


ventana = tk.Tk()
ventana.title("Prediccion de precios futuros")
ventana.geometry("1000x600")

label_precios = tk.Label(ventana, text="INGRESE AQUI LOS PRECIOS ANTERIORES DEL PRODUCTO, SEPARADOS POR COMA!: ")
label_precios.pack()

entry_precios = tk.Entry(ventana, font=("Arial", 11), width=30)
entry_precios.pack()

label_meses_futuros = tk.Label(ventana, text="INGRESE LA CANTIDAD DE MESES QUE DESEA PREDECIR: ")
label_meses_futuros.pack()

entry_meses_futuros = tk.Entry(ventana, font=("Arial", 11), width=30)
entry_meses_futuros.pack()

calcular_boton = tk.Button(ventana, text="CALCULAR", command=calcular)
calcular_boton.pack()

ventana.mainloop()





    


