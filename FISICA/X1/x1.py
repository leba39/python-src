#!/usr/bin/env python3

#EXAMEN 1.
#INTERPRETE DE PYTHON: ANACONDA
#MODULOS USADOS: NUMPY Y MATPLOTLIB
import matplotlib.pyplot as plt
import numpy


#ejercicio1
x=numpy.linspace(1,3,20)   #argumentos INICIO, FIN, Nº elementos.
y=x**2*numpy.exp(-x**2)    #creamos el vector y segun enunciado. Ver la utilidad de importar numpy como from numpy import * para no tener que poner nada delante.
plt.plot(x,y,"*b-")
plt.xlabel("Indices");plt.ylabel("Valores");plt.title("Vector Y");plt.grid(True)
plt.show()

#ejercicio2               simplemente creamos los vectores para hacer el polyfit
x=[1,2,3,4,5]
y=[4,2,-5,-3,-1]
polinomio=numpy.polyfit(x,y,4)  #argumentos: dos primeros vectores sobre los que realiza el ajuste y el grado del mismo.

print(polinomio)

#EXTRA: como hariamos este ejercicio si nos dieran un txt con la pareja de coordenadas de cada punto en cada linea??
#       o si nos introdujeran cada pareja de coordenadas (punto) por teclado?

#ejercicio3

matrizA=numpy.loadtxt("datos_exame.txt","int")    #Dos argumentos, la direccion del archivo y el tipo de data a leer.
print(matrizA)                                    #Esta funcion de numpy ya se encarga del formateo de los datos leidos. Devuelve en matrizA un array.


def operaciones(m):                               #creamos una funcion que toma como argumento una matriz
    
    sumam3=numpy.sum(m[m%3==0])                   #utilizando la funcion sum de numpy que permite hacer expresiones regulares (RE) dentro de los corchetes
    x=numpy.sum(m,axis=1)
    y=numpy.sum(m,axis=0)
    
    contador=0
    for i in range(len(m)):
        for j in range(len(m)):
            if i!=j and m[i][j]==m[j][i]:
                contador+=1
            
            
    return [sumam3,x,y,contador]
    

res=operaciones(matrizA)
print(res)

print("Suma de los multiplos de 3:\t%i\nVector X:\t%i\nVector Y:\t%i\nNumero de elementos aij=aji:\t%i"%(res[0],res[1],res[2],res[3]))
      
n=len(matrizA)
b=numpy.zeros([n,n])
for i in range(n):
    for j in range(n):
        if (i%2==0) and (j%2==0):
            b[i,j]=res[1][i]*res[2][j]
        elif (i%2==1) and (j%2==1):
            b[i,j]=res[1][i]+res[2][j]
        else:
            b[i,j]=res[1][i]/res[2][j]
            
print("Matriz B:\n")
print(b)

sumatorio=0
i=0
z=numpy.ravel(matrizA)           #Coje cualquier tipo de array y devuelve un vector compuesto de sus elementos. Es parecido a la funcion numpy.flatten

while (sumatorio<20) and (i<len(z)): #o i<n*n,n**2
    sumatorio+=z[i]
    i+=1
    
print("Suma de elementos menores que veinte en el vector Z:\t%i\nNumero de elementos sumados:\t%i"%(sumatorio,i))