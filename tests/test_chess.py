import unittest
from chess.chess import Chess
from chess.exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError

class TestAjedrez(unittest.TestCase):
# Esta función verifica que un objeto Chess se inicializa correctamente, asegurando que el turno inicial es de las piezas blancas y que el tablero esté bien configurado.
    def test_inicializacion(self):
        partida = Chess()  
        self.assertEqual(partida.turno, "WHITE")
        tablero = partida.get_board()
        self.assertIsNotNone(tablero)

# Esta función verifica que un peón blanco se mueva correctamente. Se asegura de que la posición final del peón no esté vacía, lo que indica que se movió correctamente.
    def test_realizar_movimientor_peon_valido(self):
        partida = Chess()
        partida.realizar_movimiento(6, 0, 4, 0)
        self.assertEqual(partida.turno, "BLACK")
        self.assertEqual(partida.get_board()[6][0], '.')
        self.assertIsNotNone(partida.get_board()[4][0])

# Esta función verifica que un caballo se mueva correctamente en el tablero. Confirma que la nueva posición del caballo no está vacía.
    def test_realizar_movimientor_caballo_valido(self):
        partida = Chess()
        partida.realizar_movimiento(7, 1, 5, 2)
        self.assertEqual(partida.turno, "BLACK")
        self.assertEqual(partida.get_board()[7][1], '.')
        self.assertIsNotNone(partida.get_board()[5][2])

# Verifica el comportamiento del método realizar_movimiento cuando no hay una pieza en la posición de origen, y asegura que se lance la excepción NonPieceOriginError
    def test_realizar_movimientor_sin_pieza1(self):
        partida = Chess()  # Asumiendo que Chess inicializa el tablero correctamente
        with self.assertRaises(NonPieceOriginError) as contexto:
            partida.realizar_movimiento(3, 3, 4, 3)  # Intento de mover una pieza inexistente
        self.assertEqual(str(contexto.exception), "There is no piece at the origin position.")

# Verifica el comportamiento del método realizar_movimiento cuando no hay una pieza en otra posición de origen, y asegura que se lance la excepción NonPieceOriginError.
    def test_realizar_movimientor_sin_pieza2(self):
        partida = Chess()  # Asumiendo que Chess inicializa el tablero correctamente
        with self.assertRaises(NonPieceOriginError) as contexto:
            partida.realizar_movimiento(3, 4, 4, 4)  # Intento de mover una pieza inexistente
        self.assertEqual(str(contexto.exception), "There is no piece at the origin position.")


# Verifica que cuando se intenta realizar_movimientor una pieza que no pertenece al jugador que tiene el turno, se lanza la excepción WrongTurnError.
    def test_turno_incorrecto(self):
        partida = Chess()
        partida.realizar_movimiento(6, 0, 4, 0)
        with self.assertRaises(WrongTurnError) as contexto:
            partida.realizar_movimiento(6, 1, 5, 2)
        self.assertEqual(str(contexto.exception), "It is not the turn of the selected piece.")

# Verifica que cuando se intenta realizar_movimientor una pieza a una posición inválida, se lanza la excepción InvalidPieceMoveError.
    def test_movimiento_invalido(self):
        partida = Chess()
        with self.assertRaises(InvalidPieceMoveError) as contexto:
            partida.realizar_movimiento(6, 0, 3, 0)
        self.assertEqual(str(contexto.exception), "Invalid move for the selected piece.")

# Verifica que el método para cambiar de turno funcione correctamente después de cada movimiento válido.
    def test_alternar_turno(self):
        partida = Chess()
        partida.realizar_movimiento(6, 0, 4, 0)
        self.assertEqual(partida.turno, "BLACK")
        partida.realizar_movimiento(1, 0, 3, 0)
        self.assertEqual(partida.turno, "WHITE")

if __name__ == '__main__':
    unittest.main()
