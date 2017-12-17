"""
EXAMEN 2 - ENERO 2016

INTERPRETE : ANACONDA v3.6 (YA QUE NOS HACE FALTA LA LIB. MATPLOT)
MODULOS: MATPLOTLIB, NUMPY (OPCIONAL)
~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#LIBRERIAS
import matplotlib.pyplot as plt
import numpy

#CONSTANTES
m=5

#FUNCIONES
def calculos(vector):
    #Como calcular el valor medio de un array/vector/lista ya que lo demas será COMUN.
        #Con NUMPY
    valorm=numpy.mean(vector)
        #Sin NUMPY
    n=len(vector)
    valorm1=sum(vector)/n #OJO! SUM es la funcion de python que suma los elementos de objetos iterables (listas etc)
                          #Existe tambien una funcion SUM en numpy que hace exactamente los mismo.
    suma=0
    for i in range(n):
        suma+=vector[i]
        if (suma>valorm):
            break
    nsumados=i+1
    nvector=vector[0:nsumados]
    
    return [nsumados,nvector]  #podriamos hacerlo directamente return[i+1,vector[0:i+1]]
                               #Esta funcion devuelve una LISTA cuyos elementos son el primero
                               #un numero (tipo INT) y el segundo un vector (es decir, otra lista de enteros)
    
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""    
#I N P U T: Leer por teclado tres numeros enteros.

print("Introduzca X, Y, Z:\t")
    #Podemos leerlo de una tirada (enteros separados por espacios) o pedirlos de uno a uno. CONTROL ERRORES
    #1.a
numeros=[]
resp="YOINICIOBUCLE"
i=0
while (not resp=="") or (i<3):
    if (i==3):
        break     #o hago un break o hago resp="" cualquiera vale.
    else:
        resp=input(">")
        if resp.isdigit():
            numeros.append(int(resp))
            i+=1
x,y,z=numeros[0],numeros[1],numeros[2]

    #1.b
resp1="YOSOLOINICIOBUCLE"
while not resp1.isdigit():
    resp1str=input("Separado por espacios >")
    resp1num=resp1str.split()
    if (len(resp1num)>2):
        resp1="".join(resp1num)
    else:
        resp1="VUELTABUCLE"
        
x1=int(resp1num[0])
y1=int(resp1num[1])
z1=int(resp1num[2])

#D E S A R R O L L O:

#pre: construir matriz cuadrada A orden m con la regla Aij dada.

    #Con NUMPY
a=numpy.zeros([m,m])
    #Sin numpy
a_1=[None]*m
for i in range(m):
    a_1[i]=[0]*m
    #aij    
for i in range(m):
    for j in range(m):
        a[i,j]=(i+1)*x+(j+1)*y+(i+1)*(j+1)*z          #a[i][j] tambien es valido
        a_1[i][j]=(i+1)*x1+(j+1)*y1+(i+1)*(j+1)*z1
        
#1)Mostrar numero de elementos pares de A y la suma de los elementos cuyo valor es mayor a 20.
        
    #Con NUMPY
pares=numpy.where(a%2==0)     #where devuelve una matriz que contiene las coordenadas de los elementos
npares=len(pares[0])          #que cumplen la condicion logica dada (a%2==0 en este caso.) por eso el
                              #numero de pares (que es lo que piden) es la longitud del vector [0].
                              # EJ: pares=[[1,2],[3,4]] -> Tendremos dos puntos con Coordenadas (1,3) (3,4)
                              #hallar el numero de puntos se podria hacer con len(pares[0]) o len(pares[1])
nsuma=numpy.sum(a>20)       #numero valores mayores que 20
suma=sum(numpy.extract(a>20,a)) #suma de los valores mayores que 20 (primero los extraemos)

    #Sin NUMPY
npar=0
suma1=0
for i in range(m):
    for j in range(m):
        if (a[i,j]%2==0):
            npar+=1
        if (a[i,j]>20):
            suma1+=a[i,j]
#2)Plotear la matriz A como mapa de calor. titulo: mapa de calor de A.
plt.figure(1)
plt.clf()
plt.imshow(a)
plt.title("Mapa de calor de A.")
plt.show()

#3)Convertir matriz A por columnas en un vector v. Ajustar v a un polinomio orden 2. Plotear v/polinomio(ejex:w).
    
#Convertir la matriz en vector por columnas. Crear vector complementario w.
    #Con NUMPY
v=numpy.ravel(a.T)  #Ravel de una matriz por defecto lo hace por filas. Si le mandamos la transpuesta
                    #lo hará por columnas.

w=numpy.arange(len(v)) #arange crea un array/vector/lista entre 0 y el rango dado.

    #Sin NUMPY
v_1=[]

i,j=0,0              #variables auxiliares
for k in range(m):   #Hago un bucle segun el orden de la matriz ya que appendearé tantas columnas.
    i=0              #reseteo i->filas
    while (i!=(m-1)):#mientras no llegue a la ultima fila
        v_1.append(a_1[i][j])  #appendeo elemento
        i+=1                   #sumo fila
    j+=1             #avanzo columna
    
w_1=[x for x in range(len(v_1))]  #Compresion de listas. Es equivalente a arange() de numpy.

#Ajustar polinomio.
coefpolinomio=numpy.polyfit(w,v,2) #GRADO 2. Argumentos:(vector dominio, vector imagen, grado)
polievaluado=numpy.polyval(coefpolinomio,w) #evaluamos el polinomio al vector dominio. Devuelve f(w).

#Ploteamos nueva grafica.
plt.figure(2)
plt.clf()
plt.plot(w,polievaluado,"-g")
plt.plot(w,v,"b*")
plt.title("Vector V. Polinomio ajustado GRADO 2.")
plt.xlabel("Vector W")
plt.ylabel("Valores")
plt.grid(True)
plt.show()

#4)Crear funcion calculos tal que devuelva el numero de elementos de 'v' necesarios para superar su valor medio
#  y otro vector con estos elementos.

[elementos,vector]=calculos(v)
"""TAMBIEN SERIA VALIDO: (POR SI ES MAS FACIL DE COMPRENDER ASI)

