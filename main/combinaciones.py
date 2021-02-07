from mano import Mano
from mesa import Mesa
from constantes import *

class Combinaciones():

    def __init__(self, cartas):
        self.cartas = cartas

    def calcular_combinacion(self):
        """
        Calcula la mejor combinacion que hay en las cartas
        """
        carta_alta = es_carta_alta()
        pareja = es_pareja()
        doble_pareja = es_doble_pareja()
        trio = es_trio()
        escalera = es_escalera()
        color = es_color()
        full = es_full()
        poker = es_poker()
        escalera_color = es_escalera_color()
        escalera_real = escalera_real()

        if escalera_real:
            return ROYAL_FLUSH
        elif escalera_color:
            return STRAIGHT_FLUSH
        elif poker:
            return POKER
        elif full:
            return FULL_HOUSE
        elif color:
            return FLUSH
        elif escalera:
            return STRAIGHT
        elif trio:
            return SET
        elif doble_pareja:
            return TWO_PAIRS
        elif pareja:
            return PAIR
        elif carta_alta:
            return HIGH_CARD
        else:
            return None 



    def es_carta_alta(self):
        pass

    def es_pareja():
        pass

    def es_doble_pareja():
        pass

    def es_trio():
        pass

    def es_escalera():
        pass
    
    def es_color():
        pass

    def es_full():
        pass

    def es_poker():
        pass
    
    def es_escalera_color():
        pass
 
    def escalera_real():
        pass

