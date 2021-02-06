from constantes import *
from PIL import Image
import time
from pyautogui import sleep 
import raton

def capturar_jugador_abajo(img):
    capturar_jugador(JUGADOR_ABAJO_X, JUGADOR_ABAJO_Y, RUTA_JUGADOR_ABAJO, img)

def capturar_izquierda_abajo(img):
    capturar_jugador(JUGADOR_IZQUIERDA_ABAJO_X, JUGADOR_IZQUIERDA_ABAJO_Y, RUTA_JUGADOR_IZQUIERDA_ABAJO, img)

def capturar_izquierda_arriba(img):
    capturar_jugador(JUGADOR_IZQUIERDA_ARRIBA_X, JUGADOR_IZQUIERDA_ARRIBA_Y, RUTA_JUGADOR_IZQUIERDA_ARRIBA, img)

def capturar_arriba(img):
    capturar_jugador(JUGADOR_ARRIBA_X, JUGADOR_ARRIBA_Y, RUTA_JUGADOR_ARRIBA, img)

def capturar_derecha_arriba(img):
    capturar_jugador(JUGADOR_DERECHA_ARRIBA_X, JUGADOR_DERECHA_ARRIBA_Y, RUTA_JUGADOR_DERECHA_ARRIBA, img)

def capturar_derecha_abajo(img):
    capturar_jugador(JUGADOR_DERECHA_ABAJO_X, JUGADOR_DERECHA_ABAJO_Y, RUTA_JUGADOR_DERECHA_ABAJO, img)

def capturar_jugador(x, y, ruta_guardar_imagen, img):
    # pixel arriba izquierda
    punto_izquierda_arriba_x = x
    punto_izquierda_arriba_y = y
    # pixel abajo derecha
    punto_derecha_abajo_x = punto_izquierda_arriba_x + caja_jugador_ancho
    punto_derecha_abajo_y = punto_izquierda_arriba_y + caja_jugador_altura
    box = (punto_izquierda_arriba_x, punto_izquierda_arriba_y, punto_derecha_abajo_x, punto_derecha_abajo_y)
    region = img.crop(box)
    region.save(ruta_guardar_imagen)

