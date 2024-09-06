import unittest
from unittest.mock import patch
from game.chess import Chess
from game.cli import play

class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)  # Considerando que imprime el tablero y el turno
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch('builtins.input', side_effect=['hola', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)  # Se imprime un mensaje de error adicional
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', '1', '2', 'hola'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)  # Se imprime un mensaje de error adicional
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', '1', '2', '1'])
    @patch('builtins.print')
    @patch.object(Chess, 'move', side_effect=Exception("InvalidMove"))
    def test_invalid_move(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)  # Se imprime el tablero, el turno y un mensaje de error
        self.assertEqual(mock_chess_move.call_count, 1)

if __name__ == '__main__':
    unittest.main()
