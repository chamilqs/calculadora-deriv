#!/usr/bin/env python
# coding: utf-8

# In[15]:


get_ipython().system('pip install sympy')


# In[2]:


from sympy import symbols, diff, limit, SympifyError
from sympy.parsing.sympy_parser import parse_expr
from tkinter import *
from tkinter import ttk

def derivada():
    try:
        x = symbols('x')  # Declarar variable independiente
        funcion_simbolica = parse_expr(funcion.get())
        derivada_simbolica = diff(funcion_simbolica, x)
        etiqueta1.configure(text=derivada_simbolica)
    except SympifyError:
        etiqueta1.configure(text="Introduce la función correctamente")

def calcular_limite():
    try:
        x = symbols('x')
        funcion_simbolica = parse_expr(funcion2.get())

        if funcion_simbolica == "":
            raise ValueError("El campo de función está vacío")

        limite_escrito = limite_entry.get()

        if limite_escrito == "":
            raise ValueError("El campo de límite está vacío")

        if limite_escrito.lower() == 'infinito':
            limite = oo
        else:
            limite = parse_expr(limite_escrito)

        resultado = limit(funcion_simbolica, x, limite)
        etiqueta2.configure(text=resultado)
    except (SympifyError, TypeError, ValueError):
        etiqueta2.configure(text="Introduce una función válida")

ventana = Tk()
ventana.geometry('450x480')
ventana.title("Calculadora de Derivadas y Límites")

# Pestañas
pestañas = ttk.Notebook(ventana)

# Pestaña de calculadora de derivadas
pestana_derivadas = ttk.Frame(pestañas)
pestañas.add(pestana_derivadas, text="Derivadas")

espacio_vacio1 = Label(pestana_derivadas, text=" ", font=("Arial", 15))
espacio_vacio1.pack()

anuncio1 = Label(pestana_derivadas, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio1.pack()

funcion = Entry(pestana_derivadas, font=("Arial", 15))
funcion.pack()

etiqueta1 = Label(pestana_derivadas, text="Resultado", font=("Arial", 15), fg="red")
etiqueta1.pack()

boton1 = Button(pestana_derivadas, text="Derivar Función", font=("Arial", 15), command=derivada)
boton1.pack()

# Pestaña de calculadora de límites
pestana_limites = ttk.Frame(pestañas)
pestañas.add(pestana_limites, text="Límites")

espacio_vacio2 = Label(pestana_limites, text=" ", font=("Arial", 15))
espacio_vacio2.pack()

anuncio2 = Label(pestana_limites, text="Introduce una función de x:", font=("Arial", 15), fg="blue")
anuncio2.pack()

funcion2 = Entry(pestana_limites, font=("Arial", 15))
funcion2.pack()

anuncio3 = Label(pestana_limites, text="Introduce hacia qué número tiende la función:", font=("Arial", 15), fg="blue")
anuncio3.pack()

limite_entry = Entry(pestana_limites, font=("Arial", 15))
limite_entry.pack()

etiqueta2 = Label(pestana_limites, text="Resultado", font=("Arial", 15), fg="red")
etiqueta2.pack()

boton2 = Button(pestana_limites, text="Calcular Límite", font=("Arial", 15), command=calcular_limite)
boton2.pack(pady=20)

# NombreDev
devName = Label(pestana_derivadas, text="Dev: Samil Q.", font=("Arial", 15), fg="red")
devName.pack(side="bottom", fill="x")

devName = Label(pestana_limites, text="Dev: Samil Q.", font=("Arial", 15), fg="red")
devName.pack(side="bottom", fill="x")

# Agregar pestañas a la ventana principal
pestañas.pack(expand=1, fill="both")

def _quit():  # Función salir
    ventana.quit()  # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria

# Botón de salir
button4 = Button(master=ventana, text="Salir", 
                 font=("Arial", 15), command=_quit)
button4.pack(side="top", pady=10)

ventana.mainloop()


# In[ ]:




