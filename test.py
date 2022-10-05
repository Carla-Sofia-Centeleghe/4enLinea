# Test para el 4 en linea
from distutils.command.build import build
from msilib.schema import Patch
import unittest

from tablero import tablero_del_juego
from contar import contar_juego
from juego import juego
from colorama import init, Fore, Style

#@Patch(build.input)
#@Patch(build.print)


class Test4enLinea(unittest.TestCase):
    # Test para el funcionamiento la creacion del tablero
    def setUp(self):
        self.tablero = tablero_del_juego()

    def test_crear_tablero(self):
        self.tablero.crear_tablero()
        self.assertEqual(self.tablero.tablero, [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

    def test_imprimir_tablero(self):
        pass

    #def test_lugar_vacio(self, indice, columna):
    #    self.tablero.crear_tablero()
    #    self.tablero.lugar_vacio([2] ,[5] ,-1)
    #    self.assertEqual(self.tablero.lugar_vacio[2], [5], -1)

    def test_columna_valida(self):
        pass

    def test_colocar_pieza(self):
        pass

    #para saber cuantas veces se llama el main
    #def test_quit(self, Patch.print, Patch.input):


if __name__ == "__main__":
    unittest.main()
