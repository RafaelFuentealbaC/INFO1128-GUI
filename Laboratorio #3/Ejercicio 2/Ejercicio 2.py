from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np
import sys, pygame
from pygame.locals import *

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
    i = img.convert('RGB')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,3))
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
 
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imagen Termica")
imagen_fondo = load_image('F6.PNG')
verde=(3,255,3)

while True:
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)

        if(pygame.mouse.get_pressed()==(1,0,0)):
              if(pygame.mouse.get_pos()[0]>0 and pygame.mouse.get_pos()[0]<303):
                   if(pygame.mouse.get_pos()[1]>0 and pygame.mouse.get_pos()[1]<235):
                    pos=pygame.mouse.get_pos() 
                    color=ventana.get_at((pos[0], pos[1]))
                    print 'color: ',color

                    w,h=imagen_fondo
                    for x in range(w):
                        for y in range(h):
                            r, g, b, a = pixels[x, y]
                            if (r, g, b) == verde:
                                print'barra'
                

                       
                       

    ventana.blit(imagen_fondo,(0,0))
    pygame.display.flip()
