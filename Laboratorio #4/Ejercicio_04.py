from PIL import Image, ImageTk
import Tkinter
import sys,os,smtplib,mimetypes

from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase 
from email import encoders
import tkFileDialog as fd

def Cargar():
    ruta = fd.askopenfilename(title='Abrir')
    archivo = open(ruta,'r+')
    contenido = archivo.read()
    print contenido
    print 'Cargar'

def Enviar():
    #Datos GUI
    _origen = origen.get()
    _clave = clave.get()
    _destino = destino.get()
    _asunto = asunto.get()
    _mensaje = mensaje.get()
    #_adjunto = adjunto.get()

    msg = MIMEMultipart()
    msg['From'] = _origen
    msg['To'] = _destino
    msg['Subject'] = _asunto
    msg.attach(MIMEText(_mensaje,'plain'))
    #Cargar()

    ##cargamos el archivo a adjuntar
    fp = open('IMAGENES/1411.jpg','rb')
    adjunto = MIMEBase('multipart', 'encrypted')
    #lo insertamos en una variable
    adjunto.set_payload(fp.read()) 
    fp.close()  
    #lo encriptamos en base64 para enviarlo
    encoders.encode_base64(adjunto) 
    #agregamos una cabecera y le damos un nombre al archivo que adjuntamos puede ser el mismo u otro
    adjunto.add_header('Content-Disposition', 'attachment', filename='1411.jpg')
    #adjuntamos al mensaje
    msg.attach(adjunto) 
    #file = open("IMAGENES/1411.jpg", "rb")
    #attach_image = MIMEImage(file.read())
    #attach_image.add_header('Content-Disposition', 'attachment; filename = "1411.jpg"')
    #msg.attach(attach_image)

    #Autenticamos
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(_origen,_clave)

    #Enviamos
    mailServer.sendmail(_origen,_destino,msg.as_string())

    #Cerramos conexion
    mailServer.close()
    print 'El correo ha sido enviado'
    
def Salir():
    win.destroy()
    #print 'Salir' 
    
win = Tkinter.Tk()
win.title('Correos')
win.geometry('500x480')

origen = Tkinter.StringVar()
clave = Tkinter.StringVar()
destino = Tkinter.StringVar()
asunto = Tkinter.StringVar()
mensaje = Tkinter.StringVar()
adjunto = Tkinter.StringVar()

txtOrigen = Tkinter.Label(win,font='Arial',bg='white',text='De:').place(x=20,y=10)
boxOrigen = Tkinter.Entry(win,textvariable=origen).place(width=370,height=21,x=100,y=13)
txtClave = Tkinter.Label(win,font='Arial',bg='white',text='Clave:').place(x=20,y=50)
boxClave = Tkinter.Entry(win,textvariable=clave,show = '●').place(width=370,height=21,x=100,y=50)
txtDestino = Tkinter.Label(win,font='Arial',bg='white',text='Para:').place(x=20,y=90)
boxDestino = Tkinter.Entry(win,textvariable=destino).place(width=370,height=21,x=100,y=90)
txtAsunto = Tkinter.Label(win,font='Arial',bg='white',text='Asunto:').place(x=20,y=130)
boxAsunto = Tkinter.Entry(win,textvariable=asunto).place(width=370,height=21,x=100,y=130)
txtMensaje = Tkinter.Label(win,font='Arial',bg='white',text='Mensaje:').place(x=20,y=170)
boxMensaje = Tkinter.Entry(win,textvariable=mensaje).place(width=370,height=150,x=100,y=170)
txtAdjunto = Tkinter.Label(win,font='Arial',bg='white',text='Adjunto:').place(x=20,y=350)
boxAdjunto = Tkinter.Entry(win,textvariable=adjunto).place(width=250,height=21,x=100,y=350)
btnAdjuntar = Tkinter.Button(win,text='Cargar',command=Cargar,width=14,height=1,anchor='center').place(x=360,y=350)
btnRetroceder = Tkinter.Button(win,text='Enviar',command=Enviar,width=15,height=2,anchor='center').place(x=120,y=410)
btnRetroceder = Tkinter.Button(win,text='Salir',command=Salir,width=15,height=2,anchor='center').place(x=270,y=410)
win.mainloop()
