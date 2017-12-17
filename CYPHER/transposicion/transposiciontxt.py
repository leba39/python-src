"""
MODULO SENCILLO PARA LA APLICACION A ARCHIVOS DE TEXTO DEL CIFRADO DE TRANSPOSICION.
"""
from os import path
from encriptaciontransposicion import tEncriptar
from desencriptaciontransposicion import tDesencriptar
import sys,time

def main():
    
    print("Bienvenido. Desea encriptar o desencriptar un archivo:",end="\t")
    modo=input()
    archivoInput=input("Introduzca el nombre/directorio del archivo:")
    archivoOutput=input("Introduzca el nombre del archivo de salida:")
    clave=int(input("CLAVE:"))
    
    if not path.exists(archivoInput):
        print("\tEl archivo %s no existe. Saliendo..."%(archivoInput))
        sys.exit()
        
    if path.exists(archivoOutput):
        print("\tSe sobreescribirá el archivo %s. Desea (c)ontinuar o (s)alir?:"%(archivoOutput),end="")
        resp=input("\t> ")
        if not resp.lower().startswith("c"):
            sys.exit()
            
    objArchivo=open(archivoInput)   #Como es para read no hace falta ponerle el segundo argumento ya que es el predeterminado.
    contenido=objArchivo.read()
    objArchivo.close()
    
    
    print("\t-%sNDO..."%(modo.upper()))
    tiempoInicio=time.time()
    
    if modo.endswith("e",0,1):
        modo="encript"    #simplemente para mejorar el display ya que lo llamo despues .title()
        contcifrado=tEncriptar(contenido,clave)
    elif modo.endswith("d",0,1):
        modo="desencript" #para display.
        contcifrado=tDesencriptar(contenido,clave)
    
    tiempoProcesado=round(time.time()-tiempoInicio,2)     #Redondeamos a dos cifras
    print("\t%scion:\t%s (s)"%(modo.title(),tiempoProcesado)) #tiempoprocesado lo formateo como string para que aparezcan los dos decimales. como %f aparecen ceros y con %i no hay decimales.
    
    objArchivoSalida=open(archivoOutput,"w")
    objArchivoSalida.write(contcifrado)
    objArchivoSalida.close()
    
    print("\n\t%sción del archivo %s finalizada. (%s caracteres)\n\tEl archivo %sado es %s ."%(modo.title(),archivoInput,len(contenido),modo,archivoOutput))
    
if __name__=="__main__":
    main()