import numpy as np
import os

def procesar_canal(canal: np.ndarray, tamaño_bloque: int, paleta: np.ndarray) -> None:
    """
    Agarra un canal de color, lo divide en bloques y cambia todos los píxeles de ese 
    bloque por el color más parecido de la paleta, modificando la matriz original.
 

    Args:
        canal(np.ndarray): canal de color rojo/azul/verde
        tamaño_bloque(_type_): tamaño del bloque ingresado por el usuario
        paleta(np.ndarray): paleta de colores
    """
    for y in range(0, canal.shape[0], tamaño_bloque):
        for x in range(0, canal.shape[1], tamaño_bloque):
            bloque = canal[y : y+tamaño_bloque, x : x+tamaño_bloque]
                
            promedio = np.mean(bloque)
            distancia = np.abs(paleta - promedio)
            indice_minimo = np.argmin(distancia)
            color_mas_cercano = paleta[indice_minimo]
                
            bloque[:] = color_mas_cercano

def mapeo(x:int, y:int, array_redimensionado: np.ndarray, PALETA:str) -> int:
    """
    Se fija qué tan oscuro es un píxel específico y devuelve qué número de letra 
    de la paleta ASCII le toca usar

    Args:
        x (int): posición en el eje x
        y (int): posición en el eje y
        array_redimensionado (np.ndarray): array con las nuevas dimensiones según lo que pide el usuario y
        en escala de grises
        PALETA (str): paleta de caracteres ASCII

    Returns:
        int: el número de índice para sacar la letra justa de la paleta
    """
    pixell = array_redimensionado[y, x]
    i = round((1 - (pixell)/255) * (len(PALETA) - 1))
    return int(i) 


def verificar_ruta(ruta: str) -> bool:
    """
    Verifica que el archivo que pasaste por consola exista de verdad. 
    Si no lo encuentra, avisa y devuelve False

    Args:
        ruta (str): ruta de la imagen a procesar
        
    Returns:
        bool: nos dice si la ruta existe o no
    """
    try:
        if not os.path.isfile(ruta):
            raise FileNotFoundError
        return True
    except FileNotFoundError:
        print("Error: La ruta o el archivo no existe.")
        return False
    except Exception as e:
        print(f"Error inesperado al verificar ruta: {e}")
        return False

def guardar_ascii_art(ascii_art: str, ruta_salida: str) -> None:
    """
    Guarda en un archivo el texto ASCII

    Args:
        ascii_art (str): dibujo en forma de texto
        ruta_salida (str): donde y con qué nombrese guarda
    """
    with open(ruta_salida, 'w') as f:
        f.write(ascii_art)
    print(f"Archivo ASCII guardado exitosamente en: {ruta_salida}")

def normalizar(array_gris: np.ndarray, x:int, y:int, valor_minimo: float, valor_maximo: float) -> float:
    """
    Normaliza los pixeles utilizando la formula de la consigna

    Args:
        array_gris (np.ndarray): la matríz en escala de gríses
        x (int): _posición en el eje x
        y (int): posición en el eje y
        valor_minimo (float): píxel mas oscuro de la imagen
        valor_maximo (float): píxel mas claro de la imagen

    Returns:
        float: el nuevo valor del píxel
    """
    pixel = array_gris[y, x]
    if valor_maximo == valor_minimo:
         return 0.0
    normalizado = ((pixel - valor_minimo) / (valor_maximo - valor_minimo)) * 255
    return normalizado

def verificar_ancho(ancho_imagen: bool | int) -> int:
    """
    Le pide al usuario el ancho para la imagen ASCII y se asegura de que sea en un formato válido
    Si no pone nada vale 100 por defecto

    Args:
        ancho_imagen (bool | int): variable que usamos de bandera para mantener el bucle 
        hasta que ponga algo válido

    Returns:
        int: valor del ancho valido
    """
    while ancho_imagen == False:
        entrada = input("Ingrese el ancho de la imagen ASCII (default = 100): ").strip()
        if entrada == "":
            ancho_imagen = 100
        else:
            try:
                ancho_imagen = int(entrada)
                if ancho_imagen <= 0:
                    ancho_imagen = False
                    print("El ancho ingresado no es válido, vuelva a intentarlo.")
            except ValueError:
                print("El ancho ingresado no es válido, vuelva a intentarlo.")
    return ancho_imagen