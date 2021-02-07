from excepciones import FiguraCartaError, TipoCartaError
from constantes import PALOS, FIGURAS, HEART, DIAMONDS, CLUB, SPADE, FIGURAS_PESO
from termcolor import colored

class Carta:

    def __init__(self, palo: str, figura):

        # Las cartas del poker pueden ser tanto una letra como un numero
        # en caso de que sea una letra puede ser solo de 4 tipos: J, Q, K, A
        # En caso de que sea un numero debera estar comprendido entre 2 y 10
        if (figura not in FIGURAS):
            raise FiguraCartaError

        # En el poker una carta tiene que ser de uno de los 4 palos
        # si nos dan otro tipo entonces lanzamos un error
        if palo not in PALOS: 
            raise TipoCartaError

        self.palo = palo
        self.figura = figura

    def mostrar_carta(self):
        """
        Imprime que carta es con su figura y su color
        """
        if self.palo == HEART:
            print(colored(str(self.figura) + '♥'  ,'red'))

        if self.palo == DIAMONDS:
            print(colored(str(self.figura) + '♦'  ,'blue'))

        if self.palo == CLUB:
            print(colored(str(self.figura) + '♣'  ,'green'))

        if self.palo == SPADE:
            print(str(self.figura) + '♠' )

    
    def __eq__(self, otra_carta):
        """
        Metodo para comparar si 2 cartas son iguales
        """
        return self.figura == otra_carta.figura
    
    def __ne__(self, otra_carta):
        """
        Metodo para comparar si 2 cartas son distintas
        """
        return not self.__eq__(otra_carta)

    def __lt__(self, other):
        figura_carta1 = self.figura
        figura_carta2 = other.figura
        peso1 = FIGURAS_PESO[str(figura_carta1)]
        peso2= FIGURAS_PESO[str(figura_carta2)]
        return peso1 < peso2
    
    def __gt__(self, other):
        return not self.__lt__(other)
