from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np

def Pix2Image(img,mode='RGB'):
    if(img.max() > 255):
        img *= 255.0 / img.max()
    img = array(img,uint8)
    imagen = Image.fromarray(img,mode)
    return imagen

def Image2Pix_rgba(img):
    i = img.convert('RGBA')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,4))
    return img

def MaskImg_gray(img):
    aT = array([0.00,0.00,0.00])
    img = dot(img,aT)
    return Pix2Image(img)

def MaskImg_rgb(img):
    aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
    img = dot(img,aT)
    return Pix2Image(img)

def MaskImg_rgba(img):
    aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00],
                [0.00,0.00,0.00]  #Canal Azul
                ])
    img = dot(img,aT)
    return Pix2Image(img)

def MaskImg_cmyk(img):
    aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
    img = dot(img,aT)
    return Pix2Image(img)

def MaskImg_hsv(img):
    aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
    img = dot(img,aT)
    return Pix2Image(img)

aImg=['F1.PNG','F2.PNG','F2.PNG','F4.PNG','F5.PNG','F6.PNG']

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix(img)
    imagen = MaskImg_gray(im)
    imagen.save('gray_'+(aImg[i]))

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix(img)
    imagen = MaskImg_rgb(im)
    imagen.save('rgb_'+(aImg[i]))

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix(img)
    imagen = MaskImg_rgba(im)
    imagen.save('rgba_'+(aImg[i]))

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix(img)
    imagen = MaskImg_cmyk(im)
    imagen.save('cmyk_'+(aImg[i]))

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix(img)
    imagen = MaskImg_hsv(im)
    imagen.save('hsv_'+(aImg[i]))

