"""
SEGUNDO CONTROL DE PROGRAMACION - DICIEMBRE 2017

INTERPRETE: ANACONDA (PYPLOT)
MODULOS: MATPLOTLIB, NUMPY(OPCIONAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import numpy
import matplotlib.pyplot as plt

#FUNCION

def transforma(v):
    
    n = len(v)
        #numpy
    m = int(numpy.ceil((1+numpy.sqrt(1+8*n))/2)) #ceil de numpy devuelve decimal
        #sin numpy
    m_1 = (1+(1+8*n)**(1/2))/2 #le hago el ceil de forma casera con el round de python
    
    if (m_1-round(m_1)>0):     #si m_1 menos su redondeo es mayor que 0 tengo que sumar 1 para hacerle ceil
        m_1 = round(m_1+1)
    else:                      #si no lo dejo tal cual por que el round ya me dá el entero superior
        m_1 = round(m_1)       #round de python devuelve el entero si no le pasamos un segundo argumento
                               #que son el numero de decimales a redondear
    
    #VERIFICACION
    verificar = (m**2-m)/2   #podria usar m_1 indiferentemente
    
    if verificar >= n:
    #CREAMOS MATRIZ
            #numpy
        matriz = numpy.zeros([m,m])
        
            #sin numpy
        matriz_1 = [None]*m_1
        for i in range(m_1):
            matriz_1[i] = [0]*m_1
   
        """
        AQUI VIENE LA CHICHA DE LA FUNCION
        
        """
           #HICE EL MISMO ALGORITMO PARA NUMPY Y SIN EL. LO UNICO QUE ME AHORRO CON NUMPY
           #ES HACER EL TRIANGULO INFERIOR YA QUE LO PUEDO SUMAR COMO TRANSPUESTA.

        #TRIANGULO SUPERIOR/FILA
        i,j,k = 0,0,0
        while k < n: 
            j=i+1  #empezamos en la columna siguiente a la correspondiente de la diagonal en cada fila.
            while j<m_1 and k<n:
                matriz_1[i][j] = v[k]
                matriz[i][j] = v[k]
                k+=1                   #siguiente elemento
                j+=1                   #avanzo columna
            i+=1                       #avanzo fila

        
        #TRIANGULO INFERIOR/COLUMNA. Mismo proceso pero a la inversa
        i,j,k = 0,0,0
        matriz += numpy.transpose(matriz)  #le sumo la traspuesta. Asi me ahorro el siguiente WHILE (numpy)
        while k<n:
            i=j+1
            while i<m_1 and k<n:
                matriz_1[i][j]=v[k]
                k+=1
                i+=1
            j+=1
            
        #DIAGONAL
        for i in range(m_1):
            for j in range(m_1):
                if i==j:
                       matriz_1[i][j] = v[i]  #Elemento de la diagonal
                       matriz[i][j] = v[i]

        return matriz  #cualquiera de las dos vale
    else:
        exit("Hubo un problema!")  #si no se verifica que entra el vector salimos del programa directamente
    
    
    
    
    
                                    # M   A   I   N
#INPUT: ENTERO POSITIVO >= 10:
print("Introduzca un entero positivo mayor o igual a 10:")
resp = "BUCLE"
while not (resp.isdigit() and n>=10):
    resp = input()
    if resp.isdigit():
        n=int(resp)
    
#1) Vector de n elementos con serie Fibonacci:
    #numpy
v_fib = numpy.ones(n)   #tamaño conocido. Lo hago de 1's por que el eneunciado dice que el elemento x_0
                        #debe ser 1. (hay series que la empiezan en 0,1,1,2,3,5....).     
    #sin numpy
v_fib1 = []             #La podria hacer de [1]*n y me ahorraria trabajo pero se puede hacer perfectamente
                        #como vector libre e ir appendeando

    #FIBONACCI
for i in range(n):
    if (i>1):
        v_fib[i] = v_fib[i-1] + v_fib[i-2]
        v_fib1.append(v_fib1[i-1] + v_fib1[i-2])
    else:
        v_fib1.append(1) #esto lo hago para poner los dos primeros 1's de la serie.
        #v_fib[i]=1      Esto lo haria tambien si hiciese numpy.zeros en vez de ones


#2) FUNCION TRANSFORMA

a = transforma(v_fib1)  #guardamos matriz

#3) Y 4)
#OUTPUT:

#DISPLAY
print("Serie de Fibonacci de %i elementos:"%(n),end="\n")
print(v_fib)
print("Matriz:")
print(a)
#3) Mapa de calor:
plt.figure(1)
plt.clf()
plt.imshow(a)
plt.title("Mapa de calor FIBONACCI")
plt.xlabel("EJE X")
plt.ylabel("EJE Y")
plt.savefig("fibonacci.png")
plt.show()

#GUARDAR EN ARCHIVO LA MATRIZ Y EL Nº DE ELEMENTOS QUE HAY QUE SUMAR PARA SUPERAR LA SUMA DE v_fib

    #numpy
sumavector = numpy.sum(v_fib)
vector = numpy.ravel(a) #como es simetrica da igual eso de empezar a sumar los elementos por columnas..
suma, contador = 0,0
while suma < sumavector:
    suma += vector[contador]
    contador += 1
    
#guardamos archivo:
try:
    file = open("salida.txt","ab")
    """
        Abrimos un file-handle (descriptor de archivo) en modo APPEND binary
        esto lo hacemos para poder appendear, es decir, poder hacer varios
        numpy.savetxt al mismo fichero

    """
    numpy.savetxt(file,[contador],"%d",header="Numero de elementos que hay que sumar:")
    numpy.savetxt(file,a,"%5.3d")        
    file.close()
except IOError:
    print("Hubo un error escribiendo al fichero.")
    

    #sin numpy
    
sumavector_1 = sum(v_fib1)         #funcion de python

#ravel casero
vector_1=[]                        #lo hice vacio pero tambien podria hacer lo de tamaño fijo (len(a)^2)
for i in range(len(a)):         
    for j in range(len(a)):
        vector_1.append(a[i][j])   #como la matriz es simetrica no me fijo en lo de ir por columnas

suma_1 ,contador_1 = 0 , 0         #mismo proceso que antes
while suma_1 < sumavector_1:
    suma_1 += vector_1[contador_1]
    contador_1 += 1
    
#GUARDAMOS EN FICHERO
try:  
    with open("salida_sin_numpy.txt","a") as salida: #abrimos fichero en modo APPEND
        salida.write("Numero de elementos que hay que sumar:\t"+str(contador_1))
        for i in range(len(a)):
            salida.write("\n")
            for j in range(len(a)):
                salida.write(str(a[i][j])+"\t\t") #escribimos los elementos de la matriz uno a uno
    
except:
    print("Hubo un error guardando al fichero.")
    

