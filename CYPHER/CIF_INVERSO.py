def Menu():
    print("\n\n\t1: Encriptar/Desencriptar mensaje.\n\t2: Salir.")

    while True:
        respuesta=input()
        if not respuesta.isdigit():
            print("Solo valores numericos.")
        else:
            resp=int(respuesta)
            if resp!=1 and resp!=2:
                print("Escoja una de las dos opciones.")
            else:
                return resp
    

def Cifrado(msg):
    cifrado = ''
    i = len(msg) - 1
    while i >= 0:
        cifrado = cifrado + msg[i]
        i = i - 1
    return cifrado

def Main():
    print("CIFRADO INVERSO\n")
    while True:
        opcion=Menu()
        if opcion==1:
            print("\t Escriba su mensaje:")
            mensaje=input()
            print("\t Resultado:")
            print(Cifrado(mensaje))
        else:
            break

if __name__=="__main__":
    Main()

