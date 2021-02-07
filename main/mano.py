from carta import Carta

class Mano():

    def __init__(self, carta1, carta2):
        self.carta1 = carta1
        self.carta2 = carta2

    def es_pareja(self):
        es_pareja = self.carta1.figura == self.carta2.figura
        return es_pareja

    def es_suited(self):
        es_mismo_color = self.carta1.palo == self.carta2.palo
        return es_mismo_color
