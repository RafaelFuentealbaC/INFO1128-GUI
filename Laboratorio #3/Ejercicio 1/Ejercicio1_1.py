from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np

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

def MaskingGreen(img):
    aT = array([# %R   %G   %B
                [1.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
    img = dot(img,aT)
    return Pix2Image(img)

img = Image.open('F1.PNG')
im = Image2Pix(img)
imagen = MaskImg(im)
imagen.save('F1_Green.PNG')

img_Green = Image.open('F1_Green.PNG')
im_Green = Image2Pix(img_Green)
imagen_Yellow = MaskingGreen(im_Green)
imagen_Yellow.save('F1_Yellow.PNG')
