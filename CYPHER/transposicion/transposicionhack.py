#TRANSPOSICION HACK

from detectaringles import esIngles
from desencriptaciontransposicion import tDesencriptar

def main():
    
    #EJEMPLO
    mensaje="""Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
    hackmensaje=hackT(mensaje)
    
    if hackmensaje==None:
        print("\tSe ha fallado el ataque por fuerza bruta. No se ha detectado un mensaje coherente.")
    else:
        print("\tMensaje descifrado:\n%s"%(hackmensaje))
    
    

def hackT(msg):
    print("\t-COMENZANDO ATAQUE POR FUERZA BRUTA-")
    print("Puede salir en cualquier momento del proceso presionando Ctrl-C o Ctrl-D.\n.............")
    
    for clave in range(1,len(msg)):
        print("Intentado clave #%i..."%(clave))
        descifrado=tDesencriptar(msg,clave)
        
        if esIngles(descifrado):
            print("\n\tPosible encriptacion hallada:")
            print("Clave #%i:\t%s..."%(clave,descifrado[:100]))
            print("\nIntroduzca F para finalizar o \'Enter\' para seguir probando claves:\t",end="")
            
            resp=input(">")
            
            if resp.strip().upper().startswith("F"):
                return descifrado
    return None
    
if __name__=="__main__":
    main()    