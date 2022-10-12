# Otra opcio para contar quien gana

# from xmlrpc.client import boolean
# import numpy as np
# from tablero import tablero_del_juego
# from colorama import init, Fore, Style

# # Declavo algunas variables utiles
# ESPACIO_VACIO = " "
# VIOLETA = "x"
# AZUL = "o"
# JUGADOR_1 = 1
# JUGADOR_2 = 2
# CONECTA = 4

# class contar_ficha():
#     def ganador(self,booleano = int):
#         #comprobar las filas
#         for fila in booleano:
#             #if si hay por lo menos 4
#             if sum(fila) >= 4:
#                 if sum(fila[4]) >= 4 or sum(fila[1:5]) >= 4 or sum(fila[2:6]) >= 4 or sum(fila[3:]) >= 4:
#                     return True
#         #comprobar por columnas
#         for fila in booleano.T:
#             #if si hay por lo menos 4
#             if sum(fila) >= 4:
#                 if sum(fila[4]) >= 4 or sum(fila[1:5]) >= 4 or sum(fila[2:6]) >= 4 or sum(fila[3:]) >= 4:
#                     return True
#         #comprobar las diagonales
#         for k in range(-2,4):
#             if sum(np.diag(booleano,k)) >= 4:
#                 if sum(np.diag(booleano, k)[4]) >= 4 or sum(np.diag(booleano, k)[::-1][:4]):
#                     return True
#             if sum(np.rot90(booleano, k)) >= 4:
#                 if sum(np.rot90(booleano, k)[4]) >= 4 or sum(np.rot90(booleano, k)[::-1][:4]):
#                     return True
#         return False, ' '

