import unittest
from io import StringIO
from chess.cli import run_game as play, render_board_with_icons as show_board_with_icons, start_game
from unittest.mock import patch, MagicMock
from chess.chess import Chess

class TestCli(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_board_with_icons(self, mock_stdout):
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        show_board_with_icons(board)
        expected_output = (
            '♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n'
            '♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '· · · · · · · ·\n'
            '♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n'
            '♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('builtins.input', side_effect=['EXIT'])
    # def test_exit_game(self, mock_input, mock_stdout):
    #     chess = MagicMock()
    #     with self.assertRaises(SystemExit):
    #         play(chess)
    #     self.assertIn("Game over.", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('builtins.input', side_effect=['1', 'EXIT'])
    # def test_exit_mid_game(self, mock_input, mock_stdout):
    #     chess = MagicMock()
    #     with self.assertRaises(SystemExit):
    #         play(chess)
    #     self.assertIn("Game over.", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('builtins.input', side_effect=['1', '1', 'EXIT'])
    # def test_exit_later(self, mock_input, mock_stdout):
    #     chess = MagicMock()
    #     with self.assertRaises(SystemExit):
    #         play(chess)
    #     self.assertIn("Game over.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['6', '0', '4', '0'])
    @patch('chess.cli.render_board_with_icons')
    def test_valid_move_pawn(self, mock_show_board, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        play(chess)
        chess.move.assert_called_with(6, 0, 4, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '1', '5', '0'])
    @patch('chess.cli.render_board_with_icons')
    def test_valid_move_knight1(self, mock_show_board, mock_input, mock_stdout):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'white'
        play(chess)
        chess.move.assert_called_with(7, 1, 5, 0)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['7', '1', '5', '0'])
    def test_valid_move_knight_black(self, mock_stdout, mock_input):
        chess = MagicMock()
        chess.get_board.return_value = [['.']*8 for _ in range(8)]
        chess.turn = 'black'
        play(chess)
        chess.move.assert_called_with(7, 1, 5, 0)

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('builtins.input', side_effect=['0', '0', '8', '1'])
    # def test_invalid_coordinates(self, mock_stdout, mock_input):
    #     chess = MagicMock()
    #     chess.get_board.return_value = [['.']*8 for _ in range(8)]
    #     chess.turn = 'white'
    #     play(chess)
    #     self.assertIn("Row and column values must be between 0 and 7.", mock_stdout.getvalue())

    # @patch('builtins.input', side_effect=['&', '0', '1', '1'])
    # def test_symbol_coordinates(self, mock_input):
    #     chess = MagicMock()
    #     chess.get_board.return_value = [['.']*8 for _ in range(8)]
    #     chess.turn = 'white'
    #     with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
    #         play(chess)
    #         self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('builtins.input', side_effect=['a', 'b', 'c', 'd', 'EXIT'])
    # def test_non_numeric_input(self, mock_stdout, mock_input):
    #     chess = MagicMock()
    #     chess.get_board.return_value = [['.']*8 for _ in range(8)]
    #     chess.turn = 'white'
    #     play(chess)
    #     self.assertIn("You must enter numeric values between 0 and 7.", mock_stdout.getvalue())

        @patch('sys.stdout', new_callable=StringIO)
        @patch('builtins.input', side_effect=['7', '1', '5', '0', 'EXIT'])
        def test_valid_move_then_exit(self, mock_stdout, mock_input):
            chess = Chess()  # Usar el objeto real de Chess

            # Establecer el estado inicial del tablero si es necesario
            chess._tablero_.set_initial_state()  # Este método debe existir en Board o Chess para inicializar las piezas

            # Ahora llamamos a start_game, que ejecuta el juego
            start_game()

            # Verifica que el movimiento se haya realizado
            self.assertIn("Game over.", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
