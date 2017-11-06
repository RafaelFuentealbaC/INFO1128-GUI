from PIL import Image, ImageTk
import Tkinter
import os

global cont
cont=0
rutas=os.listdir('IMAGENES')

def Retroceder():
    global cont
    cont-=1
    if cont<1:
        cont=len(rutas)-1
    Carga_Img(cont)
    
def Avanzar():
    global cont
    cont+=1
    if cont>len(rutas)-1:
        cont=0
    Carga_Img(cont)
    

def Carga_Img(cont):
    img=Image.open('IMAGENES'+'/'+rutas[cont])
    img.thumbnail((500,500),Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(img)
    Tkinter.Label(win,image=imgtk,width=500,height=460).place(x=15,y=-50)
    win.mainloop()
    
def Gris():
    img=Image.open('IMAGENES'+'/'+rutas[cont])
    img.thumbnail((500,500),Image.ANTIALIAS)
    img=img.convert('L')
    img.save('NuevasIMG/PNG/'+rutas[cont]+'_gray'+".PNG")
    img.save('NuevasIMG/BMP/'+rutas[cont]+'_gray'+".BMP")
    imgtk = ImageTk.PhotoImage(img)
    Tkinter.Label(win,image=imgtk,width=500,height=460).place(x=15,y=-50)
    win.mainloop()
    
global img
img = Image.open('IMAGENES'+'/'+rutas[cont])
img.thumbnail((500,500),Image.ANTIALIAS)
win = Tkinter.Tk()
win.title('Visualizador Imagenes')
win.geometry('535x460')
imgtk = ImageTk.PhotoImage(img) #Objeto PhotoImage de Tkinter
cuadro = Tkinter.Label(win,image=imgtk,width=500,height=440).place(x=15,y=-50)
btnRetroceder = Tkinter.Button(win,text='Retroceder',command=Retroceder,width=15,height=2,anchor='center').place(x=15,y=400)
btnRetroceder = Tkinter.Button(win,text='Avanzar',command=Avanzar,width=15,height=2,anchor='center').place(x=145,y=400)
btnRetroceder = Tkinter.Button(win,text='Gris',command=Gris,width=15,height=2,anchor='center').place(x=275,y=400)
btnRetroceder = Tkinter.Button(win,text='Salir',command=win.destroy,width=15,height=2,anchor='center').place(x=405,y=400)
win.mainloop()

