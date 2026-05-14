import numpy as np

def procesar_canal(canal, tamaño_bloque: int, paleta):
        for y in range(0, canal.shape[0], tamaño_bloque):
            for x in range(0, canal.shape[1], tamaño_bloque):
                bloque = canal[y : y+tamaño_bloque, x : x+tamaño_bloque]

                promedio = np.mean(bloque)
                distancia = np.abs(paleta - promedio)
                indice_minimo = np.argmin(distancia)
                color_mas_cercano = paleta[indice_minimo]
                
                bloque[:] = color_mas_cercano
    

def mapeo(x:int, y:int, array_redimensionado, PALETA:str) -> int:
    pixell = array_redimensionado[y, x]
    i = round((1 - (pixell)/255) * (len(PALETA) - 1))
    return int(i) 

def verificar_ruta():
    pass

def guardar_ascii_art(ascii_art: str, ruta_salida: str):
    with open(ruta_salida, 'w') as f:
        f.write(ascii_art)
    print(f"Archivo ASCII guardado exitosamente en: {ruta_salida}")

def normalizar(array_gris, x:int, y:int, valor_minimo, valor_maximo) -> float:
    pixel = array_gris[y, x]
    if valor_maximo == valor_minimo:
         return 0.0
    normalizado = ((pixel - valor_minimo) / (valor_maximo - valor_minimo)) * 255
    return normalizado


def verificar_ancho(ancho_imagen): 
    while ancho_imagen == False:
                ancho_imagen = float(input("Ingrese el ancho de la imagen ASCII (default = 100): "))
                if ancho_imagen <= 0:
                    ancho_imagen = False
                    print("El ancho ingresado no es valido, vuelva a intentarlo")