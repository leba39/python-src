#HACKAFFINE. IMPORTA MODULO CRYTPTOMATH, AFFINE Y DETECTARINGLES
import affine, cryptomath, detectaringles

MOSTRAR_PROCESO = True

def main():
    cifrado="ywhui+XctS6hAic<dhdS%S6RShtih&Shu7<<SdhoztS<<o1SzthoBhothuic<dhdSuSoRSh7h c+7zhoztih&S<oSRoz1ht 7thothA7%h c+7z:yhKw<7zhTc6oz1"
    hackmsg=hackAffine(cifrado)
    
    if hackmsg != None:
        print(hackmsg)
        
    else:
        print("\tProceso completado sin exito. No se ha detectado el mensaje original.")
        
    
def hackAffine(msg):
    
    print("\t-Hackeando...-\nPulse Ctrl+C o Ctrl+D para abortar el proceso y salir del programa.")
    
    for clave in range(len(affine.SIMBOLOS)**2):
        claveA=affine.partesClave(clave)[0]
        
        if cryptomath.McD(claveA,len(affine.SIMBOLOS))!=1: #Si son primos entre si no sera posible.
            continue
        
        txtposible=affine.Desencriptar(msg,clave)
        
        if MOSTRAR_PROCESO:
            print("Clave Nº%s:\t%s"%(clave,txtposible[:40]))
            
        if detectaringles.esIngles(txtposible):
            print("\n\tPOSIBLE ENCRIPTACION ENCONTRADA:\nClave Nº%s\nMensaje original:\t%s\n\n\tPulse F para Finalizar o ENTER para seguir probando claves."%(clave,txtposible[:200]))
            resp=input("> ")
            
            if resp.strip().upper().startswith("F"):
                return txtposible
            
    return None
            

if __name__=="__main__":
    main()
        