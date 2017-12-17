#!/usr/bin/env python3

#C2. EJERCICIO 2.
#INTERPRETE DE PYTHON: ANACONDA
#MODULOS USADOS: MATPLOTLIB
import matplotlib.pyplot as plt

def sumatorio(lista,numero,modo):
#FUNCION CREADA EN PARTICULAR PARA EL APARTADO 1.  
    contador=0
    for i in range(len(lista)):
        if modo=="mayores" and lista[i]>numero:
            contador+=1
        elif modo=="menores" and lista[i]<numero:
            contador+=1
    return contador


#INPUT: DESDE ARCHIVO
archivoInput=open("datac2_2.dat","r")            
v=archivoInput.read()                            
archivoInput.close()                    #Ahora ya tenemos en 'v' la cadena de texto que existe en nuestro archivo

#C H I C H A: DESARROLLO

          #Convertir V en un vector de numeros enteros:
listav=v.split()
n=len(listav)

Vint=[]   #APARTADO1
x=[]      #Voy aprovechar el for que necesito para crear el vector V de valores enteros para ir completando el vector X del apartado 1.  2PAJAROS1TIRO
cont=0

for i in range(n):
    Vint.append(int(listav[i]))
    if Vint[i]%2==0:
        cont+=Vint[i]
        if cont<40:
            x.append(Vint[i])
    
m=len(x)  #APARTADO2
y=[]      #Aprovecho la funcion sumatorio del apartado anterior con un pequeño cambio.
for i in range(m):
    y.append(sumatorio(Vint,x[i],"menores"))

print(Vint)
print(x)
print(y)

#OUTPUT: PLOTEAR
barraX=list(range(m))
#configuramos el plot.
plt.plot(barraX,x,"sr-",y,"ob-")
plt.xlabel("Indices")
plt.ylabel("Vectores")
plt.title("Vectores x e y")
plt.grid(True)
#lo guardamos y lo mostramos. importante guardar antes de hacer el show() porque si no matplotlib cierra el objeto-grafica despues de mostrarlo y ya no queda nada para guardar.
plt.savefig("grafica2.png")
plt.show()






"""
      NOTAS:
          
        if (Vint[i]%2)==0 and cont<40:
            cont+=Vint[i]
            x.append(Vint[i])

    Esto en el bucle for aparentemente funcionaria pero nos crearia un vector con un elemento de mas
    ya que actualiza el contador y agrega el elemento al vector al mismo tiempo. Así, cuando entremos
    en el ultimo elemento cuya suma a cont haga que este sea>40 ya estaremos appendeando a x sin necesitarlo.

"""

