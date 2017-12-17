"""
Cambios en la nueva versión:
    +Añadido diccionario con diferentes sets de palabras.
    +Añadido como pista el set correspondiente.
    +Mejorada la funcion nuevapalabra con choice.
"""
                    #AHORCADO v.0.2

#Importamos modulos necesarios. Aleatorio y sleep (para animaciones).
from random import choice
from time import sleep

#GLOBALES
jugador=""

#CONSTANTES
IMAGENES=["""
             +---+
             |   |
                 |
                 |
                 |
                 |
                 |
            =========""","""
             +---+
             |   |
             O   |
                 |
                 |
                 |
                 |
            =========""","""
             +---+
             |   |
             O   |
             |   |
                 |
                 |
                 |
            =========""","""
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
                 |
            =========""","""
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
                 |
            =========""","""
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
                 |
            =========""","""
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
                 |
            ========="""]

INTRO=""" _______           _______  _______  _______  _______  ______   _______ 
(  ___  )|\     /|(  ___  )(  ____ )(  ____ \(  ___  )(  __  \ (  ___  )
| (   ) || )   ( || (   ) || (    )|| (    \/| (   ) || (  \  )| (   ) |
| (___) || (___) || |   | || (____)|| |      | (___) || |   ) || |   | |
|  ___  ||  ___  || |   | ||     __)| |      |  ___  || |   | || |   | |
| (   ) || (   ) || |   | || (\ (   | |      | (   ) || |   ) || |   | |
| )   ( || )   ( || (___) || ) \ \__| (____/\| )   ( || (__/  )| (___) |
|/     \||/     \|(_______)|/   \__/(_______/|/     \|(______/ (_______)
                                                                        """
                                                     
                                                                                                                          
PALABRAS={"Animales":"lagarto hormiga raton perro gato oveja elefante tigre leon jabali ciervo conejo ardilla serpiente oso mariposa aguila halcon paloma gaviota".split(),
          "Deportes":"futbol baloncesto tenis esqui golf atletismo rugby voleybol boxeo padel rally karate taekwondo judo triathlon".split(),
          "Trabajos":"camarero reportero presentador escayolista obrero carpintero piloto profesor carnicero panadero mecanico dependiente minero".split(),
          "Objetos":"impresora pantalla teclado cartera llaves coche casa tirachinas reloj crema lapiz taza botella tabla piedra calculadora silla cama libro peluche".split()}

#FUNCIONES
#Escoge una palabra al azar del diccionario dado.
def nuevapalabra(dicc):

    dicset=choice(list(dicc.keys()))
    npalabra=choice(dicc[dicset])
    #Devolvemos ahora en esta funcion una lista con la palabra escogida y el set al que corresponde.
    return [npalabra,dicset]

#Input del usuario, verificamos que es una letra y que no la haya intentado antes (argumento).
def escogerletra(letrasintentadas):

    #Loop.
    while True:
        print("\tIntroduzca una letra:",end="")
        letra=input()

        #Verificacion
        if len(letra)!=1:
            print("\t*Solo una letra.")
        elif letra in letrasintentadas:
            print("\t*Ya introdujo esa letra anteriormente.")
        elif letra not in "abcdefghijkmnlopqrstuvwyz":
            print("\t*Solo caracteres alfabeticos.")
        else:
            return letra

#Retornamos un True si se quiere volver a jugar.
def volverjugar():
    
    print("\t¿Quiere volver a jugar? (Si/No)")
    respuesta=input()
    return respuesta.lower().startswith("s")

