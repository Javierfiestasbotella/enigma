# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
import getpass
import  time
from datetime import datetime
import time as t
from colorama import init, Fore, Back, Style
from bbdd import *

global resultado
def insertar_usuario():
    bd=pymysql.connect(
        host='lldk499.servidoresdns.net',
        user='qadr270',
        passwd='########',
        db='qadr270'
    )
    #conexion=mysql.connector.connect(**dbConnect)
    fcursor=bd.cursor()
    sql="INSERT INTO usuarios (email,contraseña,nivel) VALUES ('{0}','{1}','{2}')".format(nombreusuario_entry.get(),contrasenausuario_entry.get(),nivel)

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro exitoso",title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado",title="Aviso")

    bd.close()
#def ver_usuario():

'''def validacion_datos():
    bd=pymysql.connect(
        host='lldk499.servidoresdns.net',
        user='qadr270',
        passwd='Calafate1123',
        db='qadr270'
    )
fcursor=bd.cursor()
fcursor.execute("SELECT contrasena FROM login WHERE email")'''

#Button0(pantalla1,text="prueba",command=lambda:prueba_user()).pack()
    

          


def consulta_user(email_usu):
    global resultado
    sql="Select *from usuarios where email=%s"
    cursor.execute(sql,(email_usu,))
    resultado=cursor.fetchone()
    #conexion.commit()
    #cursor.close()
    #print(resultado[1])
    #print( resultado[3])
    nivel=resultado[3]
    return resultado
    return nivel
    

#enigmas funcion
def comprobar_enigma():
    global resultado
    global niveles
    3#n=resultado[3]
    consulta_user(nombreusuario_entry.get())
    niveles=Label(pantalla3, text=listaA[resultado[3]-1],bg="black",fg="green2",width="400",height="15",font=("calibri",9)).pack()

                
                
def respuesta():
    while solucion.get()!=listaB[resultado[3]-1]:
        messagebox.showinfo(message="Lo siento, esa no es la respuesta correcta, pruebe de nuevo",title="Aviso")
        sol_entry=Entry(pantalla3, textvariable=solucion)
        sol_entry.pack()
    
    messagebox.showinfo(message="Correcto!!! siguiente nivel: ",title="Aviso")
    actualizar_nivel(resultado[3],nombreusuario_entry.get())
    #listaA.pop(0)
    #listaB.pop(0)
    Label(pantalla3, text="").pack() 
    niveles.grid_remove() 
    boton3=Button(pantalla3, text="Siguiente enigma",bg="gold4",command=lambda:comprobar_enigma()).pack()
          
    comprobar_enigma()
