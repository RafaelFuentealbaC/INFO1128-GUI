import win32api as win
import os,ctypes,time

ruta = win.GetFullPathName('IMAGENES')
dire = os.listdir(ruta)
print len(dire)
for i in range(len(dire)):
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, 'C:\\Users\\Rafael Fuentealba\\Desktop\\Lab4\\IMAGENES\\'+dire[i],0)
    time.sleep(3)
   
