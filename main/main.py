#from pyautogui import * 
#import keyboard
#import random
#import win32con
#import raton
#import monitor
#import vision
#import pyautogui
#from constantes import * 
#from ventana import Ventana
#import threading

#from src.main.calculos.distancias.distancias import distancia_euclidea
#
import sys
sys.path.insert(0, 'C:/Users/spuzi/OneDrive/Documentos/proyectos/poker-bot/src/main')

from main.constantes import combinaciones
print(sys.path)

#print(distancia_euclidea((2,3), (-3,5)))

#def worker():
#    print (threading.currentThread().getName(), 'Lanzado')
#    time.sleep(2)
#    print (threading.currentThread().getName(), 'Deteniendo')
#
#def servicio():
#    print(threading.currentThread().getName(), 'Lanzado')
#    print (threading.currentThread().getName(), 'Deteniendo')
#
#def lanzar_ventana():
#    print(threading.currentThread().getName(), 'Lanzado')
#    ventana = Ventana()
#    ventana.mostrar_ventana()
#    print (threading.currentThread().getName(), 'Deteniendo')
#
#def hacer_algo():
#    while True:
#        coordenadas = vision.capturar_mesa_juego()
#        vision.capturar_imagen(x_posicion=coordenadas[0], 
#                               y_posicion=coordenadas[1],
#                               anchura=coordenadas[2],
#                               altura=coordenadas[3],
#                               ruta= RUTA_MESA_JUEGO)
#    
#        print(coordenadas[0]) 
#        print(coordenadas[1])
#        print(coordenadas[2])
#        print(coordenadas[3])
#        sleep(5)
#
#    #estrella = pyautogui.locateOnScreen(ICONO_ESTRELLA_FAVORITO_ESQUINA_IZQUIERDA_ARRIBA, confidence=CONFIANZA)
#    #cursor_x, cursor_y = raton.get_posicion_cursor()
#    #distancia_x = estrella.left - cursor_x 
#    #distancia_y = estrella.top - cursor_y
#    #print(distancia_x, distancia_y)
#    ##print(estrella)
#
##hilo_ventana = threading.Thread(target=lanzar_ventana, name="Ventana" )
#hilo_algo = threading.Thread(target=hacer_algo, name="hacer algo" )
#hilo_algo.start()
##hilo_ventana.start()
##ventana = Ventana()
#
#