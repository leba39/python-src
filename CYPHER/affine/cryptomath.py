#MODULO CRYPTOMATH. PARA USO EN CIFRADOS. FUNCIONES McD y ModInverso.

def McD(a,b):
    #ALGORITMO BASICO DE EUCLIDES. ES EL MAS EFICIENTE PARA SACAR EL McD de dos numeros.
    #Realiza una division entera entre ellos, despues el divisor de la 1era pasa como dividendo de la 2era
    #y el resto o residua de la 1era como divisor de la 2a. ESTO SE REPITE HASTA QUE EL RESTO SEA 0.
    #en cuyo caso el McD de esos numeros es el divisor de esta ultima division entera.
    while a != 0:
        a,b = b%a,a
    return b

def ModInverso(a,m):
    #ALGORITMO DE EUCLIDES EXTENDIDO PARA SACAR EL MODULO INVERSO DE DOS NUMEROS a y m.
    #DEVUELVE EL VALOR i. (a*i)%m=1
    
    if McD(a,m)!=1:
        return None    #No hay modulo inverso para estos numeros si no son primos.

    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    
    while v3 != 0:
        q=u3//v3
        
        v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
        
    return (u1 % m)