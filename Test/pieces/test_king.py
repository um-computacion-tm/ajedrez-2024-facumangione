import unittest
from game.pieces import King

class TestKing(unittest.TestCase):
    def test_basic_king_moves(self):
        king = King("black")
        self.assertEqual(king.color, "black")

        start_row, start_col = 4, 4

        # Movimientos esperados del rey (una casilla en cualquier dirección)
        expected_moves = [
            (3, 3), (3, 4), (3, 5),  # Superior
            (4, 3),         (4, 5),  # Lados
            (5, 3), (5, 4), (5, 5)   # Inferior
        ]

        self.assertEqual(set(king.basic_king_moves(start_row, start_col)), set(expected_moves))