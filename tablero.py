# Tablero del Tablero
# Carla S. Centeleghe


from colorama import init, Fore, Style
from juego import *

# Uso esta linea para que me funcione colorama y se vuleva a su color orginal luego
init(autoreset=True)

# Declavo algunas variables utiles
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2

# Clase donde estan casi todas mis funciones


class Tablero:

    def __init__(self):
        self.fila = 8
        self.columna = 8
        self.tablero = []

    # Creo el tablero (vacio)
    def crear_tablero(self):
        for fila in range(self.fila):
            self.tablero.append([])
            for self.columna in range(8):
                self.tablero[fila].append(" ")
        return self.tablero

    # Input para la ficha
    def pido_ficha(self):
        possicion = int(input("Ingresa la columna para colocar la pieza: "))
        return possicion

    # Este metodo tirar las fichas y revisa que no este llena la columna
    def ingresar_ficha(self, possicion, ficha):
        c = 0
        for i in reversed(range(self.columna)):
            if self.tablero[1][possicion] != " ":
                c = c+1
                print("\n" + Fore.YELLOW + "Columna llena!!!  " +
                      Fore.BLUE + "Intenta en otra columna\n")
                if c == 1:
                    return True
                break
            if self.tablero[i+1][possicion] == " ":
                self.tablero[i+1][possicion] = ficha
                break

    # Como se imprime por pantalla
    def imprimir_tablero(self):
        print("|", end="")
        for f in range(0, len(self.tablero)):
            print(f, end="|")
        print("")
        # Colores
        for fila in self.tablero:
            print("|", end="")
            for valor in fila:
                color_terminal = Fore.MAGENTA
                if valor == AZUL:
                    color_terminal = Fore.CYAN
                print(color_terminal + valor, end="")
                print(end="")
                print("|", end="")
            print("")
        # Final
        print("+", end="")
        for f in range(0, len(self.tablero)):
            print("-", end="+")
        print("")
        return True

    # Imprimo un ganaste al gandor
    def ganador_felicitaciones(self, jugador_actual):
        if jugador_actual.ficha == "x":
            print(Fore.MAGENTA + "JUGADOR 1\n" + Fore.YELLOW + "G" + Fore.GREEN + "A" + Fore.BLUE + "N" + Fore.RED +
                  "A" + Fore.CYAN + "S" + Fore.MAGENTA + "T" + Fore.WHITE + "E" + Fore.YELLOW + "!" + Fore.RED + "!")
        elif jugador_actual.ficha == "o":
            print(Fore.CYAN + "JUGADOR 2\n" + Fore.YELLOW + "G" + Fore.GREEN + "A" + Fore.BLUE + "N" + Fore.RED +
                  "A" + Fore.CYAN + "S" + Fore.MAGENTA + "T" + Fore.WHITE + "E" + Fore.YELLOW + "!" + Fore.RED + "!")

    def unoVSuno(self, jugador, jugador2):
        # Imprime las fichas y colores de los jugadores
        print(Fore.MAGENTA +
              "Jugador 1: X " + Fore.CYAN + "| Jugador 2: O")

        # Empieza el juego
        while True:
            print("Juega el " + Fore.MAGENTA + "JUGADOR 1: X")
            self.imprimir_tablero()     # imprime el tablero
            a = self.pido_ficha()       # pide la ficha del jugador
            self.ingresar_ficha(a, jugador.ficha)   # coloca la ficha
            # chequea si gana o no
            if jugador.definir_ganador_cotar_fichas(jugador.ficha, self.tablero) == True:
                self.imprimir_tablero()
                self.ganador_felicitaciones(jugador)  # felicita al gandor
                break

            # todo devuelta pero para el jugador 2
            print("Juega el " + Fore.CYAN + "JUGADOR 2: O")
            self.imprimir_tablero()
            a = self.pido_ficha()
            self.ingresar_ficha(a, jugador2.ficha)
            if jugador2.definir_ganador_cotar_fichas(jugador2.ficha, self.tablero) == True:
                self.imprimir_tablero()
                self.ganador_felicitaciones(jugador2)
                break

        #sigue y sigue, hasta que uno gane

    #otra partida boucle
    def pinta_otra(self):
        eleccion = input("¿Revancha? [S/N] ")
        if eleccion == "S":
            print('Lo siento, no quiero jugar devuelta')
            return True
        elif eleccion == "N":
            return True
