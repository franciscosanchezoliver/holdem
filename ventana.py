from tkinter import * 
import vision
import keyboard

class Ventana:

    def __init__(self):
        self.root = Tk()
        self.root.title("Asistente poker")

    def mover_ventana(self, x, y, anchura, altura):
        """
        pone la pantalla en la posicion 200, 400 de la pantalla
        """
        self.root.geometry("{}x{}+{}+{}".format(str(anchura), str(altura),str(x), str(y)))

    def mostrar_ventana(self):
        self.calcular_tamanio_mesa_juego()
        self.root.mainloop()

    def calcular_tamanio_mesa_juego(self):

        posicion_x_mesa_juego, posicion_y_mesa_juego, anchura_mesa_juego, altura_mesa_juego = vision.capturar_mesa_juego()

        print("x:", posicion_x_mesa_juego)
        print("y:", posicion_y_mesa_juego)
        print("anchura:", anchura_mesa_juego)
        print("altura:", altura_mesa_juego)

        self.mover_ventana(posicion_x_mesa_juego, posicion_y_mesa_juego, anchura=anchura_mesa_juego, altura=altura_mesa_juego)


