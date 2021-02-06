from constantes import *
import cv2
from PIL import Image
import time
from pyautogui import sleep , locate
import raton
import vision
import numpy as np

def donde_esta_el_dealer():
        mesa_juego = Image.open(RUTA_SCREEN_SHOT)

def capturar_dealer_abajo(img):
    esta_abajo = capturar_dealer(DEALER_ABAJO_X, DEALER_ABAJO_Y, RUTA_DEALER_ABAJO, img)
    esta_abajo = DEALER_ESTA_ABAJO if esta_abajo else "" 
    return esta_abajo

def capturar_dealer_izquierda_abajo(img):
    esta_izquierda_abajo = capturar_dealer(DEALER_IZQUIERDA_ABAJO_X, DEALER_IZQUIERDA_ABAJO_Y, RUTA_DEALER_IZQUIERDA_ABAJO, img)
    esta_izquierda_abajo = DEALER_ESTA_IZQUIERDA_ABAJO if esta_izquierda_abajo else "" 
    return esta_izquierda_abajo


def capturar_dealer_izquierda_arriba(img):
    esta_izquierda_arriba = capturar_dealer(DEALER_IZQUIERDA_ARRIBA_X, DEALER_IZQUIERDA_ARRIBA_Y, RUTA_DEALER_IZQUIERDA_ARRIBA, img)
    esta_izquierda_arriba = DEALER_ESTA_IZQUIERDA_ARRIBA if esta_izquierda_arriba else ""
    return esta_izquierda_arriba

def capturar_dealer_arriba(img):
    esta_arriba = capturar_dealer(DEALER_ARRIBA_X, DEALER_ARRIBA_Y, RUTA_DEALER_ARRIBA, img)
    esta_arriba = DEALER_ESTA_ARRIBA if esta_arriba else ""
    return esta_arriba

def capturar_dealer_derecha_arriba(img):
    esta_derecha_arriba = capturar_dealer(DEALER_DERECHA_ARRIBA_X, DEALER_DERECHA_ARRIBA_Y, RUTA_DEALER_DERECHA_ARRIBA, img)
    esta_derecha_arriba = DEALER_ESTA_DERECHA_ARRIBA if esta_derecha_arriba else ""
    return esta_derecha_arriba

def capturar_dealer_derecha_abajo(img):
    esta_derecha_abajo = capturar_dealer(DEALER_DERECHA_ABAJO_X, DEALER_DERECHA_ABAJO_Y, RUTA_DEALER_DERECHA_ABAJO, img)
    esta_derecha_abajo = DEALER_ESTA_DERECHA_ABAJO if esta_derecha_abajo else ""
    return esta_derecha_abajo

def capturar_dealer(x, y, ruta_guardar_imagen, img):
    # pixel arriba izquierda
    punto_izquierda_arriba_x = x
    punto_izquierda_arriba_y = y
    # pixel abajo derecha
    punto_derecha_abajo_x = punto_izquierda_arriba_x + caja_dealer_ancho
    punto_derecha_abajo_y = punto_izquierda_arriba_y + caja_dealer_altura
    box = (punto_izquierda_arriba_x, punto_izquierda_arriba_y, punto_derecha_abajo_x, punto_derecha_abajo_y)
    region = img.crop(box)
    opencvImage = cv2.cvtColor(np.array(region), cv2.COLOR_RGB2BGR)
    return vision.ver_si_esta_el_color_rojo_en_la_imagen(opencvImage)
    #print(vision.ver_si_esta_el_color_rojo_en_la_imagen(imagen))

    #region.save(ruta_guardar_imagen)

def sacar_donde_esta_el_dealer(image):
    return capturar_dealer_abajo(image) +\
    capturar_dealer_izquierda_abajo(image) +\
    capturar_dealer_izquierda_arriba(image) +\
    capturar_dealer_arriba(image) +\
    capturar_dealer_derecha_arriba(image) +\
    capturar_dealer_derecha_abajo(image)
 

if __name__ == "__main__":
    # Captura la imagen de la mesa

    image = Image.open(MESA_CON_DEALER_ABAJO)
    donde_esta_el_dealer = sacar_donde_esta_el_dealer(image)
    print(donde_esta_el_dealer)
    #opencvImage = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    #print(vision.ver_si_esta_el_color_rojo_en_la_imagen(imagen))
    ## captura la imagen de cada jugador
    print("dealer capturado")
    #sleep(5)