#!/usr/bin/env python3

#EJERCICIO C1.6
#EJEMPLO: 4, 14, 14, 14, 3, -15, 23, 34, 34 #RESULTADO: [1, 100, 100, -1, -1, 1, 1, 100]

#Preparamos las variables. El input es muy parecido al del ejercicio C1_2:

sumatorio=0
serieUsuario=[]
print("Introduzca los numeros de su serie:")

while sumatorio <= 100:
    num=int(input())
    sumatorio+=num
    serieUsuario.append(num)
    
dim=len(serieUsuario)
#CREAMOS OTRA SERIE PARALELA VACIA, CON CEROS O CON UNOS QUE ES LA QUE IREMOS ACTUALIZANDO CON LOS RESULTADOS DADOS POR LAS CONDICIONES DEL EJERCICIO.
#LA UNICA COMPLICACION DE ESTE EJERCICIO RESULTA EN QUE LA DIMENSION DE ESTA NUEVA SERIE TIENE QUE SER dim-1 POR LAS CONDICIONES DADAS EN LOS SUMATORIOS.
serieResultante=[0]*(dim-1)

#BUCLES. Como nos serviran para rellenar con los datos la serieResultante tendremos que iterar dim-1 veces.
for i in range(dim-1):
    if (serieUsuario[i+1]-serieUsuario[i])>0:
        serieResultante[i]=1
    elif (serieUsuario[i+1]-serieUsuario[i])<0:
        serieResultante[i]=-1
    else:
        serieResultante[i]=100
        
#IMPRIMIMOS LOS RESULTADOS.
        
print("NºELEMENTOS LEIDOS:%i\nLISTA DEL USUARIO:%s\nLISTA RESULTANTE:%s"%(dim,serieUsuario,serieResultante))