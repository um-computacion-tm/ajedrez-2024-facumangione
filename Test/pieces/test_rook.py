import unittest
from game.pieces import Rook
from game.board import Board    


class TestRook(unittest.TestCase):

    def test_str(self):
        rook = Rook("WHITE")
        self.assertEqual(
            str(rook),
            "♖",
        )

    def test_basic_rook_moves(self):
        rook = Rook("WHITE")
        expected_moves = [(i, 0) for i in range(8) if i != 0] + [(0, i) for i in range(8) if i != 0]
        self.assertEqual(rook.basic_rook_moves(0, 0), expected_moves)

    def test_move_vertical_desc(self):
        rook = Rook("WHITE")
        possibles = rook.basic_rook_moves(4, 1)
        expected_moves = [(r, 1) for r in range(5, 8)]
        self.assertEqual(
            possibles,
            expected_moves
        )

    def test_move_vertical_asc(self):
        rook = Rook("WHITE")
        possibles = rook.basic_rook_moves(4, 1)
        expected_moves = [(r, 1) for r in range(0, 4)]
        self.assertEqual(
            possibles,
            expected_moves
        )

    def test_rook_moves_out_of_bounds(self):
        rook = Rook("WHITE")
        # Movimientos fuera del tablero desde la esquina inferior izquierda
        expected_moves = [(i, 0) for i in range(1, 8)] + [(0, i) for i in range(1, 8)]
        self.assertEqual(rook.basic_rook_moves(0, 0), expected_moves)

if __name__ == '__main__':
    unittest.main()
