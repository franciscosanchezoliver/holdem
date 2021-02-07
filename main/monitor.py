import win32api

def numero_monitores():
    """
    Devuelve el numero de monitores
    """
    monitores = win32api.EnumDisplayMonitors()
    numero_monitores = len(monitores)
    return numero_monitores

