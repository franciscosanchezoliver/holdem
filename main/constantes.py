# para considerar que ha encontrado una imagen
# necesita una confianza
CONFIANZA = 0.8

# Turnos
FLOP = 'FLOP'
TURN = 'TURN'
RIVER = 'RIVER'


# Figuras
FIGURAS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

# Palos
HEART = "HEART" # Corazones
DIAMONDS = "DIAMONDS" # Diamantes
CLUB = "CLUB" # Treboles
SPADE = "SPADE" # Picas
PALOS = [HEART, DIAMONDS, CLUB ,SPADE]


# Combinaciones
HIGH_CARD = "HIGH_CARD" # Carta Alta
PAIR = "PAIR" # Pareja
TWO_PAIRS = "TWO_PAIRS" # Double Pareja
SET = "SET" # Trio
STRAIGHT = "STRAIGHT" # Escalera
FLUSH = "FLUSH" # Color
FULL_HOUSE = "FULL_HOUSE" # Full
POKER = "POKER" # Poker
STRAIGHT_FLUSH = "STRAIGHT_FLUSH" # Escalera de Color
ROYAL_FLUSH = "ROYAL_FLUSH" # Escalera Real

#############
# MESA DE 6 #
#############
BTN = 'BTN' # Dealer/button
SB = 'SB' # Small Blind
BB = 'BB' # Big Blind
UTG = 'UTG' # Under the Gun
MP = 'MP' # Middle Position 
CO = 'CO' # Cut Off

##########
# DEALER #
##########
DEALER_ESTA_ABAJO = "DEALER_ESTA_ABAJO"
DEALER_ESTA_IZQUIERDA_ABAJO = "DEALER_ESTA_IZQUIERDA_ABAJO" 
DEALER_ESTA_IZQUIERDA_ARRIBA = "DEALER_ESTA_IZQUIERDA_ARRIBA" 
DEALER_ESTA_ARRIBA = "DEALER_ESTA_ARRIBA" 
DEALER_ESTA_DERECHA_ARRIBA = "DEALER_ESTA_DERECHA_ARRIBA"
DEALER_ESTA_DERECHA_ABAJO = "DEALER_ESTA_DERECHA_ABAJO" 

#############
# JUGADORES #
#############

# las dimensiones de una caja para capturar un jugador
caja_jugador_ancho = 100
caja_jugador_altura = 45

# La posicion en la mesa de cada jugador
JUGADOR_ABAJO_X = 445
JUGADOR_ABAJO_Y = 455

JUGADOR_IZQUIERDA_ABAJO_X = 36
JUGADOR_IZQUIERDA_ABAJO_Y = 333

JUGADOR_IZQUIERDA_ARRIBA_X = 65
JUGADOR_IZQUIERDA_ARRIBA_Y = 130

JUGADOR_ARRIBA_X = 395
JUGADOR_ARRIBA_Y = 66 

JUGADOR_DERECHA_ARRIBA_X = 774 
JUGADOR_DERECHA_ARRIBA_Y = 128

JUGADOR_DERECHA_ABAJO_X = 806 
JUGADOR_DERECHA_ABAJO_Y = 333 

##########
# DEALER #
##########
# Las dimensiones de una caja para capturar el boton del dealer
caja_dealer_ancho = 30
caja_dealer_altura = 30

# Diferentes posiciones del dealer
DEALER_ABAJO_X = 364
DEALER_ABAJO_Y = 389

DEALER_IZQUIERDA_ABAJO_X = 175 
DEALER_IZQUIERDA_ABAJO_Y = 288

DEALER_IZQUIERDA_ARRIBA_X = 281
DEALER_IZQUIERDA_ARRIBA_Y = 147 

DEALER_ARRIBA_X = 497
DEALER_ARRIBA_Y = 145 

DEALER_DERECHA_ARRIBA_X = 729 
DEALER_DERECHA_ARRIBA_Y = 198 

DEALER_DERECHA_ABAJO_X = 682
DEALER_DERECHA_ABAJO_Y = 354


##########################
# IDENTIFICACION DE MESA #
##########################
RUTA_SCREEN_SHOT = './screen_shots/img.png'
RUTA_MESA_JUEGO = './screen_shots/mesa_juego.png'
ICONO_STARTS_ESQUINA_IZQUIERDA_ARRIBA = "./iconos/icono_starts_esquina_izquierda_arriba.png"
ICONO_SONRISA_CHAT_ABAJO = "./iconos/icono_sonriente.png"
ICONO_ESTRELLA_FAVORITO_ESQUINA_IZQUIERDA_ARRIBA = "./iconos/estrella_favorito_esquina_izquierda_arriba.png"
ICONO_LOBBY = "./iconos/icono_lobby.png"

#############
# JUGADORES #
#############
# Ruta donde se guarda la foto de cada jugador
RUTA_JUGADOR_ABAJO = './screen_shots/jugador_abajo.png'
RUTA_JUGADOR_IZQUIERDA_ABAJO = './screen_shots/jugador_izquierda_abajo.png'
RUTA_JUGADOR_IZQUIERDA_ARRIBA = './screen_shots/jugador_izquierda_arriba.png'
RUTA_JUGADOR_ARRIBA = './screen_shots/jugador_arriba.png'
RUTA_JUGADOR_DERECHA_ARRIBA = './screen_shots/jugador_derecha_arriba.png'
RUTA_JUGADOR_DERECHA_ABAJO = './screen_shots/jugador_derecha_abajo.png'

##########
# DEALER #
##########
ICONO_DEALER = "./iconos/dealer.png"
ICONO_DEALER_NO_PARECIDO = "./iconos/dealer_no_parecido.png"
MESA_CON_DEALER_ABAJO = "./screen_shots/mesa_con_dealer_abajo.png"
MESA_CON_DEALER_IZQUIERDA_ABAJO = "./screen_shots/mesa_con_dealer_izquierda_abajo.png"
MESA_CON_DEALER_IZQUIERDA_ARRIBA = "./screen_shots/mesa_con_dealer_izquierda_arriba.png"
MESA_CON_DEALER_ARRIBA = "./screen_shots/mesa_con_dealer_arriba.png"
MESA_CON_DEALER_DERECHA_ARRIBA = "./screen_shots/mesa_con_dealer_derecha_arriba.png"
MESA_CON_DEALER_DERECHA_ABAJO = "./screen_shots/mesa_con_dealer_derecha_abajo.png"

# Ruta donde se guarda la foto de cada dealer
RUTA_DEALER_ABAJO = './screen_shots/dealer_abajo.png'
RUTA_DEALER_IZQUIERDA_ABAJO = './screen_shots/dealer_izquierda_abajo.png'
RUTA_DEALER_IZQUIERDA_ARRIBA = './screen_shots/dealer_izquierda_arriba.png'
RUTA_DEALER_ARRIBA = './screen_shots/dealer_arriba.png'
RUTA_DEALER_DERECHA_ARRIBA = './screen_shots/dealer_derecha_arriba.png'
RUTA_DEALER_DERECHA_ABAJO = './screen_shots/dealer_derecha_abajo.png'
