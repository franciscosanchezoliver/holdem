import unittest
from carta import Carta 
from excepciones import FiguraCartaError, TipoCartaError
from constantes import * 


class TestCarta(unittest.TestCase):

    def test_numero_es_valido(self):
        """
        Las carta del poker pueden tener un numero comprendido entre
        el 2 y el 10
        """
        carta = Carta(palo=HEART, figura=3)
        self.assertTrue(carta.palo, HEART)

    def test_numero_no_es_valido(self):
        """
        Las carta del poker pueden tener un numero comprendido entre
        el 2 y el 10
        """
        ocurre_excepcion = False
        try:
            carta = Carta(palo=HEART, figura=1)
        except FiguraCartaError as ex:
            ocurre_excepcion = True
        self.assertTrue(ocurre_excepcion)

        try:
            carta = Carta(palo=HEART, figura=12)
        except FiguraCartaError as ex:
            ocurre_excepcion = True
        self.assertTrue(ocurre_excepcion)

    def test_tipo_es_valido(self):
        """
        Las cartas en el poker solo pueden ser de 4 tipos: 
        - Corazones
        - Diamantes
        - Treboles
        - Picas
        """
        carta = Carta(palo=DIAMONDS, figura=5)
        self.assertTrue(carta.palo , DIAMONDS)

    def test_tipo_no_es_valido(self):
        """
        Las cartas en el poker solo pueden ser de 4 tipos: 
        - Corazones
        - Diamantes
        - Treboles
        - Picas
        """
        ocurre_excepcion = False
        try:
            carta = Carta(palo="OROS", figura=2)
        except TipoCartaError as ex:
            ocurre_excepcion = True
        self.assertTrue(ocurre_excepcion)

    def test_2_cartas_son_iguales(self):
        """
        Comparamos si dadas 2 cartas el programa reconoce que son iguales
        """
        carta1 = Carta(palo=HEART, figura="J")
        carta2 = Carta(palo=HEART, figura="J")
        self.assertTrue(carta1, carta2)