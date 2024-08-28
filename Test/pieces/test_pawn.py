import unittest
from game.pieces import Pawn

class TestPawn:
    def __init__(self, color):
        self.color = color

    def basic_pawn_moves(self, row, col):
        moves = []
        if self.color == "BLACK":
            if row < 7:
                moves.append((row + 1, col))
            if row == 1:
                moves.append((row + 2, col))
        else:  # Para los peones blancos
            if row > 0:
                moves.append((row - 1, col))
            if row == 6:
                moves.append((row - 2, col))
        return moves


    def test_eat_pieces_with_pawn(self):
        test_cases = [
            ("BLACK", [(7, 0), (7, 2)], 6, 1),
            ("WHITE", [(5, 0), (5, 2)], 6, 1)
        ]
        
        for color, expected_moves, start_row, start_col in test_cases:
            pawn = Pawn(color)
            self.assertEqual(set(pawn.eat_pieces_with_peon(start_row, start_col)), set(expected_moves))