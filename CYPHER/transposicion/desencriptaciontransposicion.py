from math import ceil

def main():
    #EJEMPLO A MODO DE TEST. LO IMPORTANTE ES LA FUNCION tDesencriptar
    cifrado="Cenoonommstmme oo snnio. s s c"
    clave=8
    
    mensaje=tDesencriptar(cifrado,clave)
    
    print(mensaje+"|")
    
def tDesencriptar(msg,key):
    
    ncol= ceil(len(msg)/key)
    nfil=key
    nsobrantes= (ncol*nfil)-len(msg)
    
    mensaje=[""]*ncol
    
    col=0
    fil=0
    for letra in msg:
        mensaje[col]+=letra
        col+=1
        
        if (col==ncol) or (col==ncol-1 and fil>=(nfil-nsobrantes)):
            col=0
            fil+=1
            
    return ''.join(mensaje)
    
    
    
if __name__=="__main__":
    main()
    