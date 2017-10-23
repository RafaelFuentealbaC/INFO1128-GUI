from PIL import Image
import matplotlib.pyplot as plt

def EcHisto(datos,archivo,img):
    plt.figure()
    x = range(len(datos))
    plt.bar(x,datos,align='center')
    plt.title('Ecualizacion'+img)
    plt.xlabel('Valores de intensidad')
    plt.ylabel('Numero de pixeles')
    plt.savefig(archivo)
    return None

aNomImg = ['F1','F2','F3','F4','F5','F6']

for i in aNomImg:
    imagen = Image.open('H'+i+'/'+i+'.PNG')
    if(imagen.mode!='L'): imagen = imagen.convert('L')
    #calcula histograma acumulativo
    h_Acumulativo = []
    acumulador = 0
    htgAcumulativo = imagen.histogram()
    for v in htgAcumulativo:
        acumulador += v
        h_Acumulativo.append(acumulador)
    #extrae valores de los pixeles
    datos = imagen.getdata()
    #ecualizacion lineal
    datos_Lineales = []
    h,w = imagen.size
    M = h*w
    K = 256
    for x in datos:
        datos_Lineales.append(round(h_Acumulativo[x]*(K-1))/M)

    #creacion de la imagen ecualizada
    foto_ecualizada = Image.new('L',imagen.size)
    foto_ecualizada.putdata(datos_Lineales)
    EcHisto(datos_Lineales,'H'+i+'/Histo_Ec_'+i+'.PNG',i)
    foto_ecualizada.save('H'+i+'/'+i+'_Ecualizada.PNG')#,imagen.close())
    #foto_ecualizada.close()
print 'Fotos Ecualizadas Guardadas'

