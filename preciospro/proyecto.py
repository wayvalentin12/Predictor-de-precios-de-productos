import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import tkinter as tk



def exponencial(x, a, b):
    return a * np.exp(b * x)


def calcular():

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

   parametros_lineal = np.polyfit(meses_array, precios_array, 1)

   parametros_cuadratica = np.polyfit(meses_array, precios_array, 2)

   parametros_exponencial, _ = curve_fit(exponencial, meses_array, precios_array)




   funcion_lineal = np.polyval(parametros_lineal, meses_array)
   funcion_cuadratica = np.polyval(parametros_cuadratica, meses_array)
   funcion_exponencial = exponencial(meses_array, parametros_exponencial[0], parametros_exponencial[1])



   r1_lineal = r2_score(precios_array, funcion_lineal)
   r2_cuadratica = r2_score(precios_array, funcion_cuadratica)
   r3_exponencial = r2_score(precios_array, funcion_exponencial)

   for widget in ventana.winfo_children():
        if isinstance(widget, tk.Label) and widget != label_precios and widget != label_meses_futuros:
            widget.destroy()
   


   if r1_lineal >= r2_cuadratica and r1_lineal >= r3_exponencial:

     funcion = tk.Label(ventana, text=f"La funcion lineal es la que mas encaja, valor R2: {r1_lineal:.2f}")
     funcion.pack()
     
     precios_futuros = np.polyval(parametros_lineal, meses_futuros_array)
    
     for i in range(len(meses_futuros_array)):
        texto = f"El precio del producto en el mes {meses_futuros_array[i]} es: {precios_futuros[i]:.2f} (PREDICCIÓN)"
        precios_meses = tk.Label(ventana, text=texto)
        precios_meses.pack()
     plt.scatter(meses_array, precios_array, label="Datos historicos")
     x_curva = np.linspace(0, meses + meses_futuros - 1, 100)
     y_curva = np.polyval(parametros_lineal, x_curva)
     plt.plot(x_curva, y_curva, label="Funcion lineal")

   elif r2_cuadratica >= r1_lineal and r2_cuadratica >= r3_exponencial:
      funcion = tk.Label(ventana, text=f"La funcion cuadratica es la que mas encaja, valor R2: {r2_cuadratica:.2f}")
      funcion.pack()
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
     funcion = tk.Label(ventana, text=f"La funcion exponencial es la que mas encaja, valor R2 {r3_exponencial:.2f}")
     funcion.pack()
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





    


