from constantes import *
from PIL import Image
import time
from pyautogui import sleep , locate
import raton

def donde_esta_el_dealer():
        mesa_juego = Image.open(RUTA_SCREEN_SHOT)

def capturar_dealer_abajo(img):
    capturar_dealer(DEALER_ABAJO_X, DEALER_ABAJO_Y, RUTA_DEALER_ABAJO, img)

def capturar_dealer(x, y, ruta_guardar_imagen, img):
    # pixel arriba izquierda
    punto_izquierda_arriba_x = x
    punto_izquierda_arriba_y = y
    # pixel abajo derecha
    punto_derecha_abajo_x = punto_izquierda_arriba_x + caja_dealer_ancho
    punto_derecha_abajo_y = punto_izquierda_arriba_y + caja_dealer_altura
    box = (punto_izquierda_arriba_x, punto_izquierda_arriba_y, punto_derecha_abajo_x, punto_derecha_abajo_y)
    region = img.crop(box)

    hola= locate(img, region, confidence=CONFIANZA)

    region.save(ruta_guardar_imagen)

if __name__ == "__main__":
    while True:
        # Captura la imagen de la mesa
        mesa_juego = Image.open(RUTA_SCREEN_SHOT)
        # captura la imagen de cada jugador
        capturar_dealer_abajo(mesa_juego)
        print("dealer capturado")
        sleep(5)