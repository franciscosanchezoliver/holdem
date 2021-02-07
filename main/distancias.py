from math import sqrt

def distancia_euclidea(punto1, punto2):
    """
    Calcula la distancia eucluidea entre 2 puntos.
    Ej de uso:
    punto1 = (2,3)
    punto2 = (-3, 5)

    resultado = distancia_euclidea (punto1, punto2)

    """
    x1 = punto1[0]
    y1 = punto1[1]
    x2 = punto2[0]
    y2 = punto2[1]
    distancia = sqrt (pow((x2 - x1) , 2) + pow((y2 - y1) , 2))
    return distancia



#punto_central_jugador_principal = (892, 539)
#punto_central_jugador_izquierda_abajo = (506, 420)
#punto_central_jugador_izquierda_arriba = (705,227)
#punto_central_jugador_arriba = (860,152)
#punto_central_jugador_derecha_arriba = (1153, 218)
#punto_central_jugador_derecha_abajo = (1262, 420)


