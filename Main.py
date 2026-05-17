from ASCIIArt import *
from PixelArt import *
from funciones import *

def main():
    ruta_imagen = input("Ingrese la ruta de la imagen: ").strip()
    while not verificar_ruta(ruta_imagen):
        ruta_imagen = input("Ingrese la ruta de la imagen nuevamente: ").strip()

    metodo = input("Ingrese el método (pixel/ascii): ").lower().strip()
    while metodo not in ["pixel", "ascii"]:
        print("El método elegido no existe, vuelva a intentarlo.")
        metodo = input("Ingrese el método (pixel/ascii): ").lower().strip()

    ruta_imagen_procesada = input("Ingrese la ruta para guardar el archivo resultante(recoemendamos la ruta out/nombre_imagnen.png/.txt): ").strip()

    if metodo == "pixel":
        entrada_bloque = input("Ingrese el tamaño del bloque (default=10): ").strip()
        if entrada_bloque == "":
            tamaño_bloque = 10
        else:
            tamaño_bloque = int(entrada_bloque)

        entrada_niveles = input("Ingrese la cantidad de niveles de color (default=4): ").strip()
        if entrada_niveles == "":
            niveles_de_color = 4
        else:
            niveles_de_color = int(entrada_niveles)

        pixelart(ruta_imagen, tamaño_bloque, niveles_de_color, ruta_imagen_procesada)

    elif metodo == "ascii":
        ancho_imagen = False
        ancho_imagen = verificar_ancho(ancho_imagen)
        asciiart(ruta_imagen, ancho_imagen, ruta_imagen_procesada)

main()