import unittest
from src.main.carta.carta import Carta 
from src.main.constantes import constantes

class TestCarta(unittest.TestCase):

    def test_numero_es_valido(self):
        """
        Las carta del poker pueden tener un numero comprendido entre
        el 2 y el 10
        """
        una_carta = Carta(palo=constantes.palos.SPADE, numero=2)

        self.assertEqual(2,3, "deberia ser 3")

if __name__ == '__main__':
    unittest.main()