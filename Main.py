import numpy as np
from PIL import Image
from ASCIIArt import asciiart
from PixelArt import pixelart


def main():
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    metodo = input("Ingrese el método (pixel/ascii): ").lower().strip()
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
    

main()