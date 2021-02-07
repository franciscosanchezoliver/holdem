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
    
    def robar_carta(self, carta):
        carta_buscada = self.buscar_carta(carta) 
        if carta_buscada == carta:
            # Eliminamos de la lista de cartas que hay en la baraja
            # ya que la hemos robado
            self.cartas.remove(carta_buscada)
            return carta_buscada
        else:
            return None

    def buscar_carta(self, carta):
        if carta in self.cartas:
            return carta
        else:
            mensajes.error("La carta buscada no esta en la baraja [{},{}]".format(carta.palo, str(carta.figura)))
            return None

    def get_numero_de_cartas(self):
        return len(self.cartas)



if __name__ =="__main__":
    baraja = Baraja()
    baraja.barajar()
    baraja.mostrar_cartas()
