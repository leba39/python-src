#!/usr/bin/env python3

#EJERCICIO C1.2
#Preparamos las variables
sumatorio=0
serie=[]

print("Introduzca los numeros de su serie:")
#Preparamos la serie con el input del usuario.
while sumatorio <= 100:
    num=int(input())
    sumatorio+=num
    serie.append(num)
    
dim=len(serie)
#Inicializamos un array con zeros de longitud la dimension de serie..
v=[0]*dim
#Vamos actualizando los elementos de este array V segun las reglas dadas.
for i in range(dim):
    if serie[i]>10:
        v[i]=1
    elif serie[i]<-10:
        v[i]=-1
    else:
        v[1]=100

#HACEMOS PRINT DE LOS RESULTADOS.
print("Numeros leidos:\t%i\nLista de numeros leidos:\t%s\nLista resultante:\t%s" % (dim,serie,v))
print("Numeros leidos:\t"+str(dim)+"\nLista de numeros leidos:\t"+str(serie)+"\nLista resultante:\t"+str(v))


