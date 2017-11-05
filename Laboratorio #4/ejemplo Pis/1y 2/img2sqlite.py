# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   IMPORTACIÓN DE MÓDULOS A USAR
#------------------------------------------------------------------------------
import sqlite3 as SQ
import serial
import pygame
import binascii
import time
from PIL import Image

#------------------------------------------------------------------------------
#   FUNCIONES
#------------------------------------------------------------------------------
'''
def pinta_Rojo(i,cont):
    i.fill((255,0,0))
    rojo = pygame.image.tostring(i,'RGB')
    pygame.image.save(img,'fotos/rojo/a'+str(cont)+'.png')
    bRojo = bin(int(binascii.hexlify(rojo),16))
    return bRojo

def pinta_Verde(i,cont):
    i.fill((0,255,0))
    verde = pygame.image.tostring(i,'RGB')
    pygame.image.save(img,'fotos/verde/a'+str(cont)+'.png')
    bVerde = bin(int(binascii.hexlify(verde),16))
    return bVerde

def pinta_Azul(i,cont):
    i.fill((0,0,255))
    azul = pygame.image.tostring(i,'RGB')
    pygame.image.save(img,'fotos/azul/a'+str(cont)+'.png')
    bAzul = bin(int(binascii.hexlify(azul),16))
    return bAzul

def pinta_Gris(i,cont):
    i.fill((128,128,128))
    gris = pygame.image.tostring(i,'RGB')
    pygame.image.save(img,'fotos/gris/a'+str(cont)+'.png')
    bGris = bin(int(binascii.hexlify(gris),16))
    return bGris
'''

def pinta_RGB(img):
    w,h = img.size
    aImg = []
    imgr = Image.new('RGB',(w,h),'white')
    imgg = Image.new('RGB',(w,h),'white')
    imgb = Image.new('RGB',(w,h),'white')
    for i in range(w):
        for j in range(h):
            r, g ,b = img.getpixel((i,j))
            imgr.putpixel((i,j),(r,0,0))
            imgg.putpixel((i,j),(0,g,0))
            imgb.putpixel((i,j),(0,0,b))
    aImg.append(imgr)
    aImg.append(imgg)
    aImg.append(imgb)
    aImg.append(img.convert('L'))
    return aImg

#------------------------------------------------------------------------------
#   CONEXIÓN CON BASE DE DATOS Y CREACIÓN DE TABLA
#------------------------------------------------------------------------------
conexion = SQ.connect('BD PIS/Imagenes.db') #selecciono la carpeta que contiene a la base de datos y el nombre de mi base de datos
consulta = conexion.cursor() #establesco la conexión y uso el método cursor
MYSQL= ''' CREATE TABLE IF NOT EXISTS
            Fotos
                (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha date,
                hora time,
                img blob,
                r blob,
                g blob,
                b blob,
                gris blob
                );
        '''
if(consulta.execute(MYSQL)): #execute ejecuta comandos mysql
    print"La tabla se ha creado correctamente"
else:
    print"Error en creación de tabla"

consulta.close() #cierre de la consulta
conexion.commit() #guarda los cambios en la base de datos
conexion.close() #cierre de conexión con base de datos

#------------------------------------------------------------------------------
#   CONEXIÓN SERIAL
#------------------------------------------------------------------------------
con = serial.Serial(2,9600)
print"conexion realizada"
#------------------------------------------------------------------------------
#   INSERTAR DATOS EN LA TABLA CREADA
#------------------------------------------------------------------------------
conexion = SQ.connect('BD PIS/Imagenes.db')
consulta = conexion.cursor()
cont=1
while 1:
    sFecha = time.strftime("%d/%m/%y")
    sHora = time.strftime("%H:%M:%S")
    d = con.readline()[:-1].split('listo')

    imagen = d[2].replace('okperico','\n')
    w = d[0]
    h = d[1]
    ancho = int(w)
    alto = int(h)

    #img = Image.fromstring('RGB',(ancho,alto),imagen)
    img = pygame.image.fromstring(imagen,(ancho,alto),'RGB')
    pygame.image.save(img,'fotos/img/a'+str(cont)+'.png')

    im = Image.open('fotos/img/a'+str(cont)+'.png')
    aImg = pinta_RGB(im)

    aImg[0].show()
    aImg[0].save('fotos/rojo/a'+str(cont)+'.png')
    aImg[1].save('fotos/verde/a'+str(cont)+'.png')
    aImg[2].save('fotos/azul/a'+str(cont)+'.png')
    aImg[3].save('fotos/gris/a'+str(cont)+'.png')


    i = open('fotos/img/a'+str(cont)+'.png','rb')
    cimagen = i.read()
    cimagen.show()
    red = open('fotos/rojo/a'+str(cont)+'.png','rb')
    cred = red.read()
    green = open('fotos/verde/a'+str(cont)+'.png','rb')
    cgreen = green.read()
    blue = open('fotos/azul/a'+str(cont)+'.png','rb')
    cblue = blue.read()
    gray = open('fotos/gris/a'+str(cont)+'.png','rb')
    cgray = gray.read()



    consulta.execute("INSERT INTO Fotos(fecha,hora,img,r,g,b,gris) VALUES (?,?,?,?,?,?,?)",[sFecha,sHora,SQ.Binary(cimagen),SQ.Binary(cred),SQ.Binary(cgreen),SQ.Binary(cblue),SQ.Binary(cgray)])
    cont+=1
    conexion.commit() #guarda los cambios en la base de datos
    print "fotos recibidas"
conexion.close() #cierra la conexión a la base de datos
con.close() #cierra la conexión serial
