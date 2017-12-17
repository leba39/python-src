"""
TESTEAMOS NUESTROS MODULOS DE ENCRIPTACION Y DESENCRIPTACION MEDIANTE LA GENERACION
DE UN MENSAJES ALEATORIO Y LA COMPROBACION DE QUE COINCIDE EL RETORNO ESPERADO CON TODAS LAS CLAVES.
"""

import random,sys
from desencriptaciontransposicion import tDesencriptar
from encriptaciontransposicion import tEncriptar

def main():
    random.seed(42)
    
    for i in range(20):
        msgtest="ABCDEFGHIJKMNLOPQRSTUVWYZ"*random.randint(4,40)
        msgtest=list(msgtest)
        random.shuffle(msgtest)
        msgtest="".join(msgtest)
        
        print("\tTest nº%i:\t%s..."%(i+1,msgtest))
        
        for clave in range(1,len(msgtest)//2):
            cifrado=tEncriptar(msgtest,clave)
            desencifrado=tDesencriptar(cifrado,clave)
            
            if msgtest!=desencifrado:
                print("\tHubo un error con la clave %i y mensaje %s."%(clave,msgtest))
                sys.exit()
            
    print("\n\n\t-TEST SATISFACTORIO-")
    
    
if __name__=="__main__":
    main()
