import unittest
from carta import Carta
from constantes import *
from mano import Mano

class TestMano(unittest.TestCase):

    def test_mano_es_suited(self):
        carta1 = Carta(palo=HEART, figura="Q")
        carta2 = Carta(palo=HEART, figura=5)
        mano = Mano(carta1, carta2)
        self.assertTrue(mano.es_suited()) 

    def test_es_pareja(self):
        carta1 = Carta(palo=HEART, figura="K")
        carta2 = Carta(palo=HEART, figura="K")
        mano = Mano(carta1, carta2)
        self.assertTrue(mano.es_pareja()) 


