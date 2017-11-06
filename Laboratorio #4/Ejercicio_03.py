import sqlite3 as SQ
import binascii
import serial
import os
import Tkinter
from PIL import Image,ImageTk

global cont
cont=0
rutas=os.listdir('IMAGENES')

def Crear_Tabla():
    conexion=SQ.connect('db_img/img.db')
    consulta = conexion.cursor()

    MYSQL= ''' CREATE TABLE IF NOT EXISTS
                img
                    (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    im blob
                    );
            '''
    if(consulta.execute(MYSQL)): #execute ejecuta comandos mysql
        print"La tabla se ha creado correctamente"
    else:
        print"Error en creación de tabla"

    consulta.close() #cierre de la consulta
    conexion.commit() #guarda los cambios en la base de datos
    conexion.close() #cierre de conexión con base de datos

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
    
def Base_Datos():
    conexion = SQ.connect('db_img/img.db')
    consulta = conexion.cursor()
    i = Image.open('IMAGENES'+'/'+rutas[cont])
    w,h=i.size
    width=int(w/4)
    height=int(h/4)
    img = i.resize((width, height),Image.ANTIALIAS)
    img.save('tmb'+rutas[cont]+".png")    
    imagen=open('tmb'+rutas[cont]+".png",'rb')
    imagen = imagen.read()
    consulta=consulta.execute("INSERT INTO img(im) VALUES (?)",[SQ.Binary(imagen)])
    conexion.commit()
    print 'Imagen guardada en la Base de Datos'
    conexion.close()

Crear_Tabla()
global img
img = Image.open('Imagenes'+'/'+rutas[cont])
img.thumbnail((500,500),Image.ANTIALIAS)
win = Tkinter.Tk()
win.title('Visualizador Imagenes')
win.geometry('535x460')
imgtk = ImageTk.PhotoImage(img) #Objeto PhotoImage de Tkinter
cuadro = Tkinter.Label(win,image=imgtk,width=500,height=440).place(x=15,y=-50)
btnRetroceder = Tkinter.Button(win,text='Retroceder',command=Retroceder,width=15,height=2,anchor='center').place(x=15,y=400) #crear funcion Retroceder
btnRetroceder = Tkinter.Button(win,text='Avanzar',command=Avanzar,width=15,height=2,anchor='center').place(x=145,y=400)
btnRetroceder = Tkinter.Button(win,text='Insertar',command=Base_Datos,width=15,height=2,anchor='center').place(x=275,y=400)
btnRetroceder = Tkinter.Button(win,text='Salir',command=win.destroy,width=15,height=2,anchor='center').place(x=405,y=400)
win.mainloop()


