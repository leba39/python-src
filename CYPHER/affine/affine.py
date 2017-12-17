#CIFRADO AFFINE. COMO EL CESAR PERO MULTIPLICANDO LOS INDICES Y CON UN CESAR SIMPLE DESPUES.

import sys, random, cryptomath

SIMBOLOS="""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    #USO EJEMPLO PARA TESTEARLO. ESTE MODULO ESTARIA LISTO PARA REALIZAR ENCRIPTACION Y DESENCRIPTACION.
    #cambiar mensaje y clave a inputs y hacerle control de errores.
    
    mensaje="ywhui+XctS6hAic<dhdS%S6RShtih&Shu7<<SdhoztS<<o1SzthoBhothuic<dhdSuSoRSh7h c+7zhoztih&S<oSRoz1ht 7thothA7%h c+7z:yhKw<7zhTc6oz1"
    #mensaje=""""A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    clave=7674 
    #clave=generarClavealeatoria() 
    #modo="encript"
    modo="desencript"
    if modo=="encript":
        cifrado=Encriptar(mensaje,clave)
    elif modo=="desencript":
        cifrado=Desencriptar(mensaje,clave)
        
    print("\tClave:\t%i\n\tTexto %sado:\n%s"%(clave,modo.title(),cifrado))
    
def partesClave(key):
    claveA=key//len(SIMBOLOS)
    claveB=key%len(SIMBOLOS)
    
    return (claveA,claveB)

def comprobarClaves(keyA,keyB,mode):
    
    if (keyA==1 or keyB==0) and mode=="encript":
        sys.exit("Este tipo de cifrado se vuelve completamente vulnerable cuando la clave A se traduce a 1 o la clave B a 0. Pruebe otra clave distinta.")
        
    if keyA<0 or keyB<0 or (keyB>len(SIMBOLOS)-1):
        sys.exit("La clave A debe ser mayor que 0 y la clave B debe ser mayor que 0 y menor que %i. Pruebe otra clave distinta."%(len(SIMBOLOS)-1))
        
    if cryptomath.McD(keyA,len(SIMBOLOS))!=1:
        sys.exit("La clave A %i y el tamaño del set de simbolos %i no son primos. Pruebe otra clave distinta.")
        
def Encriptar(msg,key):
    
    kA,kB = partesClave(key)
    comprobarClaves(kA,kB,"encript")
    cifrado=""
    
    
    for caracter in msg:
        if caracter in SIMBOLOS:
            indice=SIMBOLOS.find(caracter)
            cifrado+=SIMBOLOS[(indice*kA+kB)%len(SIMBOLOS)]
        else:
            cifrado+=caracter
            
    return cifrado

def Desencriptar(msg,key):
    
    kA,kB = partesClave(key)
    comprobarClaves(kA,kB,"desencript")
    txtplano=""
    modInvkA=cryptomath.ModInverso(kA,len(SIMBOLOS))
    
    
    for caracter in msg:
        if caracter in SIMBOLOS:
            indice=SIMBOLOS.find(caracter)
            txtplano+=SIMBOLOS[((indice-kB)*modInvkA)%len(SIMBOLOS)]
        else:
            txtplano+=caracter
    return txtplano


def generarClavealeatoria():
    while True:
        kA,kB = random.randint(2,len(SIMBOLOS)),random.randint(2,len(SIMBOLOS))
        if cryptomath.McD(kA,len(SIMBOLOS))==1:
            return kA*len(SIMBOLOS)+kB

if __name__=="__main__":
    main()