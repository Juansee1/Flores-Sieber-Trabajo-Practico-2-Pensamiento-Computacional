import numpy as np
from PIL import Image
from funciones import procesar_canal

def pixelart(ruta_imagen: str, tamaño_bloque: int, niveles_de_color:int, ruta_guardado:str):
    """
    Convierte la imagen original a estilo Pixel Art armando bloques cuadrados de píxeles 
    y reduciendo la cantidad de colores disponibles

    Args:
        ruta_imagen (str): donde está la foto que queremos pixelar
        tamaño_bloque (int): que tan grandes van a ser los píxeles cuadrados nuevos
        niveles_de_color (int): cuantos colores distintos le dejamos usar a la paleta
        ruta_guardado (str): donde guardamos la nueva imagen 
    """
    Imagen = Image.open(ruta_imagen).convert('RGB')
    paleta = np.linspace(0, 255, num = niveles_de_color)
    array_imagen = np.array(Imagen)

    canal_rojo = array_imagen[:, :, 0]
    canal_verde = array_imagen[:, :, 1]
    canal_azul = array_imagen[:, :, 2]
            
    procesar_canal(canal_azul, tamaño_bloque, paleta)
    procesar_canal(canal_rojo, tamaño_bloque, paleta)
    procesar_canal(canal_verde, tamaño_bloque, paleta)

    imagen_reconstruida = np.dstack((canal_rojo, canal_verde, canal_azul))
    imagen_reconstruida = imagen_reconstruida.astype(np.uint8)
    Imagen_procesada = Image.fromarray(imagen_reconstruida)
    

    Imagen_procesada.save(ruta_guardado)
    print(f"Imagen guardada exitosamente en: {ruta_guardado}")
    
    Imagen_procesada.show()