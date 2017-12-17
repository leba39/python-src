"""
EJERCICIO C3.3
INTERPRETE:ANACONDA
MODULOS: NUMPY(OPCIONAL),COPY(OPCIONAL)
~~~~~~~~~~~~~~~~~~~~~~~~
"""
from numpy import loadtxt,reshape,sqrt,ceil,append
from copy import deepcopy

#I N P U T: Leer linea del fichero y guardarlo a un vector v.
#Manera corta: numpy
v_1=loadtxt("c3_3.dat","int")
#Manera larga: sin numpy
with open("c3_3.dat","r") as archivo:
    #lo abro en modo lectura y con la expresion with que se encarga de cerrarlo.
    v_2str=archivo.readline() #read()tambien valdria
v_2num=v_2str.strip("\n")
v_2=[int(x) for x in v_2num.split()]
#print(v_1==v_2) TRUE. LISTAS Y ARRAYS==TIPOS DE DATA ANALOGOS



#D E S A R R O L L O: convertir en matriz cuadrada minima rellenando con 5's si necesario.
n=len(v_1)

#Muchas maneras de hacerlo. Elijo dos. Una corta con numpy.reshape() y otra larga sin numpy.
#Con numpy
orden_m1=int(ceil(sqrt(n))) #ceil siempre hace el redondeo hacia "arriba". Lo pasamos a entero ya que devuelve float.

while (n<(orden_m1**2)):#con el while appendeamos al v_1 los 5's que le faltan hasta ser cuadrado perfecto
    v_1=append(v_1,5)#OJO. Este append es propio de numpy ya que los arrays de numpy no admiten el metodo .append() propio de python.
    n+=1             #si no que tienen el suyo propio. Como argumentos se le dan el vector array y el numero a añadir.
                     #y devuelve ese vector con el numero añadido. Importante meterlo en una variable, en la misma
    #si es un proceso recursivo y en una nueva si es una operacion ONE-TIME-ONLY.
m_1=v_1.reshape([orden_m1,orden_m1]) #Reshape coje el vector v_1 y lo ajusta a un array del estilo (x,x)

#Sin numpy
n_2=len(v_2)
if (n_2**(1/2)-round(n_2**(1/2))>0):     #Funcion propia Python round. Si raiz(19)-redondeo(raiz(19)) es positivo entonces sumamos 1.
    orden_m2=round(n_2**(1/2))+1
else:
    orden_m2=round(n_2**(1/2))

"""
Como crear bien las matrices sin NUMPY. Listas de listas! SEAN n,m fil y col:
    m=[[0]*n]*m    ESTA MAL!
Ya que Python crea primero  [0]*n como una unica lista-OBJETO que repite
y concatena despues 'm' veces. Pero como es el mismo "OBJETO" al intentar
modificar un elemento de esta supuesta 'fila' lo estamos haciendo en todas.
Variaciones como.
    m=[[0]*m for i in range(n)] tambien darán el mismo tipo de problema

COMO CREARLAS BIEN PARA HACER ITERACIONES FOR.

    m=[]
    for i in range(n):
        m.append([])
        for j in range(m):
            m[i].append(0)
            
    ó
    
    m=[None]*n           #Indiferente ya que luego se sobreescribiran en el for. (0)
    for i in range(n):
        m[i]=[0]*m
        
Esta ultima manera de crearla es propensa a pensar que fallará por ser casi analoga a la que
poniamos como invalida al principio mas hay que fijarse los OBJETO-columnas que se crean dentro
del bucle FOR son INDEPENDIENTES y por tanto DISTINTOS en cuanto a que no hacen referencia
al mismo "vector".

Este error ya lo teniamos en el c2_5 y lo tenía anotado para mirar en casa. Es un error parecido
al que se comete cuando se intenta crear una copia de una lista en otra variable.
Sea a=[1,2,3,4]
b=a
b[1]=5
no solo cambiará la lista en 'b', si no la original en 'a' ya que las dos hacen REFERENCIA
al mismo OBJETO.
b=list(a)
b=a[:]
b=a*1
Todos harán lo mismo y cometeran este fallo. Esto es por que solo copian en la nueva "lista" las
referencias o direcciones de memoria de los elementos, asi que cuando cambiamos uno de ellos estamos
alterando el contenido en todas las demas. Esto es conocido como SHALLOWCOPY (copiasuperficial) en
contraste al metodo correcto para copiar los valores por separado DEEPCOPY (copiadoprofundo).
    Solucion:
Crear la lista/matriz/vector por separado e asignarle los valores de los elementos de la otra uno a uno.
Importar el modulo copy y la funcion deepcopy de este.
    from copy import deepcopy
    b=deepcopy(a)
Así b y a seran OBJETOS-listas de igual contenido pero referencias DISTINTAS.
"""
m_2=[None]*orden_m2

for i in range(orden_m2):
    m_2[i]=[5]*orden_m2

m_3=deepcopy(m_2)   #tambien podriamos hacer el mismo proceso para m_3: m_3=[None]*...

#Dos maneras validas de proceder: ITERANDO a traves del vector o a traves de la matriz.

        #VECTOR
i,j=0,0        #auxiliares para la posicion
for k in range(n_2):
    m_2[i][j]=v_2[k]
    j+=1
    if (j==orden_m2):
        j=0
        i+=1
        #MATRIZ
k=0
for i in range(orden_m2):
    for j in range(orden_m2):
       if (k<n_2):
           m_3[i][j]=v_2[k]
           k+=1

#O U T P U T: printear la matriz
print("MATRIZ:")
print(m_1)
print("MATRIZ:")
print(m_2)
print("MATRIZ:")
print(m_3)

