import unittest
from game.pieces import Bishop

class TestBishop(unittest.TestCase):
    def test_basic_bishop_moves(self):
        bishop = Bishop("blanco")
        self.assertEqual(bishop.color, "blanco")

        start_row, start_col = 3, 3

        # Movimientos esperados en todas las diagonales desde la posición (3, 3)
        expected_moves = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]

        # Convirtiendo las listas a sets para evitar problemas con el orden
        self.assertEqual(set(bishop.basic_bishop_moves(start_row, start_col)), set(expected_moves))