resultados=calculos(v)    #resultados sera la lista que contiene a su vez un numero  y otra lista.
elementos=resultados[0]   #el INT
vector=resultados[1]      #el vector
"""

#O U T P U T: Imprimir por pantalla y guardar en un fichero segun la condición dada.
print("MATRIZ:")
print(a)
print("En forma de vector por columnas (v):")
print(v)
print("Numero de elementos a sumar para superar el valor medio de v: %i"%elementos)
print("Vector con dichos elementos:")
print(vector)

#guardamos en un fichero de 'n' lineas siendo n la longitud de 'vector'. En las lineas pares
#el elemento correspondiente de 'vector'. En las impares, el de la diagonal de la matriz A.
n=len(vector)

    #Con NUMPY
diagonal=numpy.diag(a)
    #Sin NUMPY
diagonal1=[]
for i in range(m):
    for j in range(m):
        if (i==j):
            diagonal1.append(a[i][j])
            
#Tuneamos el vector que tenemos que escribir en un fichero segun nos indican.
            
for i in range(n):
    if (i%2==1):  #elemento IMPAR -> linea impar
        vector[i]=diagonal[i]
        
#ESCRIBIMOS EL FICHERO.
        
    #Con NUMPY
try:
    
    numpy.savetxt("resultadosNUMPY.txt",vector,"%5d")  #Tercer argumento opcional. Es para formateo de los datos
                                                       #En este caso indicamos que la data es de tipo "DOUBLE"
                                                       #ya que NUMPY trabaja en sus arrays siempre con decimales
                                                       #mientras que el numero delante de la letra indica
                                                       #la precision. (nºdecimales %.2 etc)
except IOError:
    print("Error guardando fichero de resultados.")
    
    #Sin NUMPY:
try:
    with open("resultados.txt","w") as archivosalida: 
        archivosalida.write(str(vector))              #Convertimos a string el vector para poder escribirlo.
"""PROBAR EN CASA COMO ESCRIBIRIAMOS LINEA A LINEA.
    Posible solucion. dentro del open
    for i in range(n):
        archivosalida.writelines(str(vector[i]))"""

except:
    print("Error guardando fichero de resultados.")

"""
Los bloques TRY y EXCEPT es la primera vez que los vemos:
Son bloques que conducen/manejan el control de errores y el trato de excepciones y como su nombre indican hacen
precisamente eso -probar y redirijir-. Prueban cierto bloque de codigo y si este da un error al compilar desvia este error
y ejecuta lo que se encuentra en el bloque except. Podemos particulalizar los bloques except indicando distintos
tipos de fallos de compilacion para tener una respuesta unica a cada uno de ellos.

EJEMPLO PRACTICO:

a="tres"
try:
    n=int(a)
except ValueError:
    print("Esa variable no es un digito melón!!")

Como ves, podemos hacer un except sin nada mas (sin 'argumento' si prefieres) y encauzara cualquier tipo
de error que surja. Esto suele ser mala practica de programador ya que encauzamos distintos tipos de fallo
a uno sola respuesta. Un buen programador maneja las posibles excepciones individualmente.
ValueError,TypeError,IndexError... son algunas que ya te sonarán
"""
    

