# Diseño del tablero y sus colores


from colorama import init, Fore, Style

init(autoreset=True)

# Declavo algunas variables utiles
ESPACIO_VACIO = 0
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2
CONECTA = 4


class tablero_del_juego():
    def __init__(self):
        self.tablero = []

    #defino el tamaño de la matriz
    def crear_tablero(self):
        self.tablero = [[0 for columna in range(9)] for fila in range(8)]

    # como se imprime por pantalla
    def imprimir_tablero(tablero):
        print("|", end="")
        for f in range(1, len(tablero[0]) + 1):
            print(f, end="|")
        print("")
    # Colores
        for fila in tablero:
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
        for f in range(1, len(tablero) + 1):
            print("-", end="+")
        print("")

    #Lugar vacio en la matriz, es decir que esa columna no esta completa
    def lugar_vacio(columna, tablero):
        indice = len(tablero) - 1
        while indice >= 0:
            if tablero[indice][columna] == ESPACIO_VACIO:
                return indice
            indice -= 1
        return -1

    #Si esta llena o si existe el lugar
    def columna_valida(tablero):
        while True:
            columna = input("Ingresa la columna para colocar la pieza: ")
            # si columna es mas grande que mi matrix salta error
            if columna <= 0 or columna > len(tablero[0]):
                print("Columna no válida")
            elif tablero[0][columna - 1] != ESPACIO_VACIO:
                print("Esa columna ya está llena")
            else:
                return columna - 1

    #Pongo la pieza
    def colocar_pieza(columna, jugador, tablero):
        color = VIOLETA
        if jugador == JUGADOR_2:
            color = AZUL
        fila = tablero_del_juego.lugar_vacio(columna, tablero)
        if fila == -1:
            return False
        tablero[fila][columna] = color
        return True

    # Defino los colores de los jugadores
    def color_jugador(jugador):
        color = VIOLETA
        if jugador == JUGADOR_2:
            color = AZUL
        return color
