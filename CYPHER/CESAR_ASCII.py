#CIFRADO CESAR SOBRE ASCII V.1

MAX_CLAVE=26

def fModo():

    while True:
        print("\tDesea encriptar, desencriptar o forzar un mensaje?:\t",end="")
        modo=input().lower()
        if (modo in 'encriptar e desencriptar d forzar f'.split()):
            return modo
        else:
            print("\n Introduzca una opcion valida (e, d o f):\t",end="")

def fClave():
    clave=0
    while True:
        print("\tIntroduzca la clave del cifrado (1-%i):\t" % MAX_CLAVE,end="")
        clave=int(input())
        if (clave >= 1 and clave <= MAX_CLAVE):
            return clave
        else:
            print("\n\tClave no valida. Valores numericos entre (1-26):\t",end="")

def fMensaje():
    print("\tIntroduzca a continuación el mensaje que desea des/cifrar:")
    return input()

def fCifrado(m,key,msg):

    if m[0]=="d":
        key=-key
    cifrado=""

    for caracter in msg:
        if caracter.isalpha():
            num=ord(caracter)+key

            if caracter.isupper():
                
                if (num > ord("Z")):
                    num-=26
                elif (num < ord("A")):
                    num+=26
            if caracter.islower():
                
                if (num > ord("z")):
                    num-=26
                elif (num < ord("a")):
                    num+=26

            cifrado+=chr(num)

        else:
            cifrado+=caracter

    return cifrado

if __name__=="__main__":

    modo=fModo()
    if modo[0]=="f":
        mensaje=fMensaje()
        
        modo="d" #Para mandarlo como desencriptacion a la funcion fcifrado
        for llave in range(MAX_CLAVE):
            print("Clave nº%i de %i:\t"%(llave,MAX_CLAVE),end="")
            print(fCifrado(modo,llave,mensaje))
    else:
        llave,mensaje=fClave(),fMensaje()
        print("\n\tSu texto procesado resulta en:")
        print(fCifrado(modo,llave,mensaje))

    
            
            