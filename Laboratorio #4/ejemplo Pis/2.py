# -*- coding: utf-8 -*-
import sqlite3,os
from cStringIO import StringIO
import Tkinter as tk
from Tkinter import *
from PIL import Image,ImageTk,ImageOps

var=1

nMAX=500
nMIN=500
cont=1

def nextt():
    f_size = (100,100)
    global cont
    cont=cont+1
    if (cont<=29):
        con=sqlite3.connect('BD PIS/Imagenes.db')
        cur=con.cursor()
        consulta="Select img,r,g,b,gris FROM fotos where id="+(str(cont))
        eje=cur.execute(consulta)
        eje=eje.fetchone()
        v=eje[0]
        w=eje[1]
        x=eje[2]
        y=eje[3]
        z=eje[4]
        a=[]
        Img = []
        a.append(StringIO(v))
        a.append(StringIO(w))
        a.append(StringIO(x))
        a.append(StringIO(y))
        a.append(StringIO(z))
        for i in range(5):
            a[i]=Image.open(a[i])
            a[i]=a[i].resize((100, 100))
        a.append(ImageOps.invert(a[0]))
        for j in range(len(a)):
            Img.append(ImageTk.PhotoImage(a[j]))
        canvas0.create_image(f_size[0]/2, f_size[1]/2,image=Img[0], tags="img")
        canvas1.create_image(f_size[0]/2, f_size[1]/2,image=Img[4], tags="img")
        canvas2.create_image(f_size[0]/2, f_size[1]/2,image=Img[5], tags="img")
        canvas3.create_image(f_size[0]/2, f_size[1]/2,image=Img[1], tags="img")
        canvas4.create_image(f_size[0]/2, f_size[1]/2,image=Img[2], tags="img")
        canvas5.create_image(f_size[0]/2, f_size[1]/2,image=Img[3], tags="img")
        canvas7.create_image(f_size[0]/2, f_size[1]/2,image=Img[5], tags="img")
        print cont
        #normal(cont)
    #img=ImageTk.PhotoImage(x)
    #canvas.create_image(f_size[0]/2, f_size[1]/2, image=img, tags="img")
def previus():
    f_size = (100,100)
    global cont
    cont=cont-1
    if (cont<=29):
        con=sqlite3.connect('BD PIS/Imagenes.db')
        cur=con.cursor()
        consulta="Select img,r,g,b,gris FROM fotos where id="+(str(cont))
        eje=cur.execute(consulta)
        eje=eje.fetchone()
        v=eje[0]
        w=eje[1]
        x=eje[2]
        y=eje[3]
        z=eje[4]
        a=[]
        Img = []
        a.append(StringIO(v))
        a.append(StringIO(w))
        a.append(StringIO(x))
        a.append(StringIO(y))
        a.append(StringIO(z))
        for i in range(5):
            a[i]=Image.open(a[i])
            a[i]=a[i].resize((100, 100), Image.ANTIALIAS)
        a.append(ImageOps.invert(a[0]))
        for j in range(len(a)):
            Img.append(ImageTk.PhotoImage(a[j]))
        canvas0.create_image(f_size[0]/2, f_size[1]/2,image=Img[0], tags="img")
        canvas1.create_image(f_size[0]/2, f_size[1]/2,image=Img[4], tags="img")
        canvas2.create_image(f_size[0]/2, f_size[1]/2,image=Img[5], tags="img")
        canvas3.create_image(f_size[0]/2, f_size[1]/2,image=Img[1], tags="img")
        canvas4.create_image(f_size[0]/2, f_size[1]/2,image=Img[2], tags="img")
        canvas5.create_image(f_size[0]/2, f_size[1]/2,image=Img[3], tags="img")
        canvas7.create_image(f_size[0]/2, f_size[1]/2,image=Img[5], tags="img")
        print cont




root=Tk()
root.geometry("530x450")
root.title("Ejemplo de Imagenes")
con=sqlite3.connect('BD PIS/Imagenes.db')
cur=con.cursor()
consulta="Select img,r,g,b,gris FROM fotos where id="+(str(1))
eje=cur.execute(consulta)
eje=eje.fetchone()

v=eje[0]
w=eje[1]
x=eje[2]
y=eje[3]
z=eje[4]
a=[]
Img = []
a.append(StringIO(v))
a.append(StringIO(w))
a.append(StringIO(x))
a.append(StringIO(y))
a.append(StringIO(z))
img1=Image.open(a[0])
img2=Image.open(a[1])
img3=Image.open(a[2])
img4=Image.open(a[3])
img5=Image.open(a[4])
img6=ImageOps.invert(img1)

f_size=(100,100)

rImg1= img1.resize((100, 100), Image.ANTIALIAS)
rImg1 = ImageTk.PhotoImage(rImg1)

#-----------------2----------------------------------


rImg2= img2.resize((100, 100), Image.ANTIALIAS)
rImg2 = ImageTk.PhotoImage(rImg2)
#--------------3----------------------------


rImg3= img3.resize((100, 100), Image.ANTIALIAS)
rImg3 = ImageTk.PhotoImage(rImg3)
#----------------------4---------------------


rImg4= img4.resize((100, 100), Image.ANTIALIAS)
rImg4 = ImageTk.PhotoImage(rImg4)
#-------------------------5------------------


rImg5= img5.resize((100, 100), Image.ANTIALIAS)
rImg5 = ImageTk.PhotoImage(rImg5)


rImg6= img6.resize((100, 100), Image.ANTIALIAS)
rImg6 = ImageTk.PhotoImage(rImg6)



canvas0 = tk.Canvas(root, width=100, height=100)
canvas0.create_image(50, 50, image=rImg1, tags="img")
canvas0.place(x=0,y=0)


canvas1 = tk.Canvas(root, width=100, height=100)
canvas1.create_image(50,50, image=rImg5, tags="img")
canvas1.place(x=150,y=0)


canvas2 = tk.Canvas(root, width=100, height=100)
canvas2.create_image(50, 50,image=rImg6, tags="img")
canvas2.place(x=300,y=0)


canvas3 = tk.Canvas(root, width=100, height=100)
canvas3.create_image(50, 50,image=rImg2, tags="img")
canvas3.place(x=0,y=150)


canvas4 = tk.Canvas(root, width=100, height=100)
canvas4.create_image(50, 50,image=rImg3, tags="img")
canvas4.place(x=150,y=150)

canvas5 = tk.Canvas(root, width=100, height=100)
canvas5.create_image(50, 50,image=rImg4, tags="img")
canvas5.place(x=300,y=150)




b1 =Button(root,text="siguiente",command=nextt)
b1.place(x=250,y=400)

b2 =Button(root,text="anterior",command=previus)
b2.place(x=350,y=400)

b3 =Button(root,text="Cerrar",command=root.destroy)
b3.place(x=450, y=400)


root.mainloop()


