"""
EJERCICIO C3.2
INTERPRETE: ANACONDA
MODULOS   : RANDOM, NUMPY(OPCIONAL)
~~~~~~~~~~~~~~~~~~~~
"""
from random import randint
from numpy import argmax

#I N P U T: leer entero y guardarlo
resp=""
print("Introduzca un entero:")
while not (resp.isdigit()):
    resp=input(">")
n=int(resp)

#D E S A R R O L L O:
#1)Vector v aleatorio de orden n

#Manera 1: COMPRESION DE LISTAS
v_1=[randint(5,15) for v_i in range(n)]      
#Manera 2: CON BUCLES
v_2=[0]*n
v_3=[]
for i in range(n):
    v_2[i]=randint(5,15)
    v_3.append(randint(5,15))


#2)Diferencia maxima entre consecutivos del vector.
    
#cremos otro vector vacio que será del orden n-1 que contenga en valor absoluto estas diferencias.
#luego miraremos en este donde esta el maximo y en que posicion.
    
dif_1=[]
dif_2=[0]*(n-1)

for i in range(n-1):
    dif_1.append(abs(v_1[i]-v_1[i+1]))
    dif_2[i]=abs(v_1[i]-v_1[i+1])
#Son dos maneras de hacer lo mismo. print(dif_1==dif_2) sera TRUE

maxdif=max(dif_1)
#Manera corta: usando NUMPY
indice_1=argmax(dif_1) #devuelve 2
#Manera larga: sin usar el modulo numpy

for i in range(len(dif_1)):
    if dif_1[i]==maxdif:
        indice_2=i

#O U T P U T
#3)Si esta maxima diferencia es >5 decir que los datos son dispersos.
print("Vector aleatorio orden %i:"%(n))
print(v_1)
print("Maxima diferencia absoluta:\t%i\tentre numeros\t%i-%i"%(maxdif,v_1[indice_1],v_1[indice_1+1]))
if maxdif>5:
    print("Datos dispersos.\a")