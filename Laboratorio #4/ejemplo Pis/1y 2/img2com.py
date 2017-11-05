# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
#   IMPORTACIÓNDE MÓDULOS A USAR
#------------------------------------------------------------------------------
import serial
import os
import pygame

#------------------------------------------------------------------------------
#   FUNCIONES
#------------------------------------------------------------------------------
def enviar_Imagen(i):
    w,h = i.get_size()
    ancho = str(w)
    alto = str(h)
    imagen = pygame.image.tostring(i,'RGB')
    imagen = imagen.replace('\n','okperico')
    cadena = ancho+'listo'+alto+'listo'+imagen+'\n'
    return cadena

#------------------------------------------------------------------------------
#   MAIN PRINCIPAL
#------------------------------------------------------------------------------
conexion = serial.Serial(2,9600)
aImg = os.listdir('Imagenes')
for i in range(len(aImg)):
    img = pygame.image.load('Imagenes/' + aImg[i])
    sImagen = enviar_Imagen(img)
    conexion.write(sImagen)
conexion.close()