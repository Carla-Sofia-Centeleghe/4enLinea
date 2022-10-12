# Diseño del tablero y sus colores


from colorama import init, Fore, Style

init(autoreset=True)

# Declavo algunas variables utiles
ESPACIO_VACIO = " "
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2
CONECTA = 4


class tablero_del_juego():
    def __init__(self):
        self.filas = 7
        self.columnas = 9
        self.tablero=[]

    #defino el tamaño de la matriz
    def crear_tablero(self,filas, columnas):
        tablero = []
        for fila in range(filas):
            tablero.append([])
            for columna in range(8):
                tablero[fila].append(ESPACIO_VACIO)
        return tablero

    # como se imprime por pantalla
    def imprimir_tablero(tablero):
        print("|", end="")
        for f in range(1, len(tablero)):

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
        for f in range(1, len(tablero)):
            print("-", end="+")
        print("")


    #Lugar vacio en la matriz, es decir que esa columna no esta completa
    def lugar_vacio(columna, tablero):
        #columna = 8
        indice = len(tablero) - 1
        while indice >= 0:
            if tablero[indice][columna] == ESPACIO_VACIO:
                return indice
            indice -= 1
        return -1


    #Input para las fichas
    #def fichas(ficha_ingresada):
    #    ficha_ingresada: int = input("Ingresa la columna para colocar la pieza: ")

    #Si esta llena o si existe el lugar y para pedir que coloque la ficha
    def columna_valida(tablero):
        while True:
            columna = int(input("Ingresa la columna para colocar la pieza: "))

            #tablero_del_juego.fichas(ficha_ingresada=int)

            # si columna es mas grande que mi matrix salta error
            if columna <= 0 or columna > len(tablero[0]):
                print("Columna no válida")
            elif tablero[0][columna - 1] != ESPACIO_VACIO:
                print("Esa columna ya está llena")
            else:
                return columna - 1

    #Pongo la pieza
    def colocar_pieza(columna, jugador_actual, tablero):
       
        #columna = 8
        #columna =  tablero_del_juego.columna_valida()
        color = VIOLETA
        if jugador_actual == JUGADOR_2:
            color = AZUL
        fila = tablero_del_juego.lugar_vacio(columna, tablero)
        if fila == -1:
            return False
        #coloco la fihca    
        tablero[fila][columna] = color
        return True

    # Defino los colores de los jugadores
    def color_jugador(jugador):
        color = VIOLETA
        if jugador == JUGADOR_2:
            color = AZUL
        return color
