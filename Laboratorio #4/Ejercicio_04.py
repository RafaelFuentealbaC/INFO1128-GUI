from PIL import Image, ImageTk
import Tkinter
import sys,os,smtplib,mimetypes
import tkFileDialog as tk, tkMessageBox

from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase 
from email import encoders

def Cargar(win,msg):
    try:
        archivo = tk.askopenfilename(title = "Abrir",initialdir = "/",filetypes = (("jpeg files","*.jpg"),("jpeg files","*.jpeg*"),("ico files","*.ico"),("png files","*.png"),("all files","*.*")))
        dire = str(os.path.split(archivo)[0]+'/'+str(os.path.split(archivo)[1]))
        name = str(os.path.split(archivo)[1])
        myfile = open(dire,'rb')
        adjunto = MIMEBase('multipart', 'encrypted')
        #lo insertamos en una variable
        adjunto.set_payload(myfile.read()) 
        myfile.close()  
        #lo encriptamos en base64 para enviarlo
        encoders.encode_base64(adjunto) 
        #agregamos una cabecera y le damos un nombre al archivo que adjuntamos puede ser el mismo u otro
        adjunto.add_header('Content-Disposition', 'attachment', filename=name)
        #adjuntamos al mensaje
        msg.attach(adjunto)
        tkMessageBox.showinfo('Mensajes','Archivo Cargado')
    except:
        pass

def Enviar(msg):
    #Datos GUI
    _origen = origen.get()
    _clave = clave.get()
    _destino = destino.get()
    _asunto = asunto.get()
    _mensaje = mensaje.get()

    msg['From'] = _origen
    msg['To'] = _destino
    msg['Subject'] = _asunto
    msg.attach(MIMEText(_mensaje,'plain'))

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
    tkMessageBox.showinfo('Mensajes','Correo Enviado!')
    
def Salir():
    win.destroy()
    
win = Tkinter.Tk()
win.title('Correos')
win.geometry('500x480')
win.config(bg='#2980B9')

origen = Tkinter.StringVar()
clave = Tkinter.StringVar()
destino = Tkinter.StringVar()
asunto = Tkinter.StringVar()
mensaje = Tkinter.StringVar()
msg = MIMEMultipart()

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
boxAdjunto = Tkinter.Label(win,text='Seleccione el archivo...',bg='gray').place(width=250,height=21,x=100,y=350)
btnAdjuntar = Tkinter.Button(win,text='Cargar',command=lambda:Cargar(win,msg),width=14,height=1,anchor='center').place(x=360,y=350)
btnRetroceder = Tkinter.Button(win,text='Enviar Correo',command=lambda:Enviar(msg),width=15,height=2,anchor='center').place(x=120,y=410)
btnRetroceder = Tkinter.Button(win,text='Salir',command=Salir,width=15,height=2,anchor='center').place(x=270,y=410)
win.mainloop()
