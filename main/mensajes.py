from termcolor import colored

class Mensajes():
    def __init__(self):
        # Cada tipo de mensaje va precedido por unos tags
        self.info_tag = "[INFO] "
        self.error_tag = "[ERROR] "
        
    def info(self, contenido):
        print(colored(self.info_tag, 'blue') + contenido)
    
    def error(self, contenido):
        print(colored(self.error_tag, 'red') + contenido)

if __name__ == "__main__":
    mensajes = Mensajes()
    mensajes.info("esto es un mensaje de informacion")
    mensajes.error("esto es un mensaje de error")