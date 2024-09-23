# test_pawn.py

import unittest
from game.pieces.pawn import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.pawn_white = Pawn("WHITE")
        self.pawn_black = Pawn("BLACK")

    def test_str(self):
        self.assertEqual(str(self.pawn_white), "♙")
        self.assertEqual(str(self.pawn_black), "♟︎")

    def test_basic_pawn_moves_white_initial(self):
        # Un peón blanco en la fila 6 (posición inicial) puede mover dos casillas hacia adelante
        expected_moves = [(5, 0), (4, 0)]
        self.assertCountEqual(self.pawn_white.basic_pawn_moves(6, 0), expected_moves)

    def test_basic_pawn_moves_white_non_initial(self):
        # Un peón blanco no en posición inicial solo puede mover una casilla hacia adelante
        expected_moves = [(5, 0)]
        self.assertCountEqual(self.pawn_white.basic_pawn_moves(5, 0), expected_moves)

    def test_basic_pawn_moves_black_initial(self):
        # Un peón negro en la fila 1 (posición inicial) puede mover dos casillas hacia adelante
        expected_moves = [(2, 0), (3, 0)]
        self.assertCountEqual(self.pawn_black.basic_pawn_moves(1, 0), expected_moves)

    def test_basic_pawn_moves_black_non_initial(self):
        # Un peón negro no en posición inicial solo puede mover una casilla hacia adelante
        expected_moves = [(2, 0)]
        self.assertCountEqual(self.pawn_black.basic_pawn_moves(2, 0), expected_moves)

    def test_pawn_moves_out_of_bounds_white(self):
        # Un peón blanco en la última fila no puede moverse más hacia adelante
        expected_moves = []
        self.assertCountEqual(self.pawn_white.basic_pawn_moves(0, 0), expected_moves)

    def test_pawn_moves_out_of_bounds_black(self):
        # Un peón negro en la última fila no puede moverse más hacia adelante
        expected_moves = []
        self.assertCountEqual(self.pawn_black.basic_pawn_moves(7, 0), expected_moves)

    def test_pawn_capture_moves_white(self):
        # Suponiendo que el método `basic_pawn_moves` incluye capturas (si es así)
        # Por simplicidad, este test solo verifica movimientos básicos
        pass  # Implementar si el método maneja capturas

    def test_pawn_capture_moves_black(self):
        # Suponiendo que el método `basic_pawn_moves` incluye capturas (si es así)
        # Por simplicidad, este test solo verifica movimientos básicos
        pass  # Implementar si el método maneja capturas

if __name__ == '__main__':
    unittest.main()
