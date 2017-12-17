#!/usr/bin/env python3

#EJERCICIO C1.1
#EJEMPLO[[1,2,4,6][4,3,7,5][4,8,0,5] [6,4,7,1]]

DIM=4   #Tambien podriamos leer la len(matriz) al ser cuadrada.
print("\tIntroduzca su matriz por filas; separando cada elemento por espacios:")

#Creamos la matriz por filas ayudandonos de list comprehension. EJEMPLOS.
#Esta es otra manera de crear una matriz introduciendo todos los elementos por fila al mismo tiempo
matriz=[]
for i in range(DIM):
    matriz.append([int(j) for j in input().split()])


#Inicializamos variables:
sumapar=0
contimpar=0
#BUCLE que itera elemento a elemento y con ellos construiremos los datos pedidos.
for i in range(DIM):
    for j in range(DIM):
        #dentro de estos dos bucles ya conseguimos iterar elemento a elemento, v.gr., matriz[i][j]
        if (matriz[i][j]%2)==0:
            sumapar+=matriz[i][j]
        else:
            contimpar+=1
#Imprimimos.
print("Suma de elementos pares es %i y el numero de elementos impares es %i" % (sumapar,contimpar))