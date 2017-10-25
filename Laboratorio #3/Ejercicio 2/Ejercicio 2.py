from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np
import sys, pygame
from pygame.locals import *
import pygame.font

#-- Dimension Pantalla Pygame -- 
WIDTH = 318
HEIGHT = 237

def Pix2Image(img,mode='RGB'):
    if(img.max() > 255):
        img *= 255.0 / img.max()
    img = array(img,uint8)
    imagen = Image.fromarray(img,mode)
    return imagen

def Image2Pix(img):
    i = img.convert('L')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,1))
    return img

def MaskImg(img):
    aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,1.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
    img = dot(img,aT)
    return Pix2Image(img)
 
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 

def mensaje_pantalla(text,pantalla):
    fuente = pygame.font.Font(None, 20)
    mensaje = fuente.render(text, 1, (0, 0, 0))
    pantalla.blit(mensaje,(4,3))
    pygame.display.flip()

def temp(color):
    temp=(color*0.035)+17.1
    return temp
    
def  MAP(x,vi,vf,vis,vfs):
    return(x-vi)*(vfs-vis)/(vf-vi)+vis

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
        t='temperatura: '+str(temp(color))
    else:
        if color+1 in aColores or color -1 in aColores:
            t='temperatura: '+str(temp(color))
        else:
            if color+2 in aColores or color-2 in aColores:
                t='temperatura: '+str(temp(color))
            else:
                t='noo'
    print t
    #mensaje_pantalla(t,ventana)


def Crea_Img(aimg):
    print len(aimg)
    for i in range(len(aimg-1)):
        print aimg[i]   
    



aNewImg=[]
def img_con_colores(x1,y1):
    clr=img.getpixel((x1,y1))

    for x in range(0,302):
        for y in range(0,237):
            color=img.getpixel((x,y))

            if clr==color:
                aNewImg.append('['+str(x)+']')
                aNewImg.append('['+str(x)+']')      
    Crea_Img(aNewImg)
    return 

ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imagen Termica")
imagen_fondo = load_image('F6.PNG')
verde=(3,255,3)


img=Image.open('F6.PNG')
imagen=Image.open('F6.PNG')
img=img.convert('L')
aColores=[]
#aClr=[]
#Colores_img(img,aClr)
Colores_barra(img,aColores)

print 'colores guardados'

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
                    img_con_colores(posicion[0],posicion[1])
                    
                    
                                       
    ventana.blit(imagen_fondo,(0,0))
    pygame.display.flip()
