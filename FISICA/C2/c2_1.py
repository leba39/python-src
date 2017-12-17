#!/usr/bin/env python3

#C2. EJERCICIO 1.
#INTERPRETE DE PYTHON: ANACONDA
#MODULOS USADOS: NUMPY Y MATPLOTLIB

from numpy import zeros           #from numpy import * Importa todas sus funciones. Es equivalente a hacer import numpy a secas.
import matplotlib.pyplot as plt   #importamos una funcion de la libreria matplotlib y le asignamos un nombre para usar en el resto de nuestro codigo.
                                  #por ejemplo podiamos haber hecho import numpy.zeros as matriz0s y usar este nombre para llamarla.

def sumatorio(lista,indice,modo):
#FUNCION CREADA EN PARTICULAR PARA EL APARTADO 1.  
    contador=0
    for i in range(len(lista)):
        if modo=="mayores" and lista[i]>lista[indice]:
            contador+=1
        elif modo=="menores" and lista[i]<=lista[indice]:
            contador+=1
    return contador

#INPUT: HAY QUE LEERLO DESDE UN ARCHIVO

archivoInput=open("datac2_1.dat","r")            #CREAMOS EL OBJETO ARCHIVOINPUT QUE DE MOMENTO ES UN ARCHIVO ABIERTO EN LA RUTA DADA Y EN MODO 'READ'.
v=archivoInput.read()                            #Leemos el contenido de ARCHIVOINPUT y metemos su contenido en la variable v.
archivoInput.close()                             #IMPORTANTE. SIEMPRE HAY QUE CERRAR EL OBJETO-ARCHIVO DESPUES DE SU LECTURA/ESCRITURA/ETC.

#Ahora 'v' es una cadena de texto(string) tal y como aparece en nuestro archivo. Mejoras que se le puede hacer a la apertura del archivo pues con os.path exists.
print(v)

#DESARROLLAMOS LO QUE PIDE EL EJERCICIO - C H I C H A -

listav=v.split()                  #Creamos la variable listav para convertir la cadena de texto con los numeros y espacios en una lista de elementos (str) por separado.
n=len(listav)                     #le asignamos a n la longitud de la lista, es decir; 'n' contiene el nº de cifras en el archivo.
Vint=[]                           #Creamos una lista vacia que contendra los valores del vector listav pero como ENTEROS INT.
for i in range(n):
    Vint.append(int(listav[i]))

   #APARTADO 1
w=zeros(n)                        #Nos crea una matriz 1xn es decir, un vector de 0's de la longitud dada.
for i in range(n):
    if i%2==0:
        w[i]=sumatorio(Vint,i,"mayores")
    else:
        w[i]=sumatorio(Vint,i,"menores")

print(w)    #Podemos observar que nos imprime un array con el resultado correcto pero de numeros decimales. Eso es porque la funcion zeros inicializa la matriz
            #o vector con el tipo de data float64. Si queremos solo enteros podemos prescindir de la funcion de numpy y del modulo en si e inicializar una lista
            #de 0*n elementos como ya tenemos hecho muchas veces.
    #APARTADO 2
z=zeros(n)
for i in range(n):
    sumamaximos=0#Esta variable la ponemos a cero cada vez que pasemos al siguiente elemento del vector Z para guardar en él el siguiente maximo de la cupla (Vint,w)
    for j in range(i):#El sumatorio del segundo apartado dice que hay que sumar el maximo de la tupla(Vint,w) de todos los elementos j menores que i(posicion del actual elemento del vector z)
        sumamaximos+=max(Vint[j],w[j])
    z[i]=sumamaximos#Despues de terminar el sumatorio podemos asignar el valor del elemento del vector Z[i] y se pasaria a la siguiente iteracion.

print(z)   #Misma observacion que con w.

#OUTPUT: NOS PIDEN GRAFICAR LOS VECTORES.
barraX=list(range(n))
#configuramos el plot.
plt.plot(barraX,w,"sr-",z,"sb-")
plt.xlabel("Indices")
plt.ylabel("Vectores")
plt.title("Vectores w y z")
plt.grid(True)
#lo guardamos y lo mostramos. importante guardar antes de hacer el show() porque si no matplotlib cierra el objeto-grafica despues de mostrarlo y ya no queda nada para guardar.
plt.savefig("grafica1.png")
plt.show()
        


        
        
#ARREGLAR EL SUM
