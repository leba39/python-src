#!/usr/bin/env python3
#IMPORTANTE. PARA DESARROLLOS MAS SIMPLES EMPEZAR A USAR NUMPY: loadtext,find...
#ej:[3,2,7,6,5,9]
#C2. EJERCICIO 4.
#INTERPRETE DE PYTHON: ANACONDA
#MODULOS USADOS: MATPLOTLIB, NUMPY (polinomios)
import matplotlib.pyplot as plt
import numpy

#I N P U T: Leemos teclado usuario.
print("\t-INTRODUZCA SU SERIE DE NUMEROS-")
v=[]
suma=0
while suma<30:
    resp=input(">")
    if resp.isdigit():
        suma+=int(resp)
        v.append(int(resp))
        
    
#D E S A R R O L L O:  -CHICHA-
    #apartado2
y=[]
for i in range(len(v)):
    if v[i]>=5 and v[i]<=10:
        y.append(v[i])
print(y)
    #apartado3
n=len(y)
x=v[:n]                                   #VECTOR X CON LOS 'n' PRIMEROS ELEMENTOS DE V.
poli=numpy.polyfit(x,y,3)                 #FUNCION DE NUMPY. AJUSTE POLINOMICO.

#O U T P U T: GRAFICAR
    #apartado4
barraX=numpy.linspace(min(x),max(x),100)  #FUNCION DE NUMPY. CREA ARRAY DE TANTOS PUNTOS EQUIDISTANTES ENTRE DOS VALORES. 
polievaluado=numpy.polyval(poli,barraX)   #FUNCION DE NUMPY. EVALUA UN POLINOMIO DADO(P) PARA VALORES DADOS(BARRAX)

#configuramos el plot.
plt.plot(x,y,"sb")
plt.plot(barraX,polievaluado,"r-")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Ajuste polinomico.")
plt.grid(True)
#lo guardamos y lo mostramos. importante guardar antes de hacer el show() porque si no matplotlib cierra el objeto-grafica despues de mostrarlo y ya no queda nada para guardar.
plt.savefig("grafica4.png")
plt.show()

