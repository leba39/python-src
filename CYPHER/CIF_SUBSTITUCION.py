#CIFRADO DE SUBSTITUCION SIMPLE. SOLO ENCRIPTACION. SIN CONTROL DE ERRORES. V1.
#MODULOS Y CONSTANTES
import sys,random

SET_LETRAS=""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():

    modo="encript"
    mensaje=input("Escriba el mensaje que desea cifrar:\n")

    clave=obtKey()
    comprobarKey(clave)
    if modo[0]=='e':
        traducido=Encriptar(mensaje,clave)
    elif modo=='d':
        traducido=Desencriptar(mensaje,clave)
        
    print("\t-CLAVE-:\t\t\t%s\n\t-MENSAJE %sADO-:\n%s"%(clave,modo.upper(),traducido))
    
def obtKey():
    lkey=list(SET_LETRAS)
    random.shuffle(lkey)
    
    return ''.join(lkey)

def comprobarKey(key):
    
    lkey=list(key)
    lset=list(SET_LETRAS)
    
    lkey.sort()
    lset.sort()
    
    if lkey!=lset:
        sys.exit("HUBO UN PROBLEMA CON LA CLAVE O CON EL SET DE CIFRADO. NO COINCIDEN.")
        
def Encriptar(msg,key):
    return traducir(msg,key,"encript")
def Desencriptar(msg,key): #para futuro uso por otros modulos
    return traducir(msg,key,"desencript")

def traducir(msg,key,modo):
    
    traducido=""
    charsA=SET_LETRAS
    charsB=key
    
    if modo=="desencript":
        charsA,charsB=charsB,charsA
    
    for caracter in msg:
        indicecaracter=charsA.find(caracter)
        traducido+=charsB[indicecaracter]
    
    return traducido
    
if __name__=="__main__":
    main()