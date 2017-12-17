from random import shuffle

def obtNumSecreto(long):
    
    numerales=list(range(10))
    shuffle(numerales)
    numSecreto=""
    for i in range(long):
        numSecreto+=str(numerales[i])
        
    return numSecreto

def obtPista(intento,nsecreto):
    
    if intento==nsecreto:
        return "Ha ganado!"
    
    pistas=[]
    
    for i in range(len(intento)):
        
        if intento[i]==nsecreto[i]:
            pistas.append("Caliente")
        elif intento[i] in nsecreto:
            pistas.append("Templado")
            
    if len(pistas)==0:
        pistas.append("Frio")
        
    pistas.sort()
    
    return ' '.join(pistas)

def volverJugar():
    
    print("\tQuiere volvera jugar? (s-n):\t",end="")
    resp=input()
    
    return resp.lower().startswith("s")

def Main():
    
    MAXINTENTOS=10
    NUMCIFRAS=3
    
    print("Estoy pensando en un numero de %s cifras. Intente adivinarlo en menos de %s intentos." % (NUMCIFRAS,MAXINTENTOS))
    print("\tEstas son las pistas que le ofreceremos:\n\tFRIO\t Ninguna de sus cifras son correctas.\n\tTEMPLADO\tUna cifra es correcta pero mal posicionada.\n\tCALIENTE\tUna cifra es correcta y bien posicionada.")
    
    while True:
        numsecreto=obtNumSecreto(NUMCIFRAS)
        
        nintentos=1
        while nintentos<=MAXINTENTOS:
            intento=""
            while len(intento)!=NUMCIFRAS or not intento.isdigit():
                print("Intento nº%s:" % (nintentos),end="")
                intento=input()
        
            print(obtPista(intento,numsecreto))
            nintentos+=1
            if intento==numsecreto:
                break
            if nintentos>MAXINTENTOS:
                print("Se le acabaron los intentos. El numero secreto era %s" % (numsecreto))
        if not volverJugar():
            break
    
if __name__=="__main__":
    Main()
    
