from PIL import Image
import matplotlib.pyplot as plt

def HistoNormal(datos,archivo,img):
    plt.figure()
    x = range(len(datos))
    plt.bar(x,datos,align='center')
    plt.title('Histograma '+img+' Normal')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.savefig(archivo)
    return None

def HistoAcumulativo(datos,archivo,img):
    plt.figure()
    x = range(len(datos))
    plt.bar(x,datos,align='center')
    plt.title('Histograma '+img+' Acumulativo')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.savefig(archivo)
    return None

aNomImg = ['F1','F2','F3','F4','F5','F6']

for i in aNomImg:
    imagen = Image.open('Histogramas_'+i+'/'+i+'.PNG')
    if(imagen.mode!='L'): imagen = imagen.convert('L')
    htgNormal = imagen.histogram()
    HistoNormal(htgNormal,'Histogramas_'+i+'/Histo_Normal.PNG',i)
print 'Histogramas Normales Guardados'

for i in aNomImg:
    imagen = Image.open('Histogramas_'+i+'/'+i+'.PNG')
    if(imagen.mode!='L'): imagen = imagen.convert('L')
    h_Acumulativo = []
    acumulador = 0
    htgAcumulativo = imagen.histogram()
    for v in htgAcumulativo:
        acumulador += v
        h_Acumulativo.append(acumulador)
    HistoAcumulativo(h_Acumulativo,'Histogramas_'+i+'/Histo_Acumulativo.PNG',i)
print 'Histogramas Acumulativos Guardados'
