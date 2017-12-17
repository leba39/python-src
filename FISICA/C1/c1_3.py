#!/usr/bin/env python3

#EJERCICIO C1.3
#EJEMPLO x=[1,2,3,4,5,6]


print("\tIntroduzca uno a uno los elementos la lista que formarán la matriz. Cuando termine retorne en blanco.")
listausuario=[]
respuesta=None
#CREAMOS EL VECTOR/LISTA E INTRODUCIMOS LOS NUMEROS DEL USUARIO
while respuesta != "":
    respuesta=input(">")
    if respuesta.isdigit():
        listausuario.append(int(respuesta))               #ATENCION. De no hacer hacer como entera la respuesta
                                                          #Tendriamos un error en los bucles de abajo al ser str.
n=len(listausuario)
#Cuando empezemos a usar los modulos de numpy veremos que con sus funciones zeros y ones podemos crear facilmente matrices de las dimesiones que queramos.
#EJ. np.zeros(4,4) o np.arange(1,17).reshape(4,4) que crearia una matriz 4x4 con numeros ordenados del 1 al 16
matrizb=[[0 for col in range(n)] for fila in range(n)]    #En el PDF lo hace de una manera mas sencilla con un for que itera N veces
                                                          #y  que appendea 0*n elementos de cada vez.

#RESOLVIENDO CADA ELEMENTO DE LA MATRIZ:

for i in range(n):
    for j in range (n):                                   #A partir de aqui ya tenemos un par de bucles que nos pasan a traves de cada elemento de B[i][j]
        if i > j:
            matrizb[i][j]=sum(listausuario[:i+1])
        else:
            matrizb[i][j]=sum(listausuario[j:n])

#Imprimimos nuestra matriz fila a fila para que quede mas bonita.
for i in range(n):
    print(matrizb[i])

#Si no queremos los corchetes y las comas tambien podemos imprimir elemento a elemento poniendo espacios y haciendo secuencia de escape \n (nueva linea) en cada fila.
for i in range(n):
    cambiofila=True
    for j in range(n):
        if cambiofila:
            print("\n%i"%(matrizb[i][j]),end="\t")
            cambiofila=False
        else:
            print(matrizb[i][j],end="\t")