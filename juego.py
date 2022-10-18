# Juego del JUGADOR
# Carla S. Centeleghe

from tablero import Tablero

# Declavo algunas variables utiles
JUGADOR_1 = 1
JUGADOR_2 = 2

# Clase jugador, estan las funciones para las fichas y para ver quien gana


class Jugador:
    nrojugador = 0

    def __init__(self, ficha=None):
        Jugador.nrojugador += 1
        self.ficha = None

    # Defino los colores/fichas de los jugadores, los colores y fichas estan asociados porque printeo en color
    def color_jugador(self):
        if self.nrojugador == 1:
            self.ficha = "x"
        if self.nrojugador == 2:
            self.ficha = "o"

        return self.ficha

    # Contar las fichas, para ver la comdicion de ganar
    def definir_ganador_cotar_fichas(self, ficha, tablero):
        # Cuento las fihcas verticalmente
        for possicion in range(8):
            for i in range(5):
                if tablero[i][possicion] == ficha and tablero[i+1][possicion] == ficha and tablero[i+2][possicion] == ficha and tablero[i+3][possicion] == ficha:
                    return True

        # Cuento las fichas horizontalmente
        for posicion in range(5):
            for i in range(8):
                if tablero[i][posicion] == ficha and tablero[i][posicion+1] == ficha and tablero[i][posicion+2] == ficha and tablero[i][posicion+3] == ficha:
                    return True

        # Cuento las fichas diagonalmente positivo
        for possicion in range(5):
            for i in range(5):
                if tablero[i][possicion] == ficha and tablero[i+1][possicion+1] == ficha and tablero[i+2][possicion+2] == ficha and tablero[i+3][possicion+3] == ficha:
                    return True

        # Cuento las diagonales negativo
        for possicion in range(5):
            for i in range(3, 8):
                if tablero[i][possicion] == ficha and tablero[i-1][possicion+1] == ficha and tablero[i-2][possicion+2] == ficha and tablero[i-3][possicion+3] == ficha:
                    return False
        return False
