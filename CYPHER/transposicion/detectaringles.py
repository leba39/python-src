"""
    Modulo DetectarIngles:
Para usar hacer un import a este fichero y usar la funcion esIngles(string)
que devolverá un True o False. Es necesario que junto a este modulo se encuentre
un archivo de txt llamado dictionary que contenga las palabras del diccionario inglés.
(http://invpy.com/dictionary.txt)"""

#CONSTANTES

LETRAS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETRAS_Y_ESPACIOS=LETRAS+LETRAS.lower()+" \t\n"

#FUNCIONES

def cargarDic():
    
    arcDiccionario=open("dictionary.txt")    #Lo abrimos para lectura(por defecto). Podemos mejor control de erroes con un os.path.exists
    palabrasIngles={}                        #Creamos diccionario vacio que iremos llenando de palabras inglesas (una por key) ya que resulta mas eficiente que una lista.
    
    for palabra in arcDiccionario.read().split("\n"):  #Leemos el contenido y le hacemos un split (lista) con nueva linea como separador. El bucle iterará cada palabra.
        palabrasIngles[palabra]=None         #Asignamos un sin-valor a cada value del par de cada key ya que no nos hace falta. Lo hacemos porque su indexado es mas eficiente en la busqueda.
    
    arcDiccionario.close()                   #Cerramos archivo y retornamos el diccionario.
    
    return palabrasIngles

def quitarSimbolos(mensaje):
    
    sololetras=[]                            #Lista vacia que contendra solo las palabras y letras de mensaje.
    
    for caracter in mensaje:                 #Bucle que itera cada char de la string mensaje, si no es una letra no lo appendea.
        if caracter in LETRAS_Y_ESPACIOS:
            sololetras.append(caracter)
    
    return ''.join(sololetras)               #Por ultimo hacemos un join a la lista para convertirla de vuelta a string y la devolvemos.

#DICINGLES=cargarDic() podria ir aqui, antes de la funcion que lo necesita luego y quedaria como constante.
#De todas maneras si lo uso dentro de la propia funcion contarPalabras esta bien igual aunque usemos como modulo y no como main este archivo.
def contarPalabras(mensaje):
    
    mensaje=mensaje.upper()                  #CAPITALIZAMOS LAS PALABRAS DEL MENSAJE PARA COMPARARLAS CON LAS DEL DICCIONARIO.TXT QUE TMB LO ESTAN!!!!
    mensaje=quitarSimbolos(mensaje)          #Nos quedamos solo con las letras y espacios del mensaje y lo spliteamos en una lista de palabras posibles
    
    palabrasposibles=mensaje.split()         #Si la lista esta vacia devolvemos 0.0 para evitarnos el dividir por 0 mas tarde.
    
    if palabrasposibles==[]:
        return 0.0
    
    DICINGLES=cargarDic()
    contador=0
    for palabra in palabrasposibles:         #Iteramos a traves de cada elemento de la lista de palabras posibles y miramos si estan dentro del diccionario cargado.
        if palabra in DICINGLES:
            contador+=1
            
    return contador/len(palabrasposibles)    #Las contamos y devolvemos el tanto por uno con respecto a las palabras que habia en el mensaje dado.

def esIngles(msj,porcentajePalabras=20,porcentajeLetras=85): #Tres argumentos de los cuales dos tendran valores por defecto.
    
    cumplePalabra= (contarPalabras(msj)*100 >= porcentajePalabras)           #Esto evaluará a True o False
    
    numLetras=len(quitarSimbolos(msj))
    pLetras= numLetras/len(msj)*100
    
    cumpleLetras= (pLetras >= porcentajeLetras)                   #Esto evaluara True o False
    
    return (cumplePalabra and cumpleLetras)                  #Se tienen que cumplir las dos

