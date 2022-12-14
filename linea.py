# Tablero del Tablero
# Juego del JUGADOR
# Menu, es donde se efecutan las funciones y hace juncionar al juego
# Carla S. Centeleghe

from colorama import init, Fore, Style
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
        # Entonces si columna esta llena devuelve true, caso contrario false
        if self.tablero[0][possicion] == " " and self.tablero[1][possicion] != " ":
            self.tablero[0][possicion] = ficha
            return True
        for i in reversed(range(self.columna)):
            if self.tablero[1][possicion] != " ":
                c = c+1
                print("\n" + Fore.YELLOW + "Columna llena!!!  " +
                      Fore.BLUE + "Intenta en otra columna\n")
                if c == 1:
                    return True
                return False
            if self.tablero[i+1][possicion] == " ":
                self.tablero[i+1][possicion] = ficha
                return False
        
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
        eleccion = input("??Revancha? [S/N] ")
        if eleccion == "S":
            print('Lo siento, no quiero jugar devuelta')
            return True
        elif eleccion == "N":
            return True

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

# Clase principal, que hace funcionar el programa
class Menu:
    def __init__(self) -> None:
        pass
    # Funcion que comienza a correr el juego
    def menu():
        while True:
            # Imprimo por pantalla (con colorcito) el nombre del juego
            print(Fore.YELLOW + "4" + " " + Fore.GREEN + "E" + Fore.BLUE + "N" + " " + Fore.RED +
                  "L" + Fore.CYAN + "i" + Fore.MAGENTA + "N" + Fore.WHITE + "E" + Fore.YELLOW + "A\n")
            # Imprimo por pantalla un indice de opciones
            arbol_b = input("1- UNO vs UNO"
                            "\n"
                            "2- Salir"
                            "\n"
                            "Elige: ")
            if arbol_b == "2":
                break
            if arbol_b == "1":
                # Empieza a ejecutar y llamar junciones
                while True:
                    tablero = Tablero()
                    tablero.crear_tablero()  # Creo el tablero

                    j1 = Jugador()
                    j1.color_jugador()

                    j2 = Jugador()
                    j2.color_jugador()
                    tablero.unoVSuno(j1, j2)

                    tablero.pinta_otra()  # Revancha, vuelve a ejecutarel prograa
                    return True
            break

if __name__ == "__main__":
    Menu.menu()
