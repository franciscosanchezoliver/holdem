import unittest
from src.main.carta.carta import Carta

class TestBaraja(unittest.TestCase):

    def test_de_baraja(self):
        carta = Carta()
        self.assertEqual(2,2, "deberia ser 3")

if __name__ == '__main__':
    unittest.main()