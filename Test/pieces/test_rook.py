import unittest
from game.pieces import Rook


class TestRook(unittest.TestCase):
    def test_basic_rook_moves(self):
        rook = Rook("blanco")
        self.assertEqual(rook.color, "blanco")
        expected_moves = [(i, 0) for i in range(8) if i != 0] + [(0, i) for i in range(8) if i != 0]
        self.assertEqual(rook.basic_rook_moves(0, 0), expected_moves)
    
    def test_rook_moves_out_of_bounds(self):
        rook = Rook("blanco")
        # Movimientos fuera del tablero desde la esquina inferior izquierda
        self.assertEqual(rook.basic_rook_moves(0, 0), [(i, 0) for i in range(1, 8)] + [(0, i) for i in range(1, 8)])
    
    def test_move_vertical_desc(self):
        rook = Rook("WHITE")
        self.assertEquals(
            str(rook),
            "♖",
        )