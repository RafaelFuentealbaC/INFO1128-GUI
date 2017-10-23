from PIL import Image
from numpy import array,dot,dstack,ones,random,uint8,zeros
import numpy as np
import colorsys

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

def TresCanales(C1,C2,C3):
    aT = array([# %C1 %C2 %C3
                [C1,0.00,0.00], #Canal 1
                [0.00,C2,0.00], #Canal 2
                [0.00,0.00,C3]  #Canal 3
                ])
    return aT

def CuatroCanales(C1,C2,C3,C4):
    aT = array([# %C1 %C2 %C3 &C4
                [C1,0.00,0.00,0.00], #Canal 1
                [0.00,C2,0.00,0.00], #Canal 2
                [0.00,0.00,C3,0.00], #Canal 3
                [0.00,0.00,0.00,C4]  #Canal 4
                ])
    return aT

aImg=['F1.PNG','F2.PNG','F3.PNG','F4.PNG','F5.PNG','F6.PNG']

#GRAY
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    imagen = img.convert('L')
    imagen.save('GRAY/gray_'+(aImg[i]))


#Canales RGB
#RED
for i in range(len(aImg)):
     img = Image.open(aImg[i])
     im = Image2Pix_rgb(img)
     aT = TresCanales(1.00,0.00,0.00)
     imagen = MaskImg(im,aT,'RGB')
     imagen.save('RGB/R/red_'+(aImg[i]))
     
#GREEN
for i in range(len(aImg)):
     img = Image.open(aImg[i])
     im = Image2Pix_rgb(img)
     aT = TresCanales(0.00,1.00,0.00)
     imagen = MaskImg(im,aT,'RGB')
     imagen.save('RGB/G/green_'+(aImg[i]))
     
#BLUE
for i in range(len(aImg)):
     img = Image.open(aImg[i])
     im = Image2Pix_rgb(img)
     aT = TresCanales(0.00,0.00,1.00)
     imagen = MaskImg(im,aT,'RGB')
     imagen.save('RGB/B/blue_'+(aImg[i]))
     #imagen general
     imagen1 = img.convert('RGB')
     imagen1.save('RGB/ImgRGB/rgb_'+(aImg[i]))


aImg=['F1.jpg','F2.jpg','F3.jpg','F4.jpg','F5.jpg','F6.jpg']

#Canales RGBA
#RED
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = CuatroCanales(1.00,0.00,0.00,0.00)
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/R/red_'+(aImg[i]))
    
#Green
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = CuatroCanales(0.00,1.00,0.00,0.00)
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/G/green_'+(aImg[i]))
    
#Blue
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = CuatroCanales(0.00,0.00,1.00,0.00)
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/B/blue_'+(aImg[i]))

#Alpha
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_rgba(img)
    aT = CuatroCanales(0.00,0.00,0.00,1.00)
    imagen = MaskImg(im,aT,'RGBA')
    imagen.save('RGBA/A/alpha_'+(aImg[i]))
    #imagen RGBA General
    imagen1 = img.convert('RGBA')
    imagen1.save('RGBA/ImgRGBA/rgba_'+(aImg[i]))
    

#Canales CMYK
#Canal C
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = CuatroCanales(1.00,0.00,0.00,0.00)
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/C/c_'+(aImg[i]))

#Canal M
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = CuatroCanales(0.00,1.00,0.00,0.00)
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/M/m_'+(aImg[i]))

#Canal Y
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = CuatroCanales(0.00,0.00,1.00,0.00)
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/Y/y_'+(aImg[i]))

#canal K
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_cmyk(img)
    aT = array([#  C    M    Y    K
                [0.00,0.00,0.00,1.00],
                [0.00,0.00,0.00,1.00],
                [0.00,0.00,0.00,1.00],
                [0.00,0.00,0.00,1.00]
                ])
    imagen = MaskImg(im,aT,'CMYK')
    imagen.save('CMYK/K/k_'+(aImg[i]))

    imagen1 = img.convert('CMYK')
    imagen1.save('CMYK/ImgCMYK/cmyk_'+(aImg[i]))


#Canales HSV
#canal H
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [1.00,1.00,1.00], #Canal H
                [0.00,0.00,0.00], #Canal S
                [0.00,0.00,0.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'RGB')
    imagen.save('HSV/H/h_'+(aImg[i]))

#canal S
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [0.00,0.00,0.00], #Canal H
                [1.00,1.00,1.00], #Canal S
                [0.00,0.00,0.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'RGB')
    imagen.save('HSV/S/s_'+(aImg[i]))

#canal V
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [0.00,0.00,0.00], #Canal H
                [0.00,0.00,0.00], #Canal S
                [1.00,1.00,1.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'RGB')
    imagen.save('HSV/V/v_'+(aImg[i]))
    
#Imagen HSV    
for i in range(len(aImg)):
    img = Image.open(aImg[i])
    im = Image2Pix_hsv(img)
    aT = array([# H     S    V
                [1.00,0.00,0.00], #Canal H
                [0.00,1.00,0.00], #Canal S
                [0.00,0.00,1.00]  #Canal V
                ])
    imagen = MaskImg(im,aT,'RGB')
    imagen.save('HSV/ImgHSV/hsv_'+(aImg[i]))
    
print 'Imagenes Procesadas ¡OK!'
