                                                #Adivina el numero -PATATA CALIENTE- v.0.2#

#Importamos modulos necesarios.
from random import randint

#GLOBALES
jugador=""

#FUNCIONES
#Printamos un intro
def intro():
    print("\t\tP\tA\tT\tA\tT\tA \n \tC\tA\tL\tI\tE\tN\tT\tE")
    print("\n\n")
    print("***GRAND PRIX EDITION***")
    print()

#Bienvenida y configuracion del juego.Nombre,intervalos,intentos...    
def inicio():
    
    global jugador
    conf=[]
    #Jugador
    print ("\t\t\t------PATATA CALIENTE------ \n Bienvenido. ¿Quien va a jugar?")
    jugador= input()
    #Intervalos
    print ("Muy bien, " + jugador + ". Indique un intervalo sobre el que escogere un entero al azar.\n Minimo:")
    intmin=int(input())

    print ("Maximo:")
    intmax=int(input())

    #Chequeamos los intervalos dados.
    if intmax<intmin:
        print("\t*Su maximo es menor que su minimo. Le daremos la vuelta al intervalo para proceder.")
        nube=intmin
        intmin=intmax
        intmax=nube
    #Intentos
    print("¿Cuantos intentos se quiere dar? \n\t *Nota: El numero maximo de intentos permitidos será igual a la mitad de la longitud del intervalo")
    intentos=int(input())
    #Chequeamos los intentos dados segun norma y regla.
    while (intentos<1) or (intentos>round((intmax-intmin)/2)):
        print("Numero de intentos invalido.\n\tVuelva a intentarlo:")
        intentos=int(input())
    #Preparamos la lista de config que retornamos.
    conf.append(jugador)
    conf.append(intmin)
    conf.append(intmax)
    conf.append(intentos)
        
    return conf
    
#Dinamica del juego segun la config dada. Intentos y aciertos.    
def jugar(config):

    #Inicializamos variables segun conf y preparamos var de salida (win, devuelta...)
    intentos=0
    aleatorio=randint(config[1],config[2])
    win=False
    devuelta=[]
    
    #Loop.
    while intentos < config[3]:
        print ("Intento numero "+str(intentos+1)+" :")
        guess= int(input())
        #Chequeamos el intento y ajustamos.
        if guess>aleatorio:
            print ("Se ha pasado. MENOS!")
        if guess<aleatorio:
            print("Se ha quedado corto. MAS!")
        if guess==aleatorio:
            #En caso de acertar salimos forzosamente del loop con la var win verdadera.
            win=True
            break
        intentos+=1

    #Preparamos la lista con las variables de retorno.    
    devuelta.append(win)
    devuelta.append(intentos)
    devuelta.append(aleatorio)
    return devuelta

#Dados los datos de la partida jugada nos presenta el resultado final.
def final(resultado):
    global jugador

    #Si la primera variable (Win) es verdadera..
    if resultado[0]:
        print("Enhorabuena %s, ha ganado en %i intentos"%(jugador, resultado[1]+1))
    else:
        print("Lo sentimos %s, ha perdido. El numero que estaba pensando era %i."%(jugador, resultado[2]))

#Funcion del ciclo de operacion. Segun Flow Chart. PRESCINDIBLE 
def main():

    #Se puede modificar este loop while con una var Bool que juegue con la string del input (.lower().startswith("s")). 
    volverjugar = "si"
    while volverjugar == 'si' or volverjugar == 's':
        
        intro()
        final(jugar(inicio()))

        print("¿Quiere volver a jugar?:\t(si o no)")
        volverjugar = input()

#Aqui empieza la ejecucion del programa con main() encargandose de todo. 
if __name__ == "__main__":
    main()
        

    