#Intro del juego. Animaciones con sleep.
def intro():

    #Declaramos la global para modificarla.
    global jugador
    print (INTRO)
    print()
    sleep(2)
    print("\t\t ***Bienvenido al juego del ahorcado***")
    sleep(1)
    print("¿Quien va a jugar hoy?:\t",end="")
    jugador=input()
    sleep(1)
    print("Muy bien "+jugador+", ¡comenzemos!\n\n\n")
    sleep(1)

    #Genero una lista con las palabras que conformaran la animacion.
    animacion="GENERANDO PALABRA ALEATORIA".split()

    #Itero sobre ellas y sobre cada una de sus letras en un segundo "for".
    for i in range(len(animacion)):
        #Nuevas lineas entre palabra y palabra
        print()
        for letra in animacion[i]:
            #Printamos las letras una tras otra con un cierto retraso
            print (letra,end="")
            print("...",end="")
            sleep(.5)
    #Hacemos un clear del shell para prepararlo para el juego.
    print("\n"*20)
        
#Funcion que nos representa el tablero de juego. Printa el estado del ahorcado, letras falladas, la palabra secreta(oculta).
def estadotablero(IMAG,palabrasecreta,letrasfalladas,letrasacertadas):

    #Print del ahorcado segun los fallos que llevemos.
    print()
    print(IMAG[len(letrasfalladas)])
    sleep(1)
    print()

    #Printamos las letras falladas una tras otra en linea. 
    print("\tLetras falladas:",end="")
    for letra in letrasfalladas:
        print (letra,end="")
    print()

    #Printamos la palabra secreta ocultando las letras que no hayan sido acertadas. Var "blancos".
    blancos="_"*len(palabrasecreta)
    sleep(1)
    print("\tPalabra Secreta:\t",end="")

    #Iteracion a traves de las letras de la palabra secreta. Si alguna letra esta en las acertadas la hacemos visible.
    for letra in range(len(palabrasecreta)):
        if palabrasecreta[letra] in letrasacertadas:
            blancos= blancos[:letra]+palabrasecreta[letra]+blancos[letra+1:]
    #Printamos "blancos" letra a letra en linea.
    for letra in blancos:
        print(letra,end="")
    print()
            

#MAIN

#Damos salida a la intro e inicializamos variables vacias de juego.    
intro()
lfalladas=""
lacertadas=""
psecreta,pista=nuevapalabra(PALABRAS)
jacabado=False

#Loop de juego. Ciclo de operacion. Flow chart. Solo se fuerza la salida al final con un break en caso de juego finalizado y no querer jugar mas.
while True:

    #Actualizamos tablero y preguntamos por nueva letra.
    print("\n\n\n\n\n\tPista:\t"+pista)
    estadotablero(IMAGENES,psecreta,lfalladas,lacertadas)
    nletra=escogerletra(lfalladas+lacertadas)

    #Chequeamos si la nueva letra esta en la palabra oculta. Si lo esta verificamos si ya lo estan todas en cuyo caso se gana (jacabado).
    if nletra in psecreta:
        lacertadas+=nletra
        todoacierto=True
        for i in range(len(psecreta)):
            if psecreta[i] not in lacertadas:
                todoacierto=False
                break
        if todoacierto:
            print("\n\t¡Has ganado "+jugador+"!\t La palabra secreta era en efecto ",end="")
            sleep(1)
            print(psecreta)
            jacabado=True

    #Si no lo esta contabalizamos el fallo. Si ya fallamos todos los intentos preparamos la salida, printamos resultado y (jacabado).    
    else:
        lfalladas+=nletra

        if len(lfalladas)==len(IMAGENES)-1:
            estadotablero(IMAGENES,psecreta,lfalladas,lacertadas)
            print("\n\t¡Has perdido "+jugador+"!\nDespues de "+str(len(lfalladas))+" errores y con "+ str(len(lacertadas))+" aciertos la palabra buscada era...",end="")
            sleep(1)
            print(psecreta)
            jacabado=True

    #Por ultimo el recurso que nos saca del loop. Con "jacabado" verdadero preguntamos si se quiere volver a jugar. 
    if jacabado:
        
        #Si la respuesta es verdadera volvemos a inicializar las variables y escogemos una nueva palabra.
        if volverjugar():
            jacabado=False
            lfalladas=""
            lacertadas=""
            psecreta=nuevapalabra(PALABRAS)
        #De otra manera forzamos la salida del loop con este break y terminamos la ejecucion.
        else:
            break
    
