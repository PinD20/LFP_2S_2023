from tkinter import *
from tkinter import ttk

raiz = Tk()

def funcion_boton():
    #Obtiene todo el texto del text_area
    entrada = text_area.get("1.0", "end-1c")

    #Insertar al final del text_area que funciona como consola
    #Se agrega un salto de línea para que no quede en la misma línea el siguiente texto
    consola.insert("end-1c", entrada + "\n")

def obtener_texto_combobox():
    seleccionado = combobox_t.get()
    print(seleccionado)


etq = Label(raiz, text="Mi primera etiqueta")
etq.pack() #Se coloca automáticamente en centro de la pantalla

#etq.grid(column=0, row=0)

combobox_t = ttk.Combobox(state="readonly", values=["Opción 1", "Opción 2", "Opción 3"])
combobox_t.place(x=100,y=100) #Posicionar en coordenada específica

boton = Button(raiz, text="Mostrar opción en consola python", command=obtener_texto_combobox)
boton.place(x=400, y=100)

#Área para escribir código
text_area = Text(raiz, height=15, width=40)
text_area.place(x=100, y=150)

#Igual al anterior pero puede ser utilizado como consola para mostrar resultados
consola = Text(raiz, height=15, width=40)
consola.place(x=500, y=150)

boton = Button(raiz, text="Mostrar texto en 'consola'", command=funcion_boton)
boton.place(x=400, y=450)

#Tamaño de la ventana - ancho x alto
raiz.geometry("900x500")
#Título de la ventana
raiz.title("LFP")

#raiz.minsize(width=900, height=500)
#raiz.maxsize(width=1920, height=1080)
raiz.mainloop()
