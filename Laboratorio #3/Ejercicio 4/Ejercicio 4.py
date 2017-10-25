from PIL import Image
import math
import sys,os

def RecortaImagen(imagen):
    w,h = imagen.size
    aLetraA = [(0,0,83,89),(0,89,83,179),(0,179,83,248),(0,248,83,333),(0,333,83,415),(0,415,83,506)]
    aLetraE = [(83,0,157,89),(83,89,157,179),(83,179,157,248),(83,248,157,333),(83,333,157,415),(83,415,157,506)]
    aLetraI = [(157,0,223,89),(157,89,227,169),(157,169,227,247),(157,247,227,320),(157,320,223,415),(157,415,246,506)]
    aLetraO = [(223,0,295,89),(227,89,295,169),(227,169,295,247),(233,247,295,320),(223,320,295,415),(246,415,316,506)]
    aLetraU = [(295,0,406,89),(295,89,406,169),(295,169,406,247),(295,247,406,339),(295,339,406,415),(316,415,406,506)]
    return aLetraA,aLetraE,aLetraI,aLetraO,aLetraU

def CreaImagen(vocal,imagen,aLetras):
    aLetrasN = []
    for i in aLetras:
        caja = i
        im = imagen.crop(caja)
        aLetrasN.append(im)
    return GuardaImagen(vocal,aLetrasN)

def GuardaImagen(i,aL):
    count = 1
    for v in aL:
        v.save(i+'/'+i+str(count)+'.jpg')
        count += 1
    return

def Momento(img,p,q):
    global background
    Mpq = 0.0
    height,width = img.size
    for v in range(height):
        for u in range(width):
            if(img.getpixel((v,u)) != background):
                Mpq += math.pow(v,p)*math.pow(u,q)
    return Mpq

def MomentoCentral(img,p,q):
    global background
    m00 = Momento(img,0,0)
    xCtr = Momento(img,1,0)/m00
    yCtr = Momento(img,0,1)/m00
    cMpq = 0.0
    height,width = img.size
    for v in range(height):
        for u in range(width):
            if(img.getpixel((v,u)) != background):
                cMpq += math.pow(v-yCtr,p)*math.pow(u-xCtr,q) 
    return cMpq

def MCNormal(img,p,q):
    m00 = Momento(img,0,0)
    norm = math.pow(m00,(p+q+2)/2)
    return MomentoCentral(img,p,q)/norm

def MomentoH1(img):
    return MCNormal(img,2,0) + MCNormal(img,0,2)

def MomentoH2(img):
    return (MCNormal(img,2,0)-MCNormal(img,0,2))**2 + (4*(MCNormal(img,1,1))**2)

def MomentoH3(img):
    return (MCNormal(img,3,0)-3*MCNormal(img,1,2))**2 + (3*MCNormal(img,2,1)-MCNormal(img,0,3))**2

def MomentoH4(img):
    return (MCNormal(img,3,0)+MCNormal(img,1,2))**2 + (MCNormal(img,2,1)+MCNormal(img,0,3))**2

def MomentoH5(img):
    V1 = (MCNormal(img,3,0)-3*(MCNormal(img,1,2))) * (MCNormal(img,3,0)+MCNormal(img,1,2))
    V2 = ((MCNormal(img,3,0)+MCNormal(img,1,2))**2 - 3*(MCNormal(img,2,1)+MCNormal(img,0,3))**2)
    V3 = ((3*MCNormal(img,2,1)-MCNormal(img,0,3)) * (MCNormal(img,2,1)+MCNormal(img,0,3)))
    V4 = (3*(MCNormal(img,3,0)+MCNormal(img,1,2))**2 - (MCNormal(img,2,1)+MCNormal(img,0,3))**2)
    return V1*V2+V3*V4

def MomentoH6(img):
    V1 = (MCNormal(img,2,0)-MCNormal(img,0,2))
    V2 = ((MCNormal(img,3,0)+MCNormal(img,1,2))**2 - (MCNormal(img,2,1)+MCNormal(img,0,3))**2)
    V3 = (4*MCNormal(img,1,1))
    V4 = ((MCNormal(img,3,0)+MCNormal(img,1,2))*(MCNormal(img,2,1)+MCNormal(img,0,3)))
    return V1*V2+V3*V4

def MomentoH7(img):
    V1 = ((3*(MCNormal(img,2,1)-MCNormal(img,0,3))) * (MCNormal(img,3,0)+MCNormal(img,1,2)))
    V2 = ((MCNormal(img,3,0)+MCNormal(img,1,2))**2 - 3*(MCNormal(img,2,1)+MCNormal(img,0,3))**2)
    V3 = ((3*(MCNormal(img,1,2)-MCNormal(img,3,0))) * (MCNormal(img,2,1)+MCNormal(img,0,3)))
    V4 = ((3*(MCNormal(img,3,0)+MCNormal(img,1,2))**2) - (MCNormal(img,2,1)+MCNormal(img,0,3))**2)
    return V1*V2+V3*V4

def MomentosG(img):
    global fichero
    h1 = MomentoH1(img); fichero.write('H1='+str(h1)+'; ')
    h2 = MomentoH2(img); fichero.write('H2='+str(h2)+'; ')
    h3 = MomentoH3(img); fichero.write('H3='+str(h3)+'; ')
    h4 = MomentoH4(img); fichero.write('H4='+str(h4)+'; ')
    h5 = MomentoH5(img); fichero.write('H5='+str(h5)+'; ')
    h6 = MomentoH6(img); fichero.write('H6='+str(h6)+'; ')
    h7 = MomentoH7(img); fichero.write('H7='+str(h7)+'\n')

#im = Image.open('F1.PNG')
#print MomentosG(imagen)
aVocales= ['A','E','I','O','U']
img = Image.open('vocales.jpg')
aLA,aLE,aLI,aLO,aLU = RecortaImagen(img)
for v in aVocales:
    if(v == 'A'): CreaImagen(v,img,aLA)
    if(v == 'E'): CreaImagen(v,img,aLE)
    if(v == 'I'): CreaImagen(v,img,aLI)
    if(v == 'O'): CreaImagen(v,img,aLO)
    if(v == 'U'): CreaImagen(v,img,aLU)

fichero = open('Momentos_HU.txt','w')

background = 0
aVA=[]; aVE=[]; aVI=[]; aVO=[]; aVU=[]
for i in aVocales:
    aDir = os.listdir(i+'/')
    for j in aDir:
        imagen = Image.open(i+'/'+j)
        if(i=='A'): fichero.write(str(j)+' --> '); MomentosG(imagen)
        if(i=='E'): fichero.write(str(j)+' --> '); MomentosG(imagen)
        if(i=='I'): fichero.write(str(j)+' --> '); MomentosG(imagen)
        if(i=='O'): fichero.write(str(j)+' --> '); MomentosG(imagen)
        if(i=='U'): fichero.write(str(j)+' --> '); MomentosG(imagen)
fichero.close()
print 'Todo OK'
