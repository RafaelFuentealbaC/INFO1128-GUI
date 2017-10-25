from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np
import sys, pygame
from pygame.locals import *
import pygame.font

#-- Dimension Pantalla Pygame -- 
WIDTH = 636
HEIGHT = 237

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
def mensaje_pantalla(text):
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    mensaje = fuente.render(text, 1,(255, 255, 255),(0,0,0))
    ventana.blit(mensaje,(319,0))
    #pygame.display.flip()

def temp(color):
    temp=(color*0.034)+17.1
    temp="{0:.2f}".format(temp)
    return temp

def Colores_barra(img,aColores):
        for y in range(27,208):
            color=img.getpixel((305,y))
            aColores.append(color)

def Colores_img(img,aClr):
    for x in range(0,302):
        for y in range(0,237):
            color=img.getpixel((x,y))
            aClr.append(color)
    
def colores_pix2barra(x,y):
    color=img.getpixel((x,y))
    if color in aColores:
        t=str(temp(color))+'°C'
    else:
        if color+1 in aColores or color -1 in aColores:
            t=str(temp(color))+'°C'
        else:
            if color+2 in aColores or color -2 in aColores:
                t=str(temp(color))+'°C'
            else:
                t='no'
    mensaje_pantalla(t)


def Crea_Img(color):
    im = pygame.image.load('F6.png')
    w_h = pygame.Surface.get_size(im)
    destino = pygame.Surface(w_h)
    im = pygame.transform.threshold(destino,im,color,(50,50,50),(0,0,0),2)
    pygame.image.save(destino,'New.PNG')
    img = Image.open('New.PNG')
    imagen = img.convert('RGB')
    pixels = imagen.load()
    w,h = imagen.size
    for i in range(w):
        for j in range(h):
            r,g,b = pixels[i,j]
            pixels[i,j] = (b,g,r)
    ima=pygame.image.load('New.png')
    ventana.blit(ima,(319,0))
    pygame.display.flip()
    
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imagen Termica")
imagen_fondo = load_image('F6.PNG')
img=Image.open('F6.PNG')
imagen=Image.open('F6.PNG')
img=img.convert('L')
aColores=[]
Colores_barra(img,aColores)

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
        
        #Muestra Temperatura
        if(pygame.mouse.get_pressed()==(1,0,0)):
              if(pygame.mouse.get_pos()[0]>0 and pygame.mouse.get_pos()[0]<302):
                   if(pygame.mouse.get_pos()[1]>0 and pygame.mouse.get_pos()[1]<237):
                    pos=pygame.mouse.get_pos() 
                    colores_pix2barra(pos[0],pos[1])


        #Muestra Colores
        if(pygame.mouse.get_pressed()==(1,0,0)):
              if(pygame.mouse.get_pos()[0]>303 and pygame.mouse.get_pos()[0]<313):
                   if(pygame.mouse.get_pos()[1]>27 and pygame.mouse.get_pos()[1]<208):
                    posicion=pygame.mouse.get_pos() 
                    clr=imagen.getpixel((posicion[0],posicion[1]))
                    Crea_Img(clr) 
                                               
    ventana.blit(imagen_fondo,(0,0))
    pygame.display.flip()
