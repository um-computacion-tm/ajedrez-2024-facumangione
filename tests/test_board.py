import unittest
from chess.board import Board
from chess.exceptions import NonCaptureOwnPieceError, NonPassOverPieceError, GameOverException

class TestTablero(unittest.TestCase):
# Verifica el comportamiento del método is_valid_move de la clase Board cuando no hay una pieza en la posición de origen  
    def test_movimiento_invalido_sin_pieza(self):
        tablero = Board()
        self.assertFalse(tablero.is_valid_move(3, 3, 4, 4))

# Verifica que el método move_piece lance la excepción NonCaptureOwnPieceError cuando se intenta capturar una pieza del mismo jugador.
    def test_intento_captura_propia_pieza(self):
        tablero = Board()
        tablero.board = [[None for _ in range(8)] for _ in range(8)]
        tablero.board[7][0] = 'R'
        tablero.board[6][0] = 'P'
        with self.assertRaises(NonCaptureOwnPieceError) as contexto:
            tablero.move_piece(7, 0, 6, 0)
        self.assertEqual(str(contexto.exception), "You cannot capture your own pieces.")

# Verifica que la excepción NonPassOverPieceError se lance cuando una pieza intenta moverse sobre otra.
    def test_pieza_pasa_sobre_otras(self):
        tablero = Board()
        tablero._positions_ = [[None for _ in range(8)] for _ in range(8)]
        tablero._positions_[0][0] = 'R'
        tablero._positions_[0][1] = 'P'
        with self.assertRaises(NonPassOverPieceError) as contexto:
            tablero.move_piece(0, 0, 0, 2)
        self.assertEqual(str(contexto.exception), "You cannot pass over other pieces.")

# Verifica que se lance la excepción GameOverException con el mensaje "White wins" cuando las piezas negras se quedan sin piezas en el tablero.
    def test_partida_finalizada_gana_blancas(self):
        tablero = Board()
        class Torre:
            def get_color(self):
                return 'WHITE'
        tablero._positions_ = [[None for _ in range(8)] for _ in range(8)]
        tablero._positions_[7][7] = Torre()
        with self.assertRaises(GameOverException) as contexto:
            tablero._verificar_fin_partida()
        self.assertEqual(str(contexto.exception), "White wins")

# Verifica que se lance la excepción GameOverException con el mensaje "Black wins" cuando las piezas blancas se quedan sin piezas en el tablero.
    def test_partida_finalizada_gana_negras(self):
        tablero = Board()
        class Torre:
            def get_color(self):
                return 'BLACK'
        tablero._positions_ = [[None for _ in range(8)] for _ in range(8)]
        tablero._positions_[0][0] = Torre()
        with self.assertRaises(GameOverException) as contexto:
            tablero._verificar_fin_partida()
        self.assertEqual(str(contexto.exception), "Black wins")

# Comentar: crtl+k+c
# Descomentar: ctrl+k+u

if __name__ == '__main__':
    unittest.main()
