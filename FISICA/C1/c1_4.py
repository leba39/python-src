#!/usr/bin/env python3

#EJERCICIO C1.4
#EJEMPLO 1234

#INPUT
print("\tIntroduzca el numero a analizar:",end="")
num=""                                                 #Para que entre en el bucle la 1era vez la iniciamos asi. Tambien podria usar None.
while not num.isdigit():
    num=input(">")
num=int(num)
#Preparamos series y contadores si hace falta (ejercicio resulta usa nc??)
cifras=[]
#Bucle para ir separando las cifras una a una.
while num>0:
    cifras.append(num%10)                              #Agregamos(append) el resto de la division de num entre 10.
    num//=10                                           #Actualizamos nuestro numero y lo preparamos para la siguiente iteracion. (num=num//10) DIVISON ENTERA!!
    print(cifras[-1])                                  #Hago un print al ultimo elemento que acabo de agregar; es decir, el que acabo de appendear.
#Hay que recordar que append pone la variable que queramos como la ultima en la lista a la que se lo apliquemos.
#Tambien podriamos eliminar este print del bucle y fuera de el imprimir la lista como tal cifras: ejemplo [4,3,2,1] pero dada la vuelta cifras[::-1]
#O hacer un bucle while o for para que vaya elemento a elemento imprimiendo de mas a menos. como se quiera. (aqui no tendriamos los corchetes)

#BUCLE PARA SACAR PARES E IMPARES. Con un solo bucle podemos realizar ambas operaciones (Pero tendriamos problemas para imprimir los elementos por separado)
print("-PARES-:")    
for i in range(len(cifras)):
    if (cifras[i]%2)==0: #PAR    
        print(cifras[i])
print("-IMPARES-:")    
for i in range(len(cifras)):
    if (cifras[i]%2)==1: #IMPAR    
        print(cifras[i])
    
    
"""
#FORMA RAPIDA DE HACER EL EJERCICIO.
print("\tIntroduzca el numero a analizar:",end="")
num=""                                                 #Para que entre en el bucle la 1era vez la iniciamos asi. Tambien podria usar None.
while not num.isdigit():
    num=input(">")
    
CIFRAS=list(num)

for i in range(len(CIFRAS)):
    print(CIFRAS[len(CIFRAS)-i])

LOS MISMOS BUCLES PARA LO DE PAR E IMPAR
.
.
.
.
"""