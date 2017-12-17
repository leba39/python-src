#!/usr/bin/env python3
#ej: [5]
#C2. EJERCICIO 5.
#INTERPRETE DE PYTHON: ANACONDA
#MODULOS USADOS: MATPLOTLIB, RANDOM.
import matplotlib.pyplot as plt
from random import randint

#I N P U T: Leemos un numero por teclado
print("\t-INTRODUZCA EL TAMAÑO DE LA MATRIZ CUADRADA-")
resp=""    #Inicio la variable con tipo de data NADA para que me entre en el while la 1era vez.
while not resp.isdigit():
    resp=input(">")
n=int(resp)

#D E S A R R O L L O: CHICHA
    #apartado1:crear matriz random orden n
matrizA=[]
for i in range(n):
    fila=[randint(0,100) for i in range(n)]
    matrizA.append(fila)
print("Matriz de orden %s aleatoria:\n%s"%(n,matrizA))
    #apartado2:crear y mostrar vector x con todos los elementos de matrizA hasta el 1ero en repetirse.
x=[]
fin=False
for i in range(n):   #SE PUEDE HACER DE UNA MANERA SIMILAR CON LA FUNCION any() QUE VIENE POR DEFECTO.
    if not fin:
        for j in range(n):
            if not matrizA[i][j] in x:
                x.append(matrizA[i][j])
            else:
                fin=True
                break
print("Vector X de numeros no-repetidos:\n%s"%(x))
    #apartado3:suma elementos pares de A.
suma=0
y=[]
for i in range(n):
    for j in range(n):
        y.append(matrizA[i][j])
        if matrizA[i][j]%2==0:
            suma+=matrizA[i][j]
print("Suma de los elementos pares de la matriz aleatoria:\t%s"%(suma))

#O U T P U T: GRAFICAR
    #apartado4:convertir matrizA en vectorY y graficar.APROVECHE EL FOR DE ANTES PARA RELLENAR 'y'.
#configuramos plot
plt.plot(sorted(y),"*r")
plt.xlabel("Indices")
plt.ylabel("Valores")
plt.title("Vector Y")
plt.grid(True)
#lo guardamos y lo mostramos. importante guardar antes de hacer el show() porque si no matplotlib cierra el objeto-grafica despues de mostrarlo y ya no queda nada para guardar.
plt.savefig("grafica5.png")
plt.show()


#ATENCION: DIFERENCIA ENTRE USAR SORTED(LISTA) QUE DEVUELVE UNA LISTA ORDENADA Y EL METODO LISTA.SORT()
#          NO DEVUELVE NADA, SI NO QUE REEMPLAZA LA POSICION DE LOS ELEMENTOS EN LA PROPIA LISTA DADA
#          DE ESTA MANERA, TENDRIAMOS QUE HACER y.sort y luego plotear y o ploter directamente sorted(y)