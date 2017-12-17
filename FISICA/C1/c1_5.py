#!/usr/bin/env python3

#EJERCICIO C1.5
#EJEMPLO 2,4,5,6,8,3,1,7

#Inicializamos las variables(listas) y contadores que necesitaremos.

lPar=[]
lImpar=[]
nPar,nImpar=0,None               #Se puede asignar variables variables en una misma linea con un solo = siempre que esten ordenadas
#Iniciamos los contadores con valores diferentes para que entren en primera instancia en el BUCLE.
print("-INTRODUZCA UNA SERIE DE NUMEROS; SE FINALIZARÁ CUANDO EL NÚMERO DE ELEMENTOS PARES SEA IGUAL AL DE LOS IMPARES.-")
while nPar!=nImpar:
    
    num=input(">")
    if int(num)%2==0:
        lPar.append(num)
    else:
        lImpar.append(num)
    nPar,nImpar=len(lPar),len(lImpar)
    print("\tNºELEMENTOS PARES: %i\tNºELEMENTOS IMPARES: %i"%(nPar,nImpar))
#CUANDO TERMINEMOS, ES DECIR, SE PARE EL BUCLE IMPRIMIMOS LAS LISTAS DE NUMEROS.


print("-PARES INTRODUCIDOS-\t\t\t%s\n-IMPARES INTRODUCIDOS-\t\t\t%s"%(" ".join(lPar)," ".join(lImpar))) #Si imprimimos las listas a pelo saldrían con corchetes y comas.
    
    
    
#QUE LE PODEMOS AÑADIR A ESTE EJERCICIO: PUES OTRA CONDICION, QUE APARTE DE SER EL NºPARES=NºIMPARES QUE LA SUMA DE ESTOS SEA NULA... O IGUAL.