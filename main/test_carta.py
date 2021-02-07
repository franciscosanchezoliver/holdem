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
        self.assertTrue(carta1 == carta2)
    
    def test_2_cartas_son_distintas(self):
        """
        Comparamos si dadas 2 cartas el programa reconoce que son distintas
        """
        carta1 = Carta(palo=HEART, figura="K")
        carta2 = Carta(palo=HEART, figura="J")
        self.assertTrue(carta1 != carta2)

    def test_carta_es_menor_que_otra(self):
        """
        Comparamos que el valor de una carta es menor que el valor de otra
        """
        carta1 = Carta(palo=HEART, figura=3)
        carta2= Carta(palo=HEART, figura=5)
        self.assertTrue(carta1 < carta2)

        carta1 = Carta(palo=HEART, figura=3)
        carta2= Carta(palo=HEART, figura="K")
        self.assertTrue(carta1 < carta2)

        carta1 = Carta(palo=HEART, figura="Q")
        carta2= Carta(palo=HEART, figura="K")
        self.assertTrue(carta1 < carta2)



    def test_carta_es_mayor_que_otra(self):
        """
        Comparamos que el valor de una carta es menor que el valor de otra
        """
        carta1 = Carta(palo=HEART, figura=5)
        carta2= Carta(palo=HEART, figura=3)
        self.assertTrue(carta1 > carta2)

    def test_cartas_valen_lo_mismo(self):
        """
        Comparamos que dos cartas con la misma figura valen igual
        """
        carta1 = Carta(palo=CLUB, figura=5)
        carta2= Carta(palo=HEART, figura=5)
        self.assertTrue(carta1 == carta2)

    def test_cartas_estan_ordenadas_correctamente(self):
        """
        Dada una serie de cartas al ordenarlas se tienen que ordenar
        de forma correcta
        """
        lista_cartas = [
            Carta(palo=CLUB, figura=5),
            Carta(palo=HEART, figura=5),
            Carta(palo=DIAMONDS, figura=2),
            Carta(palo=CLUB, figura="A"),
            Carta(palo=CLUB, figura="K"),
            Carta(palo=SPADE, figura="J")
        ]
        lista_cartas.sort()
        ultima_carta = lista_cartas[-1]
        self.assertTrue(ultima_carta.palo == CLUB, ultima_carta.figura=="A")
   