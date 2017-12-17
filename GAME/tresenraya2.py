            #TR3S EN RAYA   v.0.1#
#MODULOS
from random import choice
#CONSTANTES Y GLOBALES
global jugador

imag="""   _____            ____  _____  _____ 
  |__  /___  ____  / __ \/   \ \/ /   |
   /_ </ _ \/ __ \/ /_/ / /| |\  / /| |
 ___/ /  __/ / / / _, _/ ___ |/ / ___ |
/____/\___/_/ /_/_/ |_/_/  |_/_/_/  |_|
                                       """
#FUNCIONES
def letraJugador():
    #Preguntamos que letra quiere usar para jugar al 3enraya. Devolvemos lista [letraJug,letraPC].
    letra=""
    while not (letra=="X" or letra=="O"):         #while not (letra== X or letra == O) / not (letra != "X" or letra != "O")
        print("\n\t¿Que prefiere ser O o X en el tablero?:\t",end="")
        letra=input().upper()

    if letra=="X":                              #devolvemos una lista con la decision de piezas, primero usuario, segundo pc.       
        return ["X","O"]
    else:
        return ["O","X"]

def quienEmpieza():
    #Decidimos al azar quien empieza, el 1er turno. Devolvemos string "jugador" o "pc"
    if choice([0,1])==0:
        return "jugador"
    else:
        return "pc"

def mostrarTablero(tablero):
    #Funcion que printea el tablero y su situacion actual con el argumento-lista "tablero".
    print()                                     #tablero es una lista de strings que contienen el estado del mismo. Valores " ","X" o "O". Ignorar primer indice.       
    print("\t\t\t  |   |")
    print("\t\t\t"+tablero[7]+" | "+tablero[8]+" | "+tablero[9])
    print("\t\t\t  |   |")
    print("\t\t\t----------")
    print("\t\t\t  |   |")
    print("\t\t\t"+tablero[4]+" | "+tablero[5]+" | "+tablero[6])
    print("\t\t\t  |   |")
    print("\t\t\t----------")
    print("\t\t\t  |   |")
    print("\t\t\t"+tablero[1]+" | "+tablero[2]+" | "+tablero[3])
    print("\t\t\t  |   |")

def pregMovimiento(tablero):
    #Funcion que pregunta al jugador su siguiente movimiento. Lo retornamos como un 'int' para poder usarlo directamente.
    move=" "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not estaLibre(tablero,int(move)):     #Antes tenia while not(move in ... and estalibre)
        print("\n\t¿Cual será su siguiente movimiento (1-9) ?:\t",end="")
        move=input()

    return int(move)

def estaLibre(tablero,mov):
    #Devolvemos un True si esa posicion del tablero esta vacia. Args: list-tablero, int-mov.    
    return tablero[mov]==" "

def volverJugar():
    #Funcion standar para preguntar si se quiere jugar otra partida. Retornamos True de ser asi.
    print("\n\t¿Quiere volver a jugar otra partida?:\t",end="")
    return (input().lower().startswith("s"))

def hacerMovimiento(tab,move,letra):
    #Funcion que actualiza la list-tablero con el movimiento del jugador indicado. Retorna None (nada).
    tab[move]=letra

def hayGanador(tab,le):
    #Dado la list-tablero y el jugador devuelve True si ha ganado.
    return ((tab[1]==le and tab[2]==le and tab[3]==le)or(tab[4]==le and tab[5]==le and tab[6]==le)or(tab[7]==le and tab[8]==le and tab[9]==le)  #horizontales
            or(tab[1]==le and tab[4]==le and tab[7]==le)or(tab[2]==le and tab[5]==le and tab[8]==le)or(tab[3]==le and tab[6]==le and tab[9]==le)#verticales
            or(tab[1]==le and tab[5]==le and tab[9]==le)or(tab[7]==le and tab[5]==le and tab[3]==le))                                           #diagonales

def copiaTablero(tablero):
    #Funcion que crea una copia del tablero y la devuelve.
    copia=[]
    for i in tablero:
        copia.append(i)
    return copia                                #ERROR DE COJONES AQUI, QUE DIF HAY ENTRE COPIA=TABLERO Y APPENDEAR.

