"""
EJERCICIO: C3.5
INTERPRETE: ANACONDA/DEFAULT (3.6)
MODULOS:
~~~~~~~~~~~~~~~
"""
def vectUsuario(nombre):
    print("Introduzca el vector %s con sus elementos separados por espacios:"%nombre,end="\t")
    vector_str=input(">")
    vector_num=[int(x) for x in vector_str.split()]
    """
    Esta funcion se puede mejorar muchisimo. No tiene control de errores.
    Como le aplicariamos aqui lo de no acepte el numero (vector en este caso)
    a menos que sea un entero?? (isdigit)
    """
    return vector_num



#I N P U T: Leer dos vectores por teclado.

#Como no estamos en Python2 no podemos usar input() en la manera que allí se utiliza para meter
#el vector por teclado directamente, vgr., [1,2,3,4], ya que en Python3 esto sería una cadena de texto
#"[1,2,3,4]" y no un vector. Python2 cuenta con una funcion input() y raw_input() para elegir. Py3 NO!

#Vamos a pedirle al usuario que introduzca el vector de una tirada separado por espacios. Otra manera
#seria pedirle que introdujese primero la longitud del vector y luego cada elemento por separado. ParaGustos..

v=vectUsuario("V")
w=vectUsuario("W")


#D E S A R R O L L O: meter en un vector nuevo los elementos que estan en v y w.
z=[]
for i in range(len(v)):
    if (v[i] in w) and (v[i] not in z):
        z.append(v[i])
#Iteramos por un vector cualquiera, en este caso v. Si el elemento 'i' esta en el vector w y no en el que
#estamos rellenando lo añadimos.
        
#O U T P U T: printearlos
print("Vectores:")
print(v)
print(w)
print("Elementos mutuos:")
print(z)
    
"""
~~~~~~~~~~~~~~~~~~FUNCION MEJORADA SOLUCION~~~~~~~~~~~~~~~~~~
"""


def vectUsuarioMejorado(nombre):
    print("Introduzca el vector %s con sus elementos separados por espacios:"%nombre,end="\t")
    
    vector_lista="Inicio"
    while not (all(x.isdigit() for x in vector_lista)):
        vector_str=input(">")
        vector_lista=vector_str.split()
    
    vector_num=[int(x) for x in vector_lista]
    
    return vector_num


prueba=vectUsuarioMejorado("Prueba")