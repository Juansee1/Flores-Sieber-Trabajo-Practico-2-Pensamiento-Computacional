import numpy as np
from PIL import Image
from ASCIIArt import asciiart
from PixelArt import pixelart
from funciones import verificar_ancho

def main():
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    metodo = input("Ingrese el método (pixel/ascii): ").lower().strip()
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

main()