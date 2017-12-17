"""
EXAMEN 4 - JULIO 2015
INTERPRETE: ANACONDA (PYPLOT)
MODULOS: NUMPY,MATPLOT,SCIPY,SYMPY,RANDOM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#MODULOS
import sympy
import numpy
import scipy.interpolate as interpolar
import matplotlib.pyplot as plt
from random import randint

"""
#1)CALCULAR EL LIMITE DE UNA INTEGRACION DADA:
    #SON TODO FUNCIONES DE LA LIBRERIA SYMPY!!
    #funcion  : sympy.sin(t)/t
    #integral : sympy.integrate(funcion,(t,1,x))
limite = sympy.limit(sympy.integrate(sympy.sin(t)/t,(t,1,x)),x,oo)


#2)DADOS UN CONJUNTO DE PUNTOS CALCULAR EL VALOR DE 'Y' INTERPOLADO CON 'X'
#  SOBRE LOS VALORES DE 1 A 5 CON ESPACIADO DE 0.2

x=numpy.array([1,2,3,4,5])
y=numpy.array([4,2,-5,-3,-1])
barra_x=numpy.arange(1,5,0.2)
f=interpolar.interp1d(x,y,"cubic")
eval=f(barra_x)

FE DE ERRATAS
OJO: EN EL APARTADO DOS TUVE QUE IMPORTAR LAS FUNCIONES DEL GRUPO INTERPOLATE DE LA LIBRERIA SCIPY
     DE LA MISMA MANERA QUE HAGO import matplotlib.pyplot as plt CUANDO QUIERO IMPORTAR SOLO EL GRUPO
     DE FUNCIONES QUE ME SIRVEN PARA GRAFICAR. ESTO LO HAGO YA QUE scipy.interpolate.interp1d(args) NO
     CONSIGO QUE ME FUNCIONE.
     EN EL APARTADO UNO LAS FUNCIONES PARA INTEGRAR, HACER EL LIMITE E INCLUSO PARA EL SENO DEPENDEN DE
     LA LIBRERIA SYMPY Y NO DE LA NUMPY COMO HICIMOS EN TU CASA.

"""
#EJERCICIO 3

#FUNCIONES

def calcula(m):
    n=len(m)
    
    if n>5:
        #DEFINICION
        sumatorio=0
        for i in range(n):
            sumatorio+=m[i][i-n-1]   #segun PDF
    else:
        #TRAZA
        #numpy
        sumatorio=numpy.trace(m)
        #sin numpy
        sumatorio_1=0
        for i in range(n):
            for j in range(n):
                if (i==j):
                    sumatorio_1+=(m[i][j])

    return sumatorio    #Devolvemos un solo resultado, una variable.


#INPUT
print("Orden de la matriz:")
resp="INICIOBUCLE"
while not resp.isdigit():
    resp=input(">")
n=int(resp)
#CREAMOS Y DEFINIMOS MATRIZ
    #Numpy
matriz=numpy.zeros([n,n])
    #Sin numpy
matriz_1=[None]*n
for i in range(n):
    matriz_1[i]=[0]*n
    
for i in range(n):
    for j in range(n):
        matriz[i][j]=numpy.random.randint(n)+1 #randint de numpy devuelve (0,n-1)
        matriz_1[i][j]=randint(1,n)            #randint de random permite poner intervalo
    
matriz_2=numpy.random.random([n,n])*n+1

"""
Hemos creado tres matrices con tres procesos distintos:

'matriz' se crea con la ayuda de la funcion de numpy 'zeros' para crearla y en el bucle FOR
se llena de valores enteros con la funcion randint del grupo random de NUMPY.

'matriz_1' se crea como una pseudomatriz lista-de-listas y se llena en el bucle FOR con la ayuda
de la funcion randint del modulo RANDOM (ver importaciones)

'matriz_2' se crea y define directamente con la funcion random del grupo random de la libreria de NUMPY!

    DIFERENCIAS Y SIMILITUDES:

numpy.random.randint() [NUMPY] y randint() [RANDOM] se comportan de manera practicamente equivalente.
numpy.random.random() [NUMPY] ACEPTA en los parentesis que le metamos el tamaño -por ejemplo- de una matriz
y nos devolvera una matriz con CADA UNO DE LOS ELEMENTOS con un valor aleatorio entre 0 y 1.
Si le metemos entre parentesis el tamaño de un vector [n] nos devolvera ese vector lleno con valores aleatorios.

La libreria/modulo RANDOM tambien tiene otra funcion que se llama RANDOM y la podriamos llamar asi:
import random
x=random.random()

