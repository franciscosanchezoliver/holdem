import win32api, win32con, win32gui
import time

def click_izquierdo(x, y):
    """
    Hace un click en la posicion de la pantalla
    """
    # Pulsamos el click derecho
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_derecho(x, y):
    """
    Hace un click en la posicion de la pantalla
    """
    # Pulsamos el click derecho
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def get_posicion_cursor():
    """
    Devuelve la posicion del cursor
    """
    return win32gui.GetCursorInfo()[2]



