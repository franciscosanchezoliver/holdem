import unittest
from baraja import Baraja
from carta import Carta
from constantes import * 

class TestBaraja(unittest.TestCase):

    def test_baraja_tiene_52_cartas(self):
        baraja = Baraja()
        numero_de_cartas = baraja.get_numero_de_cartas()
        self.assertEqual(numero_de_cartas, 52, "El numero de cartas en una baraja es de 52 cartas")

    def test_eliminar_carta(self):
        """
        Creamos una baraja nueva. Buscamos una carta, la robamos y comprobamos
        que esa carta ya no esta en la baraja y que la baraja tiene una carta menos
        """
        # Creamos una baraja nueva
        baraja = Baraja()
        carta = Carta(palo=HEART, figura= "J") 
        carta_robada = baraja.eliminar_carta_de_baraja(carta)
        self.assertTrue(carta_robada.palo == HEART, carta_robada.figura == "J") 
        self.assertTrue(baraja.get_numero_de_cartas() == 51)

    def test_buscar_carta(self):
        """
        Buscamos una carta en la baraja
        """
        # Creamos una baraja nueva
        baraja = Baraja()
        carta = Carta(palo=HEART, figura= 3) 
        carta_buscada = baraja.buscar_carta(carta)
        self.assertTrue(carta_buscada.palo == HEART, carta_buscada.figura == 3) 
        self.assertTrue(baraja.get_numero_de_cartas() == 52)

