import pyautogui
from PIL import Image
from pytesseract import * 
from constantes import *

# Hay que usar un .exe para poder usar esta libreria
# se puede descargar e instalar desde https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def imagen_a_texto(ruta_imagen):
    # Abrimos una imagen
    img = Image.open(ruta_imagen)
    # Transformamos la imagen a texto
    output = pytesseract.image_to_string(img)
    return (output)


if __name__ == "__main__":
    jugador_abajo = imagen_a_texto(RUTA_JUGADOR_ABAJO) 
    jugador_izquierda_abajo = imagen_a_texto(RUTA_JUGADOR_IZQUIERDA_ABAJO) 
    jugador_izquierda_arriba = imagen_a_texto(RUTA_JUGADOR_IZQUIERDA_ARRIBA)
    jugador_arriba = imagen_a_texto(RUTA_JUGADOR_ARRIBA)
    jugador_derecha_arriba = imagen_a_texto(RUTA_JUGADOR_DERECHA_ARRIBA)
    jugador_derecha_abajo = imagen_a_texto(RUTA_JUGADOR_DERECHA_ABAJO)

    print("jugador_abajo")
    print(jugador_abajo)

    print("jugador_izquierda_abajo")
    print(jugador_izquierda_abajo)

    print("jugador_izquierda_arriba")
    print(jugador_izquierda_arriba)

    print("jugador_arriba")
    print(jugador_arriba)

    print("jugador_derecha_arriba")
    print(jugador_derecha_arriba)

    print("jugador_derecha_abajo")
    print(jugador_derecha_abajo)


