from jugador import Jugador


class Mesa():

    def __init__(self, jugadores, bote, cartas_en_mesa):
        self.bote = bote
        self.jugadores = jugadores
        self.cartas_en_mesa = cartas_en_mesa
    
    def get_numero_jugadores(self):
        return len(self.jugadores)
