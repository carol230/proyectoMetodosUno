import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from PIL import Image, ImageTk
def f(v0, vf, n, a):
    def funcion(x):
        if abs(x) < 1e-10:
            return vf - v0 * (1 + x) ** n
        else:
            return vf - v0 * (1 + x) ** n - a * (((1 + x) ** n - (1 + x)) / x)

    return funcion
def obtener_interes():
    return optimize.newton(f(100, 105.31, 2, 5), 1e-5)
def graficar():
    try:
        x_min = float(entry_x_min.get())
        x_max = float(entry_x_max.get())
        x_vals = np.linspace(x_min, x_max, 500)
        funcion = f(100, 105.31, 2, 5)
        y_vals = [funcion(x) for x in x_vals]
        raiz = obtener_interes()
        y_raiz = funcion(raiz)  # Debería ser cercano a 0
        plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label='f(x)', color='blue')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.plot(raiz, y_raiz, 'ro', label='Raíz')
        plt.title("Gráfica de la función f(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.savefig("grafica_funcion.png")
        plt.close()
        imagen = Image.open("grafica_funcion.png")
        imagen_tk = ImageTk.PhotoImage(imagen)
        etiqueta_imagen.config(image=imagen_tk)
        etiqueta_imagen.image = imagen_tk
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para los límites de x.")
root = tk.Tk()
root.title("Gráfica de la Función f(x)")
frame_rango_x = ttk.Frame(root)
frame_rango_x.pack(pady=5)
ttk.Label(frame_rango_x, text="x mínimo:").grid(row=0, column=0)
entry_x_min = ttk.Entry(frame_rango_x, width=10)
entry_x_min.insert(0, "-0.1")  # Valor predeterminado
entry_x_min.grid(row=0, column=1)
ttk.Label(frame_rango_x, text="x máximo:").grid(row=0, column=2)
entry_x_max = ttk.Entry(frame_rango_x, width=10)
entry_x_max.insert(0, "0.1")  # Valor predeterminado
entry_x_max.grid(row=0, column=3)
boton_graficar = ttk.Button(root, text="Graficar", command=graficar)
boton_graficar.pack()
interes_label = ttk.Label(root, text=f"Interés obtenido: {obtener_interes():.5f}")
interes_label.pack()
etiqueta_imagen = ttk.Label(root)
etiqueta_imagen.pack()
root.mainloop()
