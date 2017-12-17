from urllib.request import urlopen, Request, URLError

ancho=input("Indique la anchura de la imagen gatuna: ")
alto=input("Indique la altura de la imagen gatuna: ")

peticion=Request("http://placekitten.com/"+ancho+"/"+alto)

try:
    respuesta=urlopen(peticion)
    gato=respuesta.read()
    imagen=open("gato.jpeg","wb")
    imagen.write(gato)
    imagen.close()
except (URLError):
    print("Hubo un error.")
