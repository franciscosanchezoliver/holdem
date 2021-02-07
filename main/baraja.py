from constantes import PALOS, FIGURAS
from carta import Carta
import random
from mensajes import Mensajes

mensajes = Mensajes()

class Baraja:

    def __init__(self):
        # Inicializamos una baraja sin cartas
        self.cartas = []
        self.crear_cartas_baraja()
    
    def crear_cartas_baraja(self):
        """
        La baraja en el poker tiene 52 cartas. 
        13 cartas por cada palo
        """
        for palo in PALOS:
            for cada_figura in FIGURAS:
                carta = Carta(palo=palo, figura=cada_figura) 
                self.cartas.append(carta) 
        
    def mostrar_cartas(self):
        for carta in self.cartas:
            carta.mostrar_carta()

    def barajar(self):
        random.shuffle(self.cartas)

    def ordenar_cartas(self):
        self.cartas.sort()
    
    def buscar_carta(self, carta):
        for cada_carta in self.cartas:
            if (carta.palo == cada_carta.palo and carta.figura == cada_carta.figura):
                return cada_carta
        else:
            mensajes.error("La carta buscada no esta en la baraja [{},{}]".format(carta.palo, str(carta.figura)))
            return None

    def eliminar_carta_de_baraja(self, carta):
        carta_eliminada = None
        for indice, cada_carta in enumerate(self.cartas):
            if (cada_carta.palo == carta.palo and cada_carta.figura == carta.figura):
                carta_eliminada = self.cartas.pop(indice)
        return carta_eliminada

    def get_numero_de_cartas(self):
        return len(self.cartas)



if __name__ =="__main__":
    baraja = Baraja()
    baraja.barajar()
    baraja.mostrar_cartas()
