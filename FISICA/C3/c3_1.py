"""
EJERCICIO C3.1
INTERPRETE: ANACONDA
MODULOS   : NUMPY
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨"""
import numpy
#INPUT
    #SIN NUMPY
    #No importamos modulo OS para comprobar el path. Suponemos como siempre hicimos que el archivo verdaderamente existe.
with open("c3_1.dat","r") as archivo:
    v_str=archivo.readline()         #archivo.read() funcionaria igual en este caso
    #Necesitamos"limpiar" v
v_num=v_str.strip("\n")
v_1=[int(x) for x in v_num.split()] #el split pasa la cadena de texto a lista quitando los espacios entre numeros pero como cadena de texto.
    
    #CON NUMPY
v_2=numpy.loadtxt("c3_1.dat","int")

if all(v_1==v_2):
    print("Comprobacion Input:\t\aOK")
#Verificamos que el formato "ARRAY" que usa numpy es equivalente a trabajar con listas en Python sin numpy.
#Como el tipo de data de los elementos de ambos vectores son "int" todo es TRUE.
    
print("Introduzca un numero entero:") #Procedemos como siempre para leer y verificar el entero introducido por el usuario.
resp=""
while not resp.isdigit():
    resp=input(">")
n=int(resp)
    
#DESARROLLO
contador=0
if n in v_1: #equivalente tambien seria hacer |if not v_1.count(n)==0|TRAD: Si la cuenta de 'n' en la lista v_1 no es 0:   
    for i in range(len(v_1)):             #FOR para ir elemento a elemento del vector.
        if v_1[i]==n:                     #si v[i] coincide con n
            k=i                           #Inicializamos variables/contador auxiliares.
            aux=0                         #k ayuda a determinar los consecutivos y aux a contarlos
            while (v_1[k]==n):            #mientras que v[k] siga siendo 'n'
                aux+=1                    #aumentamos en uno la "cuenta"
                if k<(len(v_1)-1):        #mientras que el indice k no corresponda al ultimo elemento del vector
                    k+=1                  #sumale uno a este indice para ver si el siguiente tmb coincide
                else:                     #si estamos en el indice del ultimo elemento no sumes nada
                    break                 #y salme del loop para evitar error INDEXOUTOFRANGE
                                          #el ejercicio resuelto tenia de esta manera un BUG.
            if aux>contador:              #si esta cuenta de consecutivos es mayor que la maxima
                contador=aux              #registrala en 'contador' que es la que tiene el HIGHSCORE por asi decir.
    
#OUTPUT: Printear
print("Numero máximo consecutivo de %i:\t%i"%(n,contador))