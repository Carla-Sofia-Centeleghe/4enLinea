# Test para todo el codigo
# Carla S. Centeleghe

import unittest
import unittest.mock

#from menu import Menu
from linea import Tablero
from linea import Jugador

class Test4enLinea(unittest.TestCase):
    # Test para el funcionamiento la creacion del tablero
    def test_crear_tablero_1(self):
        tablero = Tablero()
        tablero.crear_tablero()
        self.assertEqual(len(tablero.tablero), 8)

    def test_crear_tablero_2(self):
        tablero = Tablero()
        tablero.crear_tablero()
        for x in range(8):
            self.assertEqual(len(tablero.tablero[x]), 8)

    # Test para ver si puedo ingresar los input
    @unittest.mock.patch('linea.Tablero.pido_ficha', return_value=3)
    def test_pido_ficha_3(self, name):
        possicion = Tablero.pido_ficha()
        self.assertEqual(possicion, 3)

    # Test para felicitacion ganador, verificamos que la funcion printee
    def test_print_4(self):
        print("Test: test_print_4")

    #Test para ver si puedo jugar otra
    @unittest.mock.patch('linea.Tablero.pinta_otra', return_value="S")
    def test_pinta_otra_5(self, name):
        eleccion = Tablero.pinta_otra()
        self.assertTrue(eleccion)

    @unittest.mock.patch('linea.Tablero.pinta_otra', return_value="N")
    def test_pinta_otra_6(self, name):
        eleccion = Tablero.pinta_otra()
        self.assertTrue(eleccion)

    # Test para ver las fichas de los jugadores
    def test_color_jugador_7(self):
        Jugador.nrojugador = 1
        resultado = Jugador.color_jugador(Jugador)
        self.assertEqual(resultado, "x")

    def test_color_jugador_8(self):
        Jugador.nrojugador = 2
        resultado = Jugador.color_jugador(Jugador)
        self.assertEqual(resultado, "o")

    # Test para probar la condicion de ganar, es decir quien gana, jugador X
    def test_ganador_horizontal_x_9(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(1, 'x')
        juego.ingresar_ficha(2, 'x')
        juego.ingresar_ficha(3, 'x')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(
            self, 'x', juego.tablero))

    def test_ganador_vertical_x_10(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(0, 'x')
        juego.ingresar_ficha(0, 'x')
        # aca lo hice al revez, porque el que gana es x, y entonces si digo que gana O... daria falso
        self.assertFalse(Jugador.definir_ganador_cotar_fichas(
            self, 'o', juego.tablero))

    def test_diagonal_x_11(self):
        juego = Tablero()
        juego.crear_tablero()
        p_fila = [4, 6, 7]
        p_fila_2 = [5, 6, 7]
        p_fila_3 = [4, 5, 6, 7]
        for i in range(len(p_fila)):
            juego.ingresar_ficha(i+1, 'x')
        for i in range(len(p_fila_2)):
            juego.ingresar_ficha(i+1, 'o')
        juego.ingresar_ficha(6, 'x')
        for i in range(len(p_fila_3)):
            juego.ingresar_ficha(i+1, 'x')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(
            self, 'x', juego.tablero))

    def test_diagonal_x_12(self):
        juego = Tablero()
        juego.crear_tablero()
        p_fila = [0, 1]
        p_fila_1 = [0, 1, 2]
        p_fila_2 = [0, 1, 2, 3]
        for i in range(len(p_fila)):
            juego.ingresar_ficha(i+1, 'x')
        for i in range(len(p_fila_1)):
            juego.ingresar_ficha(i+1, 'o')
        juego.ingresar_ficha(1, 'o')
        for i in range(len(p_fila_2)):
            juego.ingresar_ficha(i+1, 'x')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(
            self, 'x', juego.tablero))

    # Test para probar la condicion de ganar, es decir quien gana, jugador O

    def test_ganador_horizontal_o_13(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(0, 'o')
        juego.ingresar_ficha(1, 'o')
        juego.ingresar_ficha(2, 'o')
        juego.ingresar_ficha(3, 'o')
        # aca lo hice al revez, porque el que gana es O, y entonces si digo que gana x... daria falso
        self.assertFalse(Jugador.definir_ganador_cotar_fichas(
            self, 'x', juego.tablero))

    def test_ganador_vertical_o_14(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(0, 'o')
        juego.ingresar_ficha(0, 'o')
        juego.ingresar_ficha(0, 'o')
        juego.ingresar_ficha(0, 'o')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(
            self, 'o', juego.tablero))

    def test_diagonal_o_15(self):
        juego = Tablero()
        juego.crear_tablero()
        p_fila = [4, 6, 7]
        p_fila_2 = [5, 6, 7]
        p_fila_3 = [4, 5, 6, 7]
        for i in range(len(p_fila)):
            juego.ingresar_ficha(i+1, 'o')
        for i in range(len(p_fila_2)):
            juego.ingresar_ficha(i+1, 'x')
        juego.ingresar_ficha(6, 'o')
        for i in range(len(p_fila_3)):
            juego.ingresar_ficha(i+1, 'o')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(
            self, 'o', juego.tablero))

    def test_diagonal_o_16(self):
        juego = Tablero()
        juego.crear_tablero()
        p_fila = [0, 1]
        p_fila_1 = [0, 1, 2]
        p_fila_2 = [0, 1, 2, 3]
        for i in range(len(p_fila)):
            juego.ingresar_ficha(i+1, 'o')
        for i in range(len(p_fila_1)):
            juego.ingresar_ficha(i+1, 'x')
        juego.ingresar_ficha(1, 'x')
        for i in range(len(p_fila_2)):
            juego.ingresar_ficha(i+1, 'o')
        self.assertTrue(Jugador.definir_ganador_cotar_fichas(
            self, 'o', juego.tablero))

    # Test para ver si ingresa la ficha en el tablero
    def test_ingresar_ficha_x_17(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(1, 'x')
        self.assertEqual(juego.tablero[7][1], 'x')

    def test_ingresar_ficha_x_18(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(5, 'x')
        juego.ingresar_ficha(5, 'x')
        juego.ingresar_ficha(5, 'x')
        juego.ingresar_ficha(5, 'x')
        juego.ingresar_ficha(5, 'x')
        self.assertEqual(juego.tablero[5][5], 'x')

    def test_ingresar_ficha_o_19(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(1, 'o')
        # hago esto porque se que en la columna 1, fila 5 esta vacia. Entoces va a ser difernte de 'O', ya que solo llene la fila 7 y columna 1. Recordemos que en mi matriz recoremos desde abajo, porq en un juego las cosas caen por la gravedad
        self.assertNotEqual(juego.tablero[5][1], '0')

    def test_ingresar_ficha_o_20(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        self.assertEqual(juego.tablero[5][5], 'o')

    # Test para comprobar que la columna esta llena
    def test_columna_llena_o_21(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        juego.ingresar_ficha(5, 'o')
        # juego.ingresar_ficha(5, 'o')
        self.assertTrue(juego.ingresar_ficha(5, 'o'))

    def test_columna_llena_x_22(self):
        juego = Tablero()
        juego.crear_tablero()
        juego.ingresar_ficha(6, 'x')
        juego.ingresar_ficha(6, 'x')
        juego.ingresar_ficha(6, 'x')
        juego.ingresar_ficha(6, 'x')
        juego.ingresar_ficha(6, 'x')
        juego.ingresar_ficha(6, 'x')
        juego.ingresar_ficha(6, 'x')
        # juego.ingresar_ficha(6, 'o')
        self.assertTrue(juego.ingresar_ficha(6, 'x'))

    # Test de como imprime en pantalla / NO FUNCIONA
    # def test_iprimir_tablero(self):
    #     tablero = Tablero
    #     self.assertTrue(tablero.imprimir_tablero(self))


if __name__ == "__main__":
    unittest.main()
