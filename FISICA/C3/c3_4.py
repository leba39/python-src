"""
EJERCICIO: C3.4
INTERPRETE: ANACONDA/DEFAULT 3.6 (NO HACE FALTA LA DEPENDENCIA MATPLOTLIB DE ANACONDA PORQUE NO PLOTEAMOS)
MODULOS: NUMPY(OPCIONAL PERO MUY RECOMENDADO AL ESTAR ESTE EJERCICIO CARGADO DE OPERACIONES DE RECOMPOSICION)
~~~~~~~~~~~~~~~~
"""
from numpy import loadtxt,shape,copy
#from copy import deepcopy

#I N P U T: Leer matriz desde archivo.

matriz=loadtxt("c3_4.dat","int")
n,m=matriz.shape  #no hace falta parentesis ya que este atributo/metodo de numpy devuelve formato TUPLA.

#D E S A R R O L L O:
#1) Extraer de la matriz la cuadrada mas grande posible.

if (n<m):
    b=matriz[:n,:n].copy() #FIJARSE QUE EL ACCESO A MATRICES/ARRAYS POR NUMPY SE PUEDE HACER ,PEJ.,[1,2]
elif (n>m):
    b=matriz[:m,:m].copy() #TAMBIEN PODRIAMOS USAR LA FUNCION DEEPCOPY DEL MODULO COPY.
                           #b=copy.deepcopy(matriz[:n,:n])...
else:
    b=matriz.copy()
        
#2) Crear vector V de la misma longitud que el orden de B segun el sumatorio dado en el PDF.

n=len(b)
v=[] #Tambien podriamos inicializar el vector con 0's o 1's o lo que sea ya que sabemos el tamaño.
for i in range(n):
    v.append(b[i,i]+b[i,n-i-1]) #El sumatorio es "+", ej. resuelto lo pone con "-"??

#O U T P U T: Printear
print("Matriz de entrada leida correctamente:")
print(matriz)
print("Mayor matriz cuadrada:")
print(b)
print("Vector 'v':",end="\t")
print(v)

"""
~~~~~~~~ASPECTOS CLAVES DEL EJERCICIO~~~~~~~~~~~~~
Funcion shape de numpy se tiene que llamar sin parentesis y asignarle el resultado que devuelve
a dos variables, es decir a una DUPLA de variables (n,m);(x,y) lo que se quiera.
El acceso a elementos de matrices/array si son dadas por NUMPY (que tiene un tipo de data especial)
se puede hacer en un mismo corchete. EJEMPLO

    m: ARRAY([...],[...],..) NUMPY -> m[0,0]=1er elemento m[2,1]=Elemento 3x2
    
Cuando creamos pseudo-matrices con LISTAS DE LISTAS a traves de python sin NUMPY esto no se puede hacer.

    q: matriz lista de listas python -> q[0][0]=1er elemento q[2][1]=elemento 3x2
"""
