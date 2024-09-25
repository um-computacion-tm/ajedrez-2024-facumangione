import unittest
from unittest.mock import MagicMock
from game.pieces.rook import Rook

class PruebaTorre(unittest.TestCase):

#Verifica que el método __str__ de la clase Torre devuelva 'R' para una torre blanca y 'r' para una torre negra.

    def test_metodo_str(self):
        torre_blanca = Rook('WHITE')
        torre_negra = Rook('BLACK')
        self.assertEqual(str(torre_blanca), 'R')
        self.assertEqual(str(torre_negra), 'r')
        
#Comprueba que el método possible_moves de una torre blanca, ubicada en el centro del tablero, devuelva los movimientos correctos.

    def test_movimientos_posibles_torre_blanca(self):
        torre = Rook('WHITE')
        fila_inicial, col_inicial = 4, 4
        movimientos_esperados = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), 
                                 (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        movimientos_resultantes = torre.possible_moves(fila_inicial, col_inicial)
        self.assertEqual(sorted(movimientos_resultantes), sorted(movimientos_esperados))

#Verifica que el método possible_moves funcione correctamente para una torre negra en el centro del tablero.

    def test_movimientos_posibles_torre_negra(self):
        torre = Rook('BLACK')
        fila_inicial, col_inicial = 4, 4
        movimientos_esperados = [(3, 4), (2, 4), (1, 4), (0, 4), (5, 4), (6, 4), (7, 4), 
                                 (4, 3), (4, 2), (4, 1), (4, 0), (4, 5), (4, 6), (4, 7)]
        movimientos_resultantes = torre.possible_moves(fila_inicial, col_inicial)
        self.assertEqual(sorted(movimientos_resultantes), sorted(movimientos_esperados))

if __name__ == '__main__':
    unittest.main()
