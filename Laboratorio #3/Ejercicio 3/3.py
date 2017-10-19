from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np

def Pix2Image(img,mode):
    if(img.max() > 255):
        img *= 255.0 / img.max()
    img = array(img,uint8)
    imagen = Image.fromarray(img,mode)
    return imagen

def Image2Pix_rgb(img):
    i = img.convert('RGB')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,3))
    return img

def Image2Pix_rgba(img):
    i = img.convert('RGBA')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,4))
    return img

def Image2Pix_cmyk(img):
    i = img.convert('CMYK')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,4))
    return img

def Image2Pix_hsv(img):
    i = img.convert('HSV')
    w,h = i.size
    data = i.getdata()
    img = array(data,uint8)
    img = img.reshape((h,w,3))
    return img

def MaskImg(img,aT,mode):
    img = dot(img,aT)
    return Pix2Image(img,mode)


aImg=['F1.PNG','F2.PNG','F2.PNG','F4.PNG','F5.PNG','F6.PNG']
#GRAY
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    imagen = img.convert('L')
    imagen.save('gray/gray_'+(aImg[i]))
#RED
for i in range(len(aImg)):
     img = Image.open(aImg[i])
     im = Image2Pix_rgb(img)
     aT = array([# %R   %G   %B
                [1.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
     imagen = MaskImg(im,aT,'RGB')
     imagen.save('RGB/R/red_'+(aImg[i]))
#GREEN
for i in range(len(aImg)):
     img = Image.open(aImg[i])
     im = Image2Pix_rgb(img)
     aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,1.00,0.00], #Canal Verde
                [0.00,0.00,0.00]  #Canal Azul
                ])
     imagen = MaskImg(im,aT,'RGB')
     imagen.save('RGB/G/green_'+(aImg[i]))
#BLUE
for i in range(len(aImg)):
     img = Image.open(aImg[i])
     im = Image2Pix_rgb(img)
     aT = array([# %R   %G   %B
                [0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,1.00]  #Canal Azul
                ])
     imagen = MaskImg(im,aT,'RGB')
     imagen.save('RGB/B/blue_'+(aImg[i]))

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = array([# %R   %G   %B
                [1.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00], #Canal Azul
                [0.00,0.00,0.00]  #Canal Alpha
                ])
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/R/red_'+(aImg[i]))
    
    imagen1 = img.convert('RGBA')
    imagen1.save('RGBA/rgba_'+(aImg[i]))

'''
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = array([# %R   %G   %B
                [0.01,0.00,0.00], #Canal Rojo
                [0.00,0.01,0.00], #Canal Verde
                [0.00,0.00,0.01]  #Canal Azul
                ])
    imagen = MaskImg(im,aT)
    imagen.save('CMYK/cmyk_'+(aImg[i]))



for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# %R   %G   %B
                [0.01,0.00,0.00], #Canal Rojo
                [0.00,0.01,0.00], #Canal Verde
                [0.00,0.00,0.01]  #Canal Azul
                ])
    imagen = MaskImg(im,aT)
    imagen.save('HSV/hsv_'+(aImg[i]))
'''
