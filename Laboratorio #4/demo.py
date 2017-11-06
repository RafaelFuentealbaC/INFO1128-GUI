#-*- coding: utf-8 -*-
import Tkinter, tkMessageBox

def Saludar():
    """Extrae lo que se escribe en el campo de texto
       y lo muestra con un cuadro de diálogo"""
    _nombre=nombre.get()
    tkMessageBox.showinfo("mensaje", "Hola %s"%_nombre)

ventana = Tkinter.Tk()
nombre=Tkinter.StringVar()#almacena los datos que se escriben en caja_texto
etiqueta = Tkinter.Label(ventana, text="Cuál es tu nombre? ")
caja_texto = Tkinter.Entry(ventana, bd =5, textvariable=nombre)
boton=Tkinter.Button(ventana, text="PULSAR", command=Saludar)

etiqueta.grid(row=0, column=0, padx=10, pady=50)
caja_texto.grid(row=0, column=1)
boton.grid(row=0, column=2, padx=10)

ventana.mainloop()
