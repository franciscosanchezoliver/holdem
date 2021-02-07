from mensajes import Mensajes 

mensajes = Mensajes()

class Error(Exception):
    """
    Clase base para las excepciones
    """
    pass

class FiguraCartaError(Error):
    """
    Las cartas del poker pueden ser tanto una letra como un numero
    en caso de que sea una letra puede ser solo de 4 tipos: J, Q, K, A
    En caso de que sea un numero debera estar comprendido entre 2 y 10
    """
    mensajes.error("La figura de una carta puede ser una de las siguientes: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A")
    pass

class TipoCartaError(Error):
    """
    Las cartas en el poker solo pueden ser de 4 tipos: 
    - Corazones
    - Diamantes
    - Treboles
    - Picas
    Este error se debe lanzar cuando se intenta crear una carta que no 
    es de uno de estos tipos
    """
    mensajes.error("El tipo de carta puede ser de uno de los siguientes tipos: corazones, diamantes, treboles o picas")
    pass
