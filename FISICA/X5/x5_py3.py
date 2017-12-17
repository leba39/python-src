"""
EXAMEN 5 - JULIO 2016
INTERPRETE: ANACONDA (NECESITAMOS PLOTEAR)
MODULOS: MATPLOTLIB, NUMPY (OPCIONAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#MODULOS
import numpy
import matplotlib.pyplot as plt
#FUNCIONES
def calcula(matriz): #Devolver un vector que sea la diagonal de la matriz y otro que sea la suma de cada columna
    #NUMPY
    v_diag = numpy.diag(matriz)
    v_col  = numpy.sum(matriz,axis=0) #0 para col, 1 para fil. No confundir con SUM de Python!
    #SIN NUMPY
    n=len(matriz)
    v_diag1 = []       #Puedo crearlas vacias y appendear o como ya se el tamaño a priori definirlas.
    v_col1  = [0]*n
    for i in range(n):
        for j in range(n):
            if (i==j):
                v_diag1.append(matriz[i][j])
                
    i,j=0,0
    for k in range(n):
        i=0             #1era fila
        suma=0          #reseteo suma
        while (i<n):
            suma+=matriz[i][j]
            i+=1
        v_col1[k]=suma
        j+=1            #avanzo columna
        
    return [v_diag,v_col1]     #Indiferente. Devolvemos una lista con dos vectores. 

#MAIN
    
#I N P U T: Leer entero por teclado
    #Input con control de errores basico.
print("Introduzca un numero entero:")
resp="INICIOBUCLE"
while not resp.isdigit():
    resp=input(">")
n=int(resp)

#D E S A R R O L L O:
#1) Crear matriz cuadrada de orden 'n' y definirla segun la regla.

    #NUMPY
matriz=numpy.zeros([n,n])
    #SIN NUMPY
matriz_1=[None]*n
for i in range(n):
    matriz_1[i]=[0]*n    #la creamos correctamente
    
    #DEFINICION

for i in range(n):
    for j in range(n):
        contador=0;suma=0          #auxiliares
        limite=(i+1)**3*(j+1)**2   #para cada elemento calculamos su 'limite' y procesamos el bucle
        while (suma<limite):
            contador+=1
            suma+=contador
        matriz[i,j]=contador
        matriz_1[i][j]=contador

#2)Crear la funcion calcula y llamarla.
[diagonal,sumcol]=calcula(matriz)  #puedo hacer resultado=calcula(matriz) y luego diagonal=resultado[0] etc

#3)Crear vectoe de 50 elementos entre min y max de diagonal e interpola diagonal y sumcol entre estos.

barra_x = numpy.linspace(min(diagonal),max(diagonal),50)  #limites y nº argumentos
interpol   = numpy.interp(barra_x,diagonal,sumcol)        #barrax y vectores a interpolar

#O U T P U T: Plotear y guardar en fichero.

    #unos prints para que quede bonito
print("Matriz generada de orden %i:"%n)
print(matriz)
print("Vector diagonal:",end="\t")
print(diagonal)
print("Vector suma columnas:",end="\t")
print(sumcol)

#3)Grafica

plt.figure(1)
plt.clf()
plt.plot(diagonal,sumcol,"bs")
plt.plot(barra_x,interpol,"g*")
plt.xlabel("Valores")
plt.ylabel("Data")
plt.grid(True)
plt.title("Interpolacion")
plt.savefig("grafica.png")
plt.show()


#4)Si el numero de pares de la matriz es mayor que el numero de elementos mayores que el orden de ella. guardar.
#  si no hacer mapa de calor.

#NUMPY

npares = numpy.sum(matriz%2==0)     #DEVUELVE LA SUMA DE LOS ELEMENTOS QUE CUMPLEN LA CONDICION LOGICA!!
norden = numpy.sum(matriz>n)

#SIN NUMPY
npares_1,norden_1=0,0

for i in range(n):
    for j in range(n):
        if (matriz_1[i][j]%2==0):
            npares_1+=1
        if (matriz[i][j]>n):
            norden_1+=1

#GUARDAR EN ARCHIVO / MAPA DE CALOR.
            
if (npares>norden): #guardar en archivo
    
    print("Con que nombre quiere guardar la matriz?:")
    resp=input(">")
    try:
        numpy.savetxt(resp,matriz,"%5d")
    except IOError:
        print("Hubo un error escribiendo al fichero.")
    
    """
    SIN NUMPY

    try:
        with open(resp,"w") as salida:
            salida.write(str(matriz_1))
    except:
        print("Hubo un error escribiendo al fichero.")
    """
    
else:               #graficar
    plt.figure(2)
    plt.clf()
    plt.imshow(matriz)
    plt.title("Mapa de calor")
    plt.savefig("mapacalor.png")
    plt.show()
    
    






