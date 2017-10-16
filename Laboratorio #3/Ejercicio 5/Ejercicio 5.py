from PIL import Image
import matplotlib.pyplot as plt

def HistoNormal(datos,archivo,img):
    plt.figure()
    x = range(len(datos))
    plt.bar(x,datos,align='center')
    plt.title('Histograma '+img+' Normal')
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.savefig(archivo,bbox_inches='tight')
    return None

aNomImg = ['F1','F2','F3','F4','F5','F6']

for i in aNomImg:
    imagen = Image.open('Histogramas_'+i+'/'+i+'.PNG')
    if(imagen.mode!='L'): imagen = imagen.convert('L')
    htgNormal = imagen.histogram()
    HistoNormal(htgNormal,'Histogramas_'+i+'/Histo_Normal.PNG',i)
print 'Histogramas Normales Guardados'
