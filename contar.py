#Me sirve para contar cuantas fichas lleva cada jugador, y si saber quien cano cuando sume 4

from tablero import tablero_del_juego
from colorama import init, Fore, Style

# Declavo algunas variables utiles
ESPACIO_VACIO = " "
VIOLETA = "x"
AZUL = "o"
JUGADOR_1 = 1
JUGADOR_2 = 2
CONECTA = 4


class contar_juego():
    def conteo_derecha(fila, columna, color, tablero):
        fin_columnas = len(tablero[0])
        contador = 0
        for i in range(columna, fin_columnas):
            if contador >= CONECTA:
                return contador
            if tablero[fila][i] == color:
                contador += 1
            else:
                contador = 0
        return contador

    def conteo_izquierda(fila, columna, color, tablero):
        contador = 0
        for i in range(columna, -1, -1):
            if contador >= CONECTA:
                return contador
            if tablero[fila][i] == color:
                contador += 1
            else:
                contador = 0

        return contador

    def conteo_abajo(fila, columna, color, tablero):
        fin_filas = len(tablero)
        contador = 0
        for i in range(fila, fin_filas):
            if contador >= CONECTA:
                return contador
            if tablero[i][columna] == color:
                contador += 1
            else:
                contador = 0
        return contador

    def conteo_arriba(fila, columna, color, tablero):
        contador = 0
        for i in range(fila, -1, -1):
            if contador >= CONECTA:
                return contador
            if contador >= CONECTA:
                return contador
            if tablero[i][columna] == color:
                contador += 1
            else:
                contador = 0
        return contador

    def conteo_arriba_derecha(fila, columna, color, tablero):
        contador = 0
        numero_fila = fila
        numero_columna = columna
        while numero_fila >= 0 and numero_columna < len(tablero[0]):
            if contador >= CONECTA:
                return contador
            if tablero[numero_fila][numero_columna] == color:
                contador += 1
            else:
                contador = 0
            numero_fila -= 1
            numero_columna += 1
        return contador

    def conteo_arriba_izquierda(fila, columna, color, tablero):
        contador = 0
        numero_fila = fila
        numero_columna = columna
        while numero_fila >= 0 and numero_columna >= 0:
            if contador >= CONECTA:
                return contador
            if tablero[numero_fila][numero_columna] == color:
                contador += 1
            else:
                contador = 0
            numero_fila -= 1
            numero_columna -= 1
        return contador

    def conteo_abajo_derecha(fila, columna, color, tablero):
        contador = 0
        numero_fila = fila
        numero_columna = columna
        while numero_fila < len(tablero) and numero_columna < len(tablero[0]):
            if contador >= CONECTA:
                return contador
            if tablero[numero_fila][numero_columna] == color:
                contador += 1
            else:
                contador = 0
            numero_fila += 1
            numero_columna += 1
        return contador

    def direcciones():
        return [
            'izquierda',
            'arriba',
            'abajo',
            'derecha',
            'arriba_derecha',
            'abajo_derecha',
            'arriba_izquierda'
        ]

    def conteo(fila, columna, color, tablero):
        direcciones = contar_juego.direcciones()
        for direccion in direcciones:
            
            # funcion salva vidas, globals te deja unir por asi decirlo dos palabras.Entoces puedo usar eso para llamar a la funcion y no tener que hacer un if gigante
            funcion = contar_juego.conteo_ + direccion
            conteo = funcion(fila, columna, color, tablero)
            if conteo >= CONECTA:
                return conteo
        return 0

    def ganador(jugador, tablero):
        color = tablero_del_juego.color_jugador(jugador)
        for f, fila in enumerate(tablero):
            for c, celda in enumerate(fila):
                conteo = contar_juego.conteo(f, c, color, tablero)
                if conteo >= CONECTA:
                    return True
        return False
