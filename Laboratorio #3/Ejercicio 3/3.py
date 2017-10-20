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


aImg=['F1.jpg','F2.jpg','F3.jpg','F4.jpg','F5.jpg','F6.jpg']
#GRAY
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    imagen = img.convert('L')
    imagen.save('gray/gray_'+(aImg[i]))

#Canales RGB

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
     #imagen general
     imagen1 = img.convert('RGB')
     imagen1.save('RGB/rgb_'+(aImg[i]))

#Canales RGBA


#RED
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = array([# %R   %G   %B   &A
                [1.00,0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00,0.00], #Canal Azul
                [0.00,0.00,0.00,0.00]  #Canal Alpha
                ])
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/R/red_'+(aImg[i]))

#Green
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = array([# %R   %G   %B   &A
                [0.00,0.00,0.00,0.00], #Canal Rojo
                [0.00,1.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00,0.00], #Canal Azul
                [0.00,0.00,0.00,0.00]  #Canal Alpha
                ])
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/G/green_'+(aImg[i]))
#Blue
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = array([# %R   %G   %B   &A
                [0.00,0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,1.00,0.00], #Canal Azul
                [0.00,0.00,0.00,0.00]  #Canal Alpha
                ])
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/B/blue_'+(aImg[i]))

#Alpha

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = array([# %R   %G   %B   &A
                [0.00,0.00,0.00,0.00], #Canal Rojo
                [0.00,0.00,0.00,0.00], #Canal Verde
                [0.00,0.00,0.00,0.00], #Canal Azul
                [0.00,0.00,0.00,1.00]  #Canal Alpha
                ])
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/A/alpha_'+(aImg[i]))
    #imagen RGBA General
    imagen1 = img.convert('RGBA')
    imagen1.save('RGBA/rgba_'+(aImg[i]))


#Canales CMYK
#Canal C
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = array([#  C    M    Y    K
                [1.00,0.00,0.00,0.00], 
                [0.00,0.00,0.00,0.00], 
                [0.00,0.00,0.00,0.00],
                [0.00,0.00,0.00,0.00]
                ])
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/C/c_'+(aImg[i]))

#Canal M
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = array([#  C    M    Y    K
                [0.00,0.00,0.00,0.00], 
                [0.00,1.00,0.00,0.00], 
                [0.00,0.00,0.00,0.00],
                [0.00,0.00,0.00,0.00]
                ])
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/M/m_'+(aImg[i]))


#Canal Y
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = array([#  C    M    Y    K
                [0.00,0.00,0.00,0.00], 
                [0.00,0.00,0.00,0.00], 
                [0.00,0.00,1.00,0.00],
                [0.00,0.00,0.00,0.00]
                ])
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/Y/y_'+(aImg[i]))

#canal K

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = array([#  C    M    Y    K
                [0.00,0.00,0.00,0.00], 
                [0.00,0.00,0.00,0.00], 
                [0.00,0.00,0.00,0.00],
                [0.00,0.00,0.00,1.00]
                ])
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/K/k_'+(aImg[i]))

    imagen1 = img.convert('CMYK')
    imagen1.save('CMYK/cmyk_'+(aImg[i]))
'''
#Canales HSV

#canal H
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [1.00,0.00,0.00], #Canal H
                [0.00,0.00,0.00], #Canal S
                [0.00,0.00,0.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'HSV')
    imagen.save('HSV/H/h_'+(aImg[i]))

#canal S

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [0.00,0.00,0.00], #Canal H
                [0.00,1.00,0.00], #Canal S
                [0.00,0.00,0.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'HSV')
    imagen.save('HSV/S/s_'+(aImg[i]))

#canal V

for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [0.00,0.00,0.00], #Canal H
                [0.00,0.00,0.00], #Canal S
                [0.00,0.00,1.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'HSV')
    imagen.save('HSV/V/v_'+(aImg[i]))
 #   imagen1 = img.convert('HSV')
 #   imagen1.save('HSV/hsv_'+(aImg[i]))
'''
print 'listo'
