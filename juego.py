#detalles del juego

import random
from tablero import tablero_del_juego
from colorama import init, Fore, Style
#from contar import contar_juego
from contar2 import contar_ficha

init(autoreset=True)

# Declavo algunas variables utiles
ESPACIO_VACIO = " "
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2
CONECTA = 4


class juego():
    #elige el jugador que va a empezar el juego, es al azar. Porq uso una libreria para ello
    def elegir_jugador():
        return random.choice([JUGADOR_1, JUGADOR_2])

    #turnos y colores
    def turnos_colores(self, turno, tablero):
        print(Fore.MAGENTA +
              "Jugador 1: {VIOLETA} " + Fore.CYAN + "| Jugador 2: {AZUL}")
        if turno == JUGADOR_1:
            print("Juega el " + Fore.MAGENTA + "jugador 1 ({VIOLETA})")
        else:
            print("Juega el " + Fore.CYAN + "jugador 2 ({AZUL})")
        return tablero_del_juego.columna_valida(self, tablero)

    #imprimo un ganaste al gandor
    def ganador_felicitaciones(jugador_actual):
        if jugador_actual == JUGADOR_1:
            print(Fore.MAGENTA + "Jugador 1\n" + Fore.YELLOW + "G" + Fore.GREEN + "A" + Fore.BLUE + "N" + Fore.RED +
                  "A" + Fore.CYAN + "S" + Fore.MAGENTA + "T" + Fore.WHITE + "E" + Fore.YELLOW + "!" + Fore.RED + "!")
        else:
            print(Fore.CYAN + "Jugador 2\n" + Fore.YELLOW + "G" + Fore.GREEN + "A" + Fore.BLUE + "N" + Fore.RED +
                  "A" + Fore.CYAN + "S" + Fore.MAGENTA + "T" + Fore.WHITE + "E" + Fore.YELLOW + "!" + Fore.RED + "!")

    #mando a imorimir por terminal la ebolucion del tablero y el truno de la persona que toca
    def unoVSuno(self, tablero):
        jugador_actual = juego.elegir_jugador()
        while True:
            tablero_del_juego.imprimir_tablero(tablero)

            columna_turno: int = juego.turnos_colores(self,jugador_actual, tablero)

            pieza_en_el_tablero = tablero_del_juego.colocar_pieza(columna_turno,jugador_actual, tablero)
            if not pieza_en_el_tablero:
                print(Fore.RED + "¡mal! Proba otra vez")

            ganado = contar_ficha.ganador(jugador_actual, tablero)

            if ganado:
                tablero_del_juego.imprimir_tablero(tablero)
                juego.ganador_felicitaciones(jugador_actual)
                break
            else:  # cambia los jugadores, va dando los turnos
                if jugador_actual == JUGADOR_1:
                    jugador_actual = JUGADOR_2
                else:
                    jugador_actual = JUGADOR_1

    #otra partida boucle
    def pinta_otra():
        while True:
            eleccion = input("¿Revancha? [S/N] ")()
            if eleccion == "S":
                return True
            elif eleccion == "N":
                return False
