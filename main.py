# Main, aca llamas a todos

from tablero import tablero_del_juego
from contar import contar_juego
from juego import juego
from colorama import init, Fore, Style

init(autoreset=True)


def main():
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
                game = tablero_del_juego()
                tablero_base = game.crear_tablero()  # self

                juego.unoVSuno(tablero_base)
                if not juego.pinta_otra():
                    break


main()