def tableroLleno(tablero):
    #Devolvemos True o False si el tablero esta lleno o no.
    for i in range(1,10):                       #Hago el loop con un range en vez de directamente con "tablero" para evitar el primer indice.
        if (estaLibre(tablero,i)):              #ya que siempre inicio esta lista [" "]*10 y estaLibre fallaria con el primero.
            return False                        #Tambien podria poner un X o un O en la primera posicion ya que se pasa de ella en el resto del prog.
    return True

def movAleatorio(tablero,listamov):
    #Devolvemos al azar un movimiento viable de una lista de ellos entregada. (IA part)
    movePosibles=[]                             #De una lista de movimientos miramos cuales estan libres y escogemos uno aleatoriamente.
                                                #La IA del pc le entregara a la funcion esta lista de posibles movimientos.
    for i in listamov:
        if (estaLibre(tablero,i)):
            movePosibles.append(i)

    if len(movePosibles)!=0:
        return (choice(movePosibles))
    else:
        return None

def movPc(tablero,letrapc):
    #Simple AI que retorna el siguiente movimiento del PC. Esquinas>centro>lados (nºposibilidades de hacer lineas). Probar centro>esquinas>lados.
    if letrapc=="X":
        letrajug="O"
    else:
        letrajug="X"

    #Si el pc puede ganar en el siguiente movimiento, devolvemos ese.
    for i in range(1,10):
        copia=copiaTablero(tablero)
        if estaLibre(copia,i):
            hacerMovimiento(copia,i,letrapc)
            if hayGanador(copia,letrapc):
                return i
    #Si el jugador puede ganar en el siguiente movimiento, delvolvemos ese (bloquear).
    for i in range(1,10):
        copia=copiaTablero(tablero)
        if estaLibre(copia,i):
            hacerMovimiento(copia,i,letrajug)
            if hayGanador(copia,letrajug):
                return i
    #Esquinas
    move=movAleatorio(tablero,[1,3,7,9])
    if move!=None:
        return move
    #Centro
    if estaLibre(tablero,5):
        return 5
    #Lados
    return movAleatorio(tablero,[2,4,6,8])

def intro():
    
    global jugador
    print()
    print (imag)
    print()
    print("\t\t\t***BIENVENIDO AL TRES EN RAYA***")
    print("¿Quien va a jugar hoy?:\t",end="")
    jugador=input()
    print("Muy bien "+jugador+", ¡comenzemos!\n\n\n")
    print()

def main():

    primeravez=True
    while True:                 #Loop juego
                            
        if primeravez:
            intro()
            
        tablero=[" "]*10
        letrajug,letrapc=letraJugador()
        turno=quienEmpieza()
        print("\tEl primer turno sera del "+turno+".")
        jacabado=False

        while not jacabado:
            if turno=="jugador":    #Proceso de turno del jug.
                mostrarTablero(tablero)
                move=pregMovimiento(tablero)
                hacerMovimiento(tablero,move,letrajug)

                if hayGanador(tablero,letrajug):
                    mostrarTablero(tablero)
                    print("\n\tF E L I C I D A D E S ! Ha ganado!")
                    jacabado=True
                else:
                    if tableroLleno(tablero):
                        mostrarTablero(tablero)
                        print("\n\tLa partida ha acabado en empate!")
                        jacabado=True   #break
                    else:
                        turno="pc"
            else:
                move=movPc(tablero,letrapc)
                hacerMovimiento(tablero,move,letrapc)
                
                if hayGanador(tablero,letrapc):
                    mostrarTablero(tablero)
                    print("\n\tHa perdido! El ordenador le ha ganado!")
                    jacabado=True
                else:
                    if tableroLleno(tablero):
                        mostrarTablero(tablero)
                        print("\n\tLa partida ha acabado en empate!")
                        jacabado=True   #break
                    else:
                        turno="jugador"
                
        if not volverJugar():
            break
        else:
            primeravez=False
                    
#Ejecutamos el codigo a través de main() solo como modulo principal.
if __name__== "__main__":
    main()
    