# -*- coding: utf-8 -*-
import mysql.connector
import getpass
import  time
from datetime import datetime
import time as t
from colorama import init, Fore, Back, Style
global resultado
dbConnect={
    'host':'lldk499.servidoresdns.net',
    'user':'qadr270',
    'password':'456456456',
    'database':'qadr270',
    

}
conexion=mysql.connector.connect(**dbConnect)
cursor=conexion.cursor()

#Consultar tabla de la bbdd consulta la base de datos actual
def consultar_ddbb():
    global resultado
    sql="Select * from usuarios"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    #print(resultado)
    for datos in resultado:
        bd=str(datos[0])+" "+datos[1]+" "+datos[2]+" "+str(datos[3])+"\n"
        print(datos[1])
        

def registrar():
    #introducir nuevo usuario
    global resultados
    sql="Select * from usuarios"
    cursor.execute(sql)
    resultado=cursor.fetchall()
    for datos in resultado:
        bd=str(datos[0])+" "+datos[1]+" "+datos[2]+" "+str(datos[3])+"\n"
    lista=[datos[0]]
    for i in lista:
        nuevo_id=max(lista)+1
    id_usu=nuevo_id
    email_usu=input("digame su email: ")
    passw_usu2=""
    passw_usu=getpass.getpass("escriba su contraseña: ")
    while passw_usu!=passw_usu2:
        passw_usu2=getpass.getpass("escribe de nuevo su contraseña: ")       
    nivel_usu="1"
    #Inserta Registros
    sqlInsertar="insert into usuarios(ID,EMAIL,CONTRASEÑA,NIVEL)values(%s,%s,%s,%s)"
    cursor.execute(sqlInsertar,(id_usu,email_usu,passw_usu,nivel_usu))
    conexion.commit()
    #cursor.close()
    #conexion.close()


#Consulta todos los datos del usuario
def consulta_user(email_usu):
    global resultado
    sql="Select *from usuarios where email=%s"
    cursor.execute(sql,(email_usu,))
    resultado=cursor.fetchone()
    #conexion.commit()
    #cursor.close()
    #print(resultado[1])
    print( resultado[3])
    return resultado


#Actualizar nivel para subir un nivel num hace referencia al nuevo nivel al que sube
def actualizar_nivel(num,email):    
    #user_cambionivel=input("escriba su email: ")
    sql2="update usuarios set NIVEL=%s where EMAIL=%s"
    valores=(num,email)
    cursor.execute(sql2,valores)
    resultado=cursor.fetchone()
    conexion.commit()
    #cursor.close()
    #conexion.close()

#preguntas enigmas completado.pide enigmas de la listaA y las soluciones son de la listaB
listaA=["Tienes 3 bolsas de caramelos que estan las tres mal\n etiquetadas, en una la etiqueta pone caramelos de fresa\n en otra pone caramelos de naranja y en la última pone mezcla\n de caramelos de naranja y fresa. ¿cuántos caramelos \nmínimo tienes que sacar para saber donde estan\n realmente las etiquetas?: ","En una casa hay tres relojes funcionando.\n El día 1 de enero todos ellos indicaban la hora correctamente,\n pero sólo estaba funcionando bien el reloj del dormitorio;\n el de la cocina se atrasaba un minuto al día y\n el del salón se adelantaba un minuto al día.\n Si los relojes continúan marchando así…\n¿al cabo de cuántos días volverán los tres a marcar\n la hora exacta?:  ","¿Que números hay en la siguiente línea de la secuencia? \n             1\n            1 1\n            2 1\n          1 2 1 1\n        1 1 1 2 2 1\n        3 1 2 2 1 1\n      1 3 1 1 2 2 2 1\n    1 1 1 3 2 1 3 2 1 1\n3 1 1 3 1 2 1 1 1 3 1 2 2 1 \n" ,"Un collar y una lanza se cambian por un escudo.Una lanza se cambia por un collar y un cuchillo.Dos escudos se cambian por tres cuchillos.¿Cuántos collares cuesta una lanza? ","Hemos colocado en el jardín dos velas de distinta altura.\n La más larga mide 28 cm y tarda 7 horas en consumirse completamente,\n mientras que la más corta, que es más gruesa, tarda 11 horas en consumirse.\n Encendemos las dos a la vez cuando empieza la fiesta y al cabo de 3 horas,\n cuando se van los amigos, las apagamos. \nEn ese momento tienen las dos la misma altura. \n¿Cuál era la longitud inicial en centímetros \nde la la vela más corta? "]
listaB=["1","1440","13211311123113112211","5","22"]
nivel=1
#print("nivel "+str(nivel))
def start (num):
  global email_usu
  global resultado
  global nivel
  #nivel=num
  nivel=resultado[3]
  instanteInicial = datetime.now()
  for pre in listaA[num:]:
    for sol in listaB[num:]:
      enigma=input(pre)
      while enigma!=sol:
        print("lo siento, prueba de nuevo ")
        print("\n")
        #print(Fore.GREEN+"           nivel "+str(nivel_nuevo)+Fore.WHITE)
        enigma=input(pre)
      # al final de la partida te dice el tiempo de respuesta y empezamos el siguiente nivel
      instanteFinal = datetime.now()
      tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
      segundos = tiempo.seconds
      print(Fore.RED+"     CORRECTO!!!"+Fore.WHITE+", tu tiempo de respuesta ha sido "+ str(segundos)+" Segundos")
      
      listaA.pop(0)
      listaB.pop(0)
      nivel_nuevo=resultado[3]+1
      actualizar_nivel(nivel_nuevo,resultado[1])
      print(nivel_nuevo)
      print(resultado)
      print(Fore.GREEN+"          Siguiente nivel "+Fore.WHITE)
      t.sleep(2)
      print("\n")
    
      start(resultado[3]-1)

#Iniciar sesion
def iniciar_sesion(email_usu,nombre):
    global resultado
    email_usu=input(Fore.BLUE+"Escriba su email: "+Fore.WHITE)
    prueba=consulta_user(email_usu)
    while prueba!=resultado[1]:
        t.sleep(1)
        print("Usuario no registrado, compruebe su email:")
        prueba=consulta_user(email_usu)
    t.sleep(1)
    print("Usuario correcto")
    t.sleep(1)
    print("\n")
    nombre=getpass.getpass("digame su contraseña: ")
    t.sleep(2)
    while nombre!=resultado[2]:
        print(Fore.RED+"Lo siento vuelve a intentarlo"+Fore.WHITE)
        nombre=getpass.getpass("digame su contraseña: ")       
    print(Fore.BLUE+"contraseña correcta"+Fore.WHITE)        
    print(Fore.YELLOW+"Cargando datos...\n"+Fore.WHITE)
    t.sleep(5)
    print(Fore.GREEN+"START\n"+Fore.WHITE)
    start(resultado[3]-1)

def inico_juego():
    print("       Bienvenido a:\n       "+Fore.GREEN+"   3NI?M4"+Fore.WHITE)
    print("\n")
    empezar=input("¿Iniciar sesión o Resgistrarse? i/r: ")
    if empezar=="i":
        iniciar_sesion()
    elif empezar=="r":
        registrar()
        print("INICIO DE SESION")
        iniciar_sesion()
    else:
        print("Eso no es una respuesta prueba de nuevo")
        empezar=input("¿Iniciar sesión o Resgistrarse? I/R: ")





