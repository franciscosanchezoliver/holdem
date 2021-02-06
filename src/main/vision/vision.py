from constantes import * 
import pyautogui
import time
import capturar_jugadores
from PIL import Image
import imagehash
import numpy as np
import cv2
from pyautogui import sleep 

def imagen_esta_en_pantalla(ruta_imagen):
    """ 
    Te dice si cierta imagen esta en la pantalla con un rango 
    de confianza
    """
    if pyautogui.locateOnScreen(ruta_imagen, confidence=CONFIANZA) != None:
        return True
    else:
        return False

def guardar_imagen_mesa_juego():
    coordenadas = capturar_mesa_juego()
    capturar_imagen(x_posicion=coordenadas[0], 
                               y_posicion=coordenadas[1],
                               anchura=coordenadas[2],
                               altura=coordenadas[3],
                               ruta = RUTA_MESA_JUEGO)

def capturar_imagen(x_posicion, y_posicion, anchura, altura, ruta):
    """
    Hace una sreenshot de la pantalla en la posicionq ue le digas
    """
    captura_pantalla = pyautogui.screenshot(region=(x_posicion, y_posicion, anchura, altura))
    captura_pantalla.save(ruta)
    print("Imagen capturada en :", ruta)

def capturar_mesa_juego():
    esquina_izquierda_arriba = pyautogui.locateOnScreen(ICONO_ESTRELLA_FAVORITO_ESQUINA_IZQUIERDA_ARRIBA, confidence=CONFIANZA)
    esquina_izquierda_abajo = pyautogui.locateOnScreen(ICONO_SONRISA_CHAT_ABAJO , confidence=CONFIANZA)
    esquina_derecha_arriba = pyautogui.locateOnScreen( ICONO_LOBBY, confidence=CONFIANZA)

    anchura = (esquina_derecha_arriba.left + esquina_derecha_arriba.width) - esquina_izquierda_arriba.left
    altura = (esquina_izquierda_abajo.top + esquina_izquierda_abajo.height) - (esquina_izquierda_arriba.top - esquina_izquierda_arriba.height)

    return esquina_izquierda_arriba.left, esquina_izquierda_arriba.top, anchura, altura 


def capturar_subimagen(imagen):
    Image.open("/path/to/image.jpg")
    box = (100, 100, 400, 400)
    region = im.crop(box)
    return region

def calcular_similitud_entre_imagenes():
    hash0 = imagehash.average_hash(Image.open(ICONO_DEALER)) 
    hash1 = imagehash.average_hash(Image.open("./iconos/dealer_no_parecido.png")) 
    cutoff = 5
    print ("diferencia", hash0 - hash1)

    if hash0 - hash1 < cutoff:
      print('images are similar')
    else:
      print('images are not similar')

def ver_si_esta_el_color_rojo_en_la_imagen(img):
    # Definimos un rango de colores que lo consideramos
    # como "rojo"
    rojo_min = 160
    rojo_max = 255
    verde_min = 0 
    verde_max = 50 
    azul_min = 0 
    azul_max = 50

    # Le pasamos los colores en las cordenadas GBR en lugar de RGB porque 
    # asi lo toma la libreria
    limites_color = [([verde_min, azul_min, rojo_min], [verde_max, azul_max, rojo_max])]

    for (lower, upper) in limites_color:
        # Creamos un array para los limites
        lower = np.array(lower , dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # Encontramos los colores que esten entre los
        # limites que hemos definido y aplicamos una mascara
        mascara = cv2.inRange(img, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mascara)

        if output.max() > 200:
            return True
        else:
            return False

        # mostramos la comparacion de la imagen y la mascara
        #cv2.imshow("images", np.hstack([img, output]))
        #cv2.waitKey(0)


if __name__ == "__main__":
    while True:

        #imagen = cv2.imread(ICONO_DEALER)
        #ver_si_esta_el_color_rojo_en_la_imagen(imagen)

        ## Captura la imagen de la mesa
        guardar_imagen_mesa_juego()
        mesa_juego = Image.open(RUTA_MESA_JUEGO)
        # captura la imagen de cada jugador
        capturar_jugadores.capturar_jugador_abajo(mesa_juego)
        capturar_jugadores.capturar_izquierda_abajo(mesa_juego)
        capturar_jugadores.capturar_izquierda_arriba(mesa_juego)
        capturar_jugadores.capturar_arriba(mesa_juego)
        capturar_jugadores.capturar_derecha_arriba(mesa_juego)
        capturar_jugadores.capturar_derecha_abajo(mesa_juego)
        print("jugadores capturados")
        sleep(5)