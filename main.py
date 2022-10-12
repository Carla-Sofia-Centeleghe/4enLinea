# Main, aca llamas a todos

from tablero import *
from juego import *
from colorama import init, Fore, Style
from contar2 import *


init()


def main():
    t1 = tablero_del_juego()

    while True:
        print(Fore.YELLOW + "4" + " " + Fore.GREEN + "E" + Fore.BLUE + "N" + " " + Fore.RED +
              "L" + Fore.CYAN + "i" + Fore.MAGENTA + "N" + Fore.WHITE + "E" + Fore.YELLOW + "A\n")

        print
        arbol_b = input("1- UNO vs UNO"
                        "\n"
                        "2- Salir"
                        "\n"
                        "Elige: ")
        if arbol_b == "2":
            break
        if arbol_b == "1":
            while True:
                tablero = tablero_del_juego.crear_tablero(t1.filas,t1.columnas,t1.tablero)
                juego.unoVSuno(tablero)
                if not juego.pinta_otra():
                    break

main()
