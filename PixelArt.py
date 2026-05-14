import numpy as np
from PIL import Image
from funciones import procesar_canal

def pixelart(ruta_imagen, tamaño_bloque, niveles_de_color, ruta_guardado):
    Imagen = Image.open(ruta_imagen)
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