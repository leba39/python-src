#!/usr/bin/env python3
#IMPORTANTE. PARA DESARROLLOS MAS SIMPLES EMPEZAR A USAR NUMPY: loadtext,find...


#C2. EJERCICIO 3.
#INTERPRETE DE PYTHON: ANACONDA
#MODULOS USADOS: MATPLOTLIB
import matplotlib.pyplot as plt

#I N P U T: Leemos del fichero. NUEVA FORMA. NO HAY QUE CERRAR.

with open("datac2_3.dat","r") as archivoIN:
    contenido=archivoIN.read().splitlines()
    #Nos lee el contenido y el metodo splitlines lo divide en varios elementos,segun el separador \n de una lista.
    #OTRA FORMA.
    """contenido=archivoIN.readlines()
    matrizAstr=[linea.strip("\n") for linea in contenido]"""
    
#CONVERTIMOS LA LISTA CON LAS CADENAS DE TEXTO POR FILAS EN UNA MATRIZ DE ENTEROS.
matrizA=[]    #Creo una matriz/array vacia. Contendra dentro a su vez otras listas.
filadeA=[]    #nos servira para ir rellenando la matriz A.

for fila in contenido:
    linea=fila.split()
    for caracter in linea:
        filadeA.append(int(caracter))
    matrizA.append(list(filadeA))
    del filadeA[:]   #TAMBIEN PODRIA HACER filadeA[:]=[]

#AHORA YA TENEMOS LA MATRIZ DE ENTEROS A Y PODEMOS TRABAJAR.
#D E S A R R O L L O    C H I C H A
    #apartado1
fil=len(matrizA)#COMO SE QUE LA MATRIZ ES CUADRADA NO TENDRE QUE AVERIGUAR EL TAMAÑO DE CADA FILA
print("\t-MULTIPLOS DE TRES EN LA MATRIZ LEIDA-")
cont=0
for i in range(fil):
    for j in range(fil):
        if matrizA[i][j]%3==0:
            print("Indice %s,%s:\t%s"%(i,j,matrizA[i][j]))
            cont+=1
print("Numero de multiplos de tres:\t%s"%(cont))
    #apartado2
v=[0]*fil
suma=0
for i in range(fil):
    for j in range(fil):
        for k in range(fil):
            if (j<i) and (k<i):
                suma+=matrizA[j][k]
    v[i]=suma
    suma=0
     #apartado3
print("\t-ELEMENTOS DE V SUCESIVOS CON SUMA MENOR QUE CIEN-")
i=0
suma=v[i]
while suma<100 and i<(fil-1): #fil-1 es la dimension del vector V si no contamos el 0. 
   print(v[i],end="\t")       #Asi, de no sumar los elementos de V mas de 10.
   i+=1                       #el bucle no daria error cuando intentase acceder a un elemento
   suma+=v[i]                 #del vector V con un indice mayor a su longitud.    
                                   
                          
   
#O U T P U T: Apartado 4, GRAFICAR. LO DE SIEMPRE.   
barraX=list(range(fil))
#configuramos el plot.
plt.plot(barraX,v,"*g-")
plt.xlabel("Indices")
plt.ylabel("Valores")
plt.title("Vector V")
plt.grid(True)
#lo guardamos y lo mostramos. importante guardar antes de hacer el show() porque si no matplotlib cierra el objeto-grafica despues de mostrarlo y ya no queda nada para guardar.
plt.savefig("grafica3.png")
plt.show()