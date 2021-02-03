from constantes import * 
import pyautogui
import time
import capturar_jugadores
from PIL import Image
import imagehash

def imagen_esta_en_pantalla(ruta_imagen):
    """ 
    Te dice si cierta imagen esta en la pantalla con un rango 
    de confianza
    """
    if pyautogui.locateOnScreen(ruta_imagen, confidence=CONFIANZA) != None:
        return True
    else:
        return False

def capturar_imagen(x_posicion, y_posicion, anchura, altura):
    """
    Hace una sreenshot de la pantalla en la posicionq ue le digas
    """
    captura_pantalla = pyautogui.screenshot(region=(x_posicion, y_posicion, anchura, altura))
    captura_pantalla.save(RUTA_SCREEN_SHOT)
    print("Imagen capturada en :", RUTA_SCREEN_SHOT)

def capturar_mesa_juego():
    esquina_izquierda_arriba = pyautogui.locateOnScreen(ICONO_ESTRELLA_FAVORITO_ESQUINA_IZQUIERDA_ARRIBA, confidence=CONFIANZA)
    esquina_izquierda_abajo = pyautogui.locateOnScreen(ICONO_SONRISA_CHAT_ABAJO , confidence=CONFIANZA)
    esquina_derecha_arriba = pyautogui.locateOnScreen( ICONO_LOBBY, confidence=CONFIANZA)

    anchura = (esquina_derecha_arriba.left + esquina_derecha_arriba.width) - esquina_izquierda_arriba.left
    altura = (esquina_izquierda_abajo.top + esquina_izquierda_abajo.height) - (esquina_izquierda_arriba.top - esquina_izquierda_arriba.height)

    return esquina_izquierda_arriba.left, esquina_izquierda_arriba.top, anchura, altura 

def capturar_jugadores():
    """
    Captura los datos de los diferentes jugadores que hay en la mesa
    """

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

