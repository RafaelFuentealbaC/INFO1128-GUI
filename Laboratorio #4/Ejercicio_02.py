from PIL import Image, ImageTk
import Tkinter
import os

global cont

cont=0
rutas=os.listdir('IMAGENES')
print rutas[0]

def Retroceder():
    print 'Retroceder'

def Avanzar():
    global cont
    cont+=1
    img = Image.open(rutas[cont])
    img.thumbnail((500,500),Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    return imgtk
    
def Gris():
    print 'Gris'

def Salir():
    print 'Salir'


img = Image.open(rutas[0])
img.thumbnail((500,500),Image.ANTIALIAS)

win = Tkinter.Tk()
win.title('Visualizador Imagenes')
win.geometry('535x460')
imgtk = ImageTk.PhotoImage(img) #Objeto PhotoImage de Tkinter
cuadro = Tkinter.Label(win,image=Avanzar(),width=500,height=500).place(x=15,y=-50)
btnRetroceder = Tkinter.Button(win,text='Retroceder',command=Retroceder,width=15,height=2,anchor='center').place(x=15,y=400) #crear funcion Retroceder
btnRetroceder = Tkinter.Button(win,text='Avanzar',command=Avanzar,width=15,height=2,anchor='center').place(x=145,y=400)
btnRetroceder = Tkinter.Button(win,text='Gris',command=Gris,width=15,height=2,anchor='center').place(x=275,y=400)
btnRetroceder = Tkinter.Button(win,text='Salir',command=Salir,width=15,height=2,anchor='center').place(x=405,y=400)
win.mainloop()

