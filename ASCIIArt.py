import numpy as np
from PIL import Image
from funciones import mapeo, normalizar, guardar_ascii_art

def asciiart(ruta_imagen: str, ancho_imagen: int, ruta_guardado:str): 
    """
    Pasa una imagen a texto ASCII: la pasa a blanco y negro, 
    ajusta el tamaño, le asigna los caracteres y guarda el archivo de texto

    ruta_imagen (str): donde está la foto original que queremos transformar
    ancho_imagen (int): cuantas letras de ancho queremos que tenga el dibujo
    ruta_guardado (str): donde guardamos el archivo .txt final
    """
    PALETA = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    Imagen = Image.open(ruta_imagen)

    # escala de grises
    imagen_gris = Imagen.convert('L')
    array_gris = np.array(imagen_gris)

    # normalizar la imagen
    valor_minimo = np.min(array_gris)
    valor_maximo = np.max(array_gris)

    array_normalizado = np.zeros_like(array_gris, dtype=float)

    for y in range(0, array_gris.shape[0], 1):
        for x in range(0, array_gris.shape[1], 1):
            array_normalizado[y, x] = normalizar(array_gris, x, y, valor_minimo, valor_maximo)

    imagen_normalizada = Image.fromarray(np.uint8(array_normalizado))

    # redimensión
    nuevo_ancho = ancho_imagen
    ancho1, alto1 = imagen_normalizada.size
    nuevo_alto = int((alto1 * nuevo_ancho / ancho1) * 0.45)

    imagen_redimensionada = imagen_normalizada.resize((nuevo_ancho, nuevo_alto))
    array_redimensionado = np.array(imagen_redimensionada)


    resultado_final = ""
    for y in range(array_redimensionado.shape[0]):
        for x in range(array_redimensionado.shape[1]):
            indice = mapeo(x, y, array_redimensionado, PALETA)
            resultado_final += PALETA[indice]
        resultado_final += "\n"

    print(resultado_final)
    

    guardar_ascii_art(resultado_final, ruta_guardado)
