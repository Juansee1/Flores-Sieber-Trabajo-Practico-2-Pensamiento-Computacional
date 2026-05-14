import numpy as np
from PIL import Image
from ASCIIArt import asciiart
from PixelArt import pixelart
<<<<<<< HEAD
from funciones import verificar_ancho
=======

>>>>>>> a259072e52c38a4752c0c3c585e89942e57cc5fa

def main():
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    metodo = input("Ingrese el método (pixel/ascii): ").lower().strip()
<<<<<<< HEAD
    ruta_imagen_procesada = input("Ingrese la ruta para guardar el archivo resultante: ")
    
    if metodo == "pixel":
        tamaño_bloque = int(input("Ingrese el tamaño del bloque: "))
        niveles_de_color = int(input("Ingrese la cantidad de niveles de color (default = 4): "))
        pixelart(ruta_imagen, tamaño_bloque, niveles_de_color, ruta_imagen_procesada)
        
    elif metodo == "ascii": 
        ancho_imagen = False
        verificar_ancho(ancho_imagen)  
        asciiart(ruta_imagen, ancho_imagen, ruta_imagen_procesada)
        
    else:
        print("El método elegido no existe, vuelva a intentarlo")
=======
    ruta_imagen_procesada = input("Ingrese la ruta para guardar la imagen procesada: ")
    
    if metodo == "pixel":
        tamaño_bloque = float(input("Ingrese el tamaño del bloque: "))
        niveles_de_color = float(input("Ingrese la cantidad de niveles de color (default = 4): "))
        pixelart(ruta_imagen, tamaño_bloque, niveles_de_color)
        
    elif metodo == "ascii":
        ancho_imagen = float(input("Ingrese el ancho de la imagen ASCII (default = 100)"))
        asciiart(ruta_imagen)
    else:
        print("El método elejido no existe, vuelva a intentarlo")
    
>>>>>>> a259072e52c38a4752c0c3c585e89942e57cc5fa

main()