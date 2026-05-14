def procesar_canal(canal, tamaño_bloque:float, paleta:str):
        for y in range(0, canal.shape[0], tamaño_bloque):
            for x in range(0, canal.shape[1], tamaño_bloque):
                bloque = canal[y : y+tamaño_bloque, x : x+tamaño_bloque]

                promedio = np.mean(bloque)
                distancia = np.abs(paleta - promedio)
                indice_minimo = np.argmin(distancia)
                color_mas_cercano = paleta[indice_minimo]
                
                bloque[:] = color_mas_cercano
    
def mapeo(x:int, y:int, array_redimensionado, PALETA) -> float:
    pixell = array_redimensionado[y, x]
    i = round((1 - (pixell)/255) * (len(PALETA) - 1))
    return i 

def verificar_ruta():
    pass


