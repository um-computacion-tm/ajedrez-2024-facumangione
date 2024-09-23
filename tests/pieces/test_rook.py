# test_rook.py

import unittest
from game.pieces.rook import Rook

class TestRook(unittest.TestCase):

    def test_str(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♖")
        rook_black = Rook("BLACK")
        self.assertEqual(str(rook_black), "♜")

    def test_basic_rook_moves_center(self):
        rook = Rook("WHITE")
        expected_moves = [
            # Horizontales
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7),
            # Verticales
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4)
        ]
        self.assertCountEqual(rook.basic_rook_moves(4, 4), expected_moves)

    def test_basic_rook_moves_corner(self):
        rook = Rook("WHITE")
        expected_moves = [
            # Horizontales
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            # Verticales
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)
        ]
        self.assertCountEqual(rook.basic_rook_moves(0, 0), expected_moves)

    def test_basic_rook_moves_edge(self):
        rook = Rook("WHITE")
        expected_moves = [
            # Horizontales
            (0, 4), (0, 5), (0, 6), (0, 7),
            # Verticales
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)
        ]
        self.assertCountEqual(rook.basic_rook_moves(0, 4), expected_moves)

    def test_move_vertical_desc(self):
        rook = Rook("WHITE")
        possibles = rook.basic_rook_moves(4, 1)
        expected_moves = [(5, 1), (6, 1), (7, 1)]
        self.assertCountEqual(
            [move for move in possibles if move[1] == 1 and move[0] > 4],
            expected_moves
        )

    def test_move_vertical_asc(self):
        rook = Rook("WHITE")
        possibles = rook.basic_rook_moves(4, 1)
        expected_moves = [(3, 1), (2, 1), (1, 1), (0, 1)]
        self.assertCountEqual(
            [move for move in possibles if move[1] == 1 and move[0] < 4],
            expected_moves
        )

    def test_rook_moves_out_of_bounds(self):
        rook = Rook("WHITE")
        # Movimientos fuera del tablero desde la esquina inferior izquierda
        expected_moves = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]
        self.assertCountEqual(rook.basic_rook_moves(0, 0), expected_moves)

if __name__ == '__main__':
    unittest.main()
