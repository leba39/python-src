#ENCRIPTACION POR TRANSPOSICION

def main():
    #Llama a la funcion encargada de la encriptacion despues de realizar los input y control de errores (tmb entra clave>len(msg)/2)
    #e imprime en la consola el resultado con un caracter | "pipe" para determinar su correcto final (tema de espacios).
    print("\t -ENCRIPTACION POR TRANSPOSICION-\nEscriba su mensaje:\t",end="")
    mensaje=input()
    clave=""
    while not clave.isdigit() or int(clave)>(len(mensaje)/2):
        print("Introduzca su clave de cifrado (menor que la mitad longitud del mensaje):\t",end="")
        clave=input()
    cifrado=tEncriptar(mensaje,int(clave))
    print("\n\tResultado:\n"+cifrado+"|")
    
def tEncriptar(msg,key):
    #Primero creamos una lista con tantos elementos strings como nos diga la clave dada ya que en este tipo de encriptacion
    #se tienen tantas columnas como nºkey y se apilan los caracteres del mensaje en ellos formando varias filas hasta completarlo.
    encriptado=[""]*key
    #Bucle for para que nos itere a traves de estas columnas y poder asi rellenar cada elemento de la lista encriptado con los caracteres necesarios.
    for col in range(key):
        indice=col    #esta variable nos sirve para determinar que caracteres van en cada elemento (es decir columna) de nuestra "lista".
        
        #Bucle while que se itera tantas veces como nuestro indice(pointer) sea menor que la longitud de caracteres del mensaje.
        while indice<len(msg):
            encriptado[col]+=msg[indice] #rellenamos cada elemento de la lista con el caracter del mensaje correspondiente.
            indice+=key                  #sumamos la clave al indice (representa nºcol) para ir completando.
        
        
    return "".join(encriptado)           #juntamos todos los elementos de la lista ya "mezclados" o encriptados en una string y la retornamos

#VARIABLE NAME DEL ARCHIVO .PY  - ASI PODEMOS IMPORTARLO COMO MODULO SIN EJECUTAR EL MAIN NI EL MENSAJE QUE TENEMOS NOSOTROS -
if __name__=="__main__":
    main()