#pantalla0
def fpantalla0():
    global pantalla0
    pantalla0=Tk()
    pantalla0.geometry("300x400")
    pantalla0.title("3NI?M4")
    pantalla0.iconbitmap("enigmaico.ico")
    pantalla0.config(bg="white")
    #miframe=Frame(raiz,width=300, height=380,background="white")
    #miframe.pack()

    image=PhotoImage(file="enigma.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso a 3NI?M4",bg="black",fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar sesión",height="3",width="30",bg="gold4",font=("calibri",10),command=lambda:fpantalla1()).pack()
    Label(text="").pack()

    Button(text="Registrarse",height="3",width="30",bg="gold4",font=("calibri",10),command=lambda:fpantalla2()).pack()
    Label(text="").pack()
    pantalla0.mainloop()
#pantalla de inicio es pantalla1
def fpantalla1():
    global pantalla1
    pantalla1=Toplevel(pantalla0)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesión")
    pantalla1.iconbitmap("enigmaico.ico")
    pantalla1.config(bg="gray93")

    Label(pantalla1, text="Por favor ingrese su email y contraseña",bg="black",fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(pantalla1, text="").pack()

    global email
    global contrasenausuario_verify
     
    email=StringVar()
    contrasenausuario_verify=StringVar()

    global nombreusuario_entry
    global contrasenausuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombreusuario_entry=Entry(pantalla1, textvariable=email)
    nombreusuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasenausuario_entry=Entry(pantalla1,show="*",textvariable=contrasenausuario_verify)
    contrasenausuario_entry.pack()
    Label(pantalla1).pack()
    
    Button(pantalla1,text="Iniciar Sesión",command=lambda:fpantalla3()).pack()
       

    


#pantalla de registro es pantalla2
def fpantalla2():
    global pantalla2
    global nivel
    nivel="1"
    pantalla2=Toplevel(pantalla0)
    pantalla2.geometry("420x330")
    pantalla2.title("Registro de usuario")
    pantalla2.iconbitmap("enigmaico.ico")
    pantalla2.config(bg="gray93")

    Label(pantalla2, text="Por favor ingrese los siguientes datos",bg="black",fg="white",width="350",height="3",font=("calibri",15)).pack()
    Label(pantalla2, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify
    global contrasenausuario2_verify
    
    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()
    contrasenausuario2_verify=StringVar()
    
    global nombreusuario_entry
    global contrasenausuario_entry
    global contrasenausuario2_entry

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry=Entry(pantalla2, textvariable=nombreusuario_verify)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contraseña").pack()
    contrasenausuario_entry=Entry(pantalla2,show="*" ,textvariable=contrasenausuario_verify)
    contrasenausuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Vuelva a escribir la Contraseña").pack()
    contrasenausuario2_entry=Entry(pantalla2,textvariable=contrasenausuario2_verify)
    contrasenausuario2_entry.pack()
    Label(pantalla2).pack()
    while contrasenausuario_verify.get()!=contrasenausuario2_verify.get():
        messagebox.showinfo(message="No no coinciden las contraseñas",title="Aviso")
    else:
        Button(pantalla2,text="Registrarse",bg="gold4",command=lambda:insertar_usuario()).pack()


def fpantalla3():
    global pantalla3
    global sol_entry
    global enigma_entry
    global solucion
    res=StringVar()
    solucion=StringVar()
    sol_entry=StringVar()
    listaA=["Tienes 3 bolsas de caramelos que estan las tres mal\n etiquetadas, en una la etiqueta pone caramelos de fresa\n en otra pone caramelos de naranja y en la última pone mezcla\n de caramelos de naranja y fresa. ¿cuántos caramelos \nmínimo tienes que sacar para saber donde estan\n realmente las etiquetas?: ","En una casa hay tres relojes funcionando.\n El día 1 de enero todos ellos indicaban la hora correctamente,\n pero sólo estaba funcionando bien el reloj del dormitorio;\n el de la cocina se atrasaba un minuto al día y\n el del salón se adelantaba un minuto al día.\n Si los relojes continúan marchando así…\n¿al cabo de cuántos días volverán los tres a marcar\n la hora exacta?:  ","¿Que números hay en la siguiente línea de la secuencia? \n             1\n            1 1\n            2 1\n          1 2 1 1\n        1 1 1 2 2 1\n        3 1 2 2 1 1\n      1 3 1 1 2 2 2 1\n    1 1 1 3 2 1 3 2 1 1\n3 1 1 3 1 2 1 1 1 3 1 2 2 1 \n" ,"Un collar y una lanza se cambian por un escudo.\nUna lanza se cambia por un collar y un cuchillo.\nDos escudos se cambian por tres cuchillos.¿Cuántos collares cuesta una lanza? ","Hemos colocado en el jardín dos velas de distinta altura.\n La más larga mide 28 cm y tarda 7 horas en consumirse completamente,\n mientras que la más corta, que es más gruesa, tarda 11 horas en consumirse.\n Encendemos las dos a la vez cuando empieza la fiesta y al cabo de 3 horas,\n cuando se van los amigos, las apagamos. \nEn ese momento tienen las dos la misma altura. \n¿Cuál era la longitud inicial en centímetros \nde la la vela más corta? "]
    listaB=["1","1440","13211311123113112211","5","22"]

    pantalla3=Toplevel(pantalla1)
    pantalla3.geometry("490x410")
    pantalla3.title("Enigmas")
    pantalla3.iconbitmap("enigmaico.ico")
    pantalla3.config(bg="AntiqueWhite3")

    Label(pantalla3, text="Enigma",bg="black",fg="white",width="350",height="2",font=("calibri",15)).pack()
    Label(pantalla3, text="").pack()

    boton=Button(pantalla3, text="escribir enigma",bg="gold4",command=lambda:comprobar_enigma()).pack()
    Label(pantalla3, text="").pack()

    #niveles=Label(pantalla3, text=i,bg="black",fg="green2",width="400",height="10",font=("calibri",9)).pack()
    sol_entry=Entry(pantalla3, textvariable=solucion)
    sol_entry.pack()

    boton2=Button(pantalla3, text="Enviar respuesta",bg="gold4",command=lambda:respuesta()).pack()
    Label(pantalla3, text="").pack()

    boton4=Button(pantalla3, text="Página principal",bg="gold4").pack()

    

fpantalla0()
#consulta_user("sara@")
#consultar_ddbb()
#actualizar_nivel(1,"sara@")
#print(resultado)

