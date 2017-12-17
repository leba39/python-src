#!/usr/bin/env python3

import requests
from datetime import datetime
from time import sleep


def Menu():
    
    print("\tBienvenido a ISS API:\n-OPCIONES-\n\n1.Personal en la estación espacial internacional.\n2.Localización actual de la estación espacial internacional.\n3.Hora de paso de la estación espacial internacional.\n4.Salir.")
    while True:
        modo=input()
        if not is_float(modo):
            print("Por favor escoja una de las opciones del menu. Valores numericos (1-4).",end="")
        else:
            m=int(modo)
            if m not in range(1,5):
                print("Opcion no encontrada. (1-4)")
            else:
                return m
    
def getDatos(modo,parametros):

    url="http://api.open-notify.org/"
    endpoint=["astros.json","iss-now.json","iss-pass.json"]
    
    if modo==1:
        datos=requests.get(url+endpoint[modo-1])
    elif modo==2:
        datos=requests.get(url+endpoint[modo-1])
    elif modo==3:
        datos=requests.get(url+endpoint[modo-1],params=parametros)
    else:
        print("Hubo un error inesperado.")
        
    return datos.json()

def ParametrosUsuario():    #Necesita devolver un diccionario

    print("\tSe requieren los siguientes datos para devolverle la respuesta:")
    

    print("Latitud de su posición (-80º...80º):\t",end="")
    while True:    
        lat=input()
        if (not is_float(lat)) or (float(lat) < -80 or float(lat) > 80):
            print("Por favor ingrese un valor entre -80º y 80º. CAMPO OBLIGATORIO:\t",end="")
        else:
            break
    
    print("Longitud de su posición (-180º...180º):\t",end="")
    while True:
        lon=input()
        if (not is_float(lon)) or (float(lon) < -180 or float(lon) >180):
            print("Por favor ingrese un valor entre -80º y 80º. CAMPO OBLIGATORIO:\t",end="")
        else:
            break
        
    print("Altitud de su posición (0...10000m)OPCIONAL:\t",end="")
    while True:
        alt=input()
        if is_float(alt) and (float(alt) < 0 or float(alt) > 10000):
            print("Por favor ingrese un valor entre 0 y 10000(m). CAMPO OPCIONAL:\t",end="")
        elif not is_float(alt):
            alt="100"
            break
        else:
            break

    print("Número de pases (1...100)OPCIONAL:\t",end="")
    while True:
        numero=input()
        if numero.isdigit() and (int(numero)<1 or int(numero)>100):
            print("Por favor ingrese un valor entero entre 1 y 100. CAMPO OPCIONAL:\t",end="")
        elif not numero.isdigit():
            numero="1"
            break
        else:
            break

    #DICCIONARIO PARAMETROS
    param={"lat":lat,"lon":lon,"alt":alt,"n":numero}

    return param

def MostrarDat(dic,m):

    print("\nD A T A:\n")
    if m==1:
        print("\tPERSONAS")
        print(dic["number"])
        for pers in dic["people"]:
            print(pers["name"])
    elif m==2:
        t=int(dic["timestamp"])
        print("\tHORA")
        print(datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')+"\t(LOCAL)")        #HORALOCAL
        print(datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')+"\t(UTC)")       #HORAUTC
        print("\tPOSICION")
        print("Latitud:\t\t"+dic["iss_position"]["latitude"]+"\t\tº")
        print("Longitud:\t\t"+dic["iss_position"]["longitude"]+"\t\tº")
    else:
        for pase in dic["response"]:
            t=int(pase["risetime"])
            print("\n\tPASO")
            print("\tDURACION:\t"+str(pase["duration"])+" (s)")
            print("\tZENIT:")
            print(datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')+" (LOCAL)")        #HORALOCAL
            print(datetime.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')+" (UTC)")       #HORAUTC

def Main():
    #VARIABLE CONTADOR PARA PRIMER ARRANQUE. EN LOS CONSECUTIVOS FORMATEAR EL MENU Y PREGUNTAR.
    while True:
        opcion=Menu()
        if opcion!=4:
            if opcion!=3:
                datadic=getDatos(opcion,"")
                MostrarDat(datadic,opcion)
            else:
                datadic=getDatos(opcion,ParametrosUsuario())
                MostrarDat(datadic,opcion)
        else:
            break

def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

if __name__=="__main__":
    Main()
        
        
#MEJORAS. UNIXTIME to HORAS, MEJORAR EL DISPLAY DE LA DATA. FORMATEO DEL MENU. OPCIONAL: EXPORTAR DATOS A TXT. CONTROL DE ERRORES INPUT Y STATUS CODE.
    