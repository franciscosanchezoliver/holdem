import unittest
from baraja import Baraja
from carta import Carta
from constantes import * 

class TestBaraja(unittest.TestCase):

    def test_baraja_tiene_52_cartas(self):
        baraja = Baraja()
        numero_de_cartas = baraja.get_numero_de_cartas()
        self.assertEqual(numero_de_cartas, 52, "El numero de cartas en una baraja es de 52 cartas")

    def test_robar_carta(self):
        """
        Creamos una baraja nueva. Buscamos una carta, la robamos y comprobamos
        que esa carta ya no esta en la baraja y que la baraja tiene una carta menos
        """
        # Creamos una baraja nueva
        baraja = Baraja()
        carta = Carta(palo=HEART, figura= "J") 
        carta_robada = baraja.robar_carta(carta)
        self.assertTrue(carta_robada == carta) 
        self.assertTrue(baraja.get_numero_de_cartas() == 51)