Si te preguntas cual es la diferencia es que esta ultima SOLO DEVUELVE UN NUMERO entre 0 y 1 y JAMAS aceptara
NI FUNCIONARA el intentar meterle un tamaño de matriz [n,n] para que rellene todos los elementos.

Es la misma historia que pasa con el numpy.all/sum y la funcion all/sum de PYTHON que ya te tengo dicho.
"""

#GUARDAR MATRIZ
    #Numpy
try:
    numpy.savetxt("matriznpy.txt",matriz_2,"%10.2f")
except IOError:
    print("Hubo un error escribiendo el archivo.")
    
    #Sin numpy
try:
    with open("matriz.txt","w") as salida:
        salida.write(str(matriz_2))
        """PODRIA REFINAR MAS ESTE BLOQUE DE CODIGO SI QUIERO IMPRIMIR DE MANERA FORMATEADA LA MATRIZ
        for i in range(n):
            j=0
            while j<n:
                salida.write(str(matriz[i][j])+"\t")
                j+=1
            salida.write("\n")
        
        """
except:
    print("Hubo un error guardando la matriz.")


#CREAR FUNCION CALCULA, LLAMARLA Y PRINTEAR RESULTADO:

resultados=calcula(matriz)
print("Matriz:")
print(matriz)
print("Suma:",end="\t")
print(resultados)

#SUMA LA MATRIZ. SI ES >1 DIVIDELA POR DOS HASTA QUE NO LO SEA. PLOTEA LA SUMA DE CADA ESTADO INTERMEDIO.

    #numpy
suma=numpy.sum(matriz)   #suma de la matriz
vsum=[]                  #vector vacio que contendra en cada iteracion la nueva suma resultante
contador=0               #contador de iteraciones
while (suma>1):
    contador+=1            #actualizamos contador
    vsum.append(suma)      #appendeamos
    matriz=matriz/2        #actualizamos matriz
    suma=numpy.sum(matriz) #actualizamos suma

    #sin numpy
suma_1=sum(sum(matriz))
vsum_1=[]
cont=0
while (suma_1>1):
    cont+=1
    v_sum_1=suma_1
    matriz/=2
    suma_1=sum(sum(matriz))

"""NOTAS:
POR QUE HAGO SUM SUM? SUM es una funcion de PYTHON y si pruebas a meterle una lista no funciona
lista=[1,2,3] s=sum(lista) da fallo TypeError
Pero como 'matriz' es de tipo ARRAY (numpy) lo acepta. Lo que devuelve es el vector suma por columnas.
Luego para obtener la suma total le vuelvo hacer a este ultimo otro sum.

-PERO ABEL NO ERA QUE LAS FUNCIONES PROPIAS DE PYTHON NO TRABAJABAN ELEMENTO A ELEMENTO Y DEVOLVIAN SOLO NºS?

Las funciones all/sum/any pueden trabajar con objetos iterables pero solo con uno y no permiten hacer una
comparacion entre dos elemento a elemento.
Es cierto que mayormente solo devuelven 1 escalarar o 1 boolean etc pero -y esto no lo sabia- parece que SUM
de PYTHON devuelve un vector suma de columnas si lo que le mandamos es un array tipo numpy.
(como ves yo le mandé matriz a ambas)

Si este apartado de "SIN NUMPY" lo hiciese con matriz_2 que SI que es una PSEUDO MATRIZ LISTA-DE-LISTAS:
El SUM de PYTHON ya no funciona. Da TYPE ERROR.
Como lo haria?

def sumatorio(matriz_2):
    n=len(matriz_2)
    suma=0
    for i in range(n):
        for j in range(n):
            suma+=matriz_2[i][j]
            
    return suma
    
y asi la llamo cuando me haga falta en el bucle while.
"""
#OUTPUT: Prints Y plots
print("Numero de iteraciones:\t%i\nSuma nueva:\t%f"%(contador,suma))
#Le pongo %f porque 'matriz' tiene flotantes. 'matriz_2' tambien pero 'matriz_1' solo enteros (usaria %i)

barra_x=numpy.arange(len(vsum))
#Si lo quiero hacer sin numpy:
#Un barra_x=[int x for x in range(len(vsum))]  Equivalente a arange. Creamos vector.
#Un barra_x=range(lenvsum) tambien seria valido en este caso, aun que no lo recomiendo. Usar vector siempre.
plt.figure(1)
plt.clf()
plt.plot(barra_x,vsum,"r*-")
plt.xlabel("Iteraciones")
plt.ylabel("Suma")
plt.title("BUCLE")
plt.grid(True)
plt.savefig("bucle.png")
plt.show()





