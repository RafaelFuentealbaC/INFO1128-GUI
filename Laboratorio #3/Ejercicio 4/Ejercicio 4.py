from PIL import Image

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

aVocales= ['A','E','I','O','U']
img = Image.open('vocales.jpg')
aLA,aLE,aLI,aLO,aLU = RecortaImagen(img)
for v in aVocales:
    if(v == 'A'): CreaImagen(v,img,aLA)
    if(v == 'E'): CreaImagen(v,img,aLE)
    if(v == 'I'): CreaImagen(v,img,aLI)
    if(v == 'O'): CreaImagen(v,img,aLO)
    if(v == 'U'): CreaImagen(v,img,aLU)
