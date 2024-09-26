import unittest
from game.pieces.bishop import Bishop

class VerificarAlfil(unittest.TestCase):

#Prueba que el método __str__ del Alfil devuelva 'B' si es blanco y 'b' si es negro.
    def test_representacion_str(self):
        alfil_blanco = Bishop('WHITE')
        alfil_negro = Bishop('BLACK')
        self.assertEqual(str(alfil_blanco), 'B')
        self.assertEqual(str(alfil_negro), 'b')

#Evalúa los movimientos permitidos de un alfil blanco desde el centro del tablero. Llama al método possible_moves con una fila y columna iniciales, y verifica que los movimientos devueltos sean los esperados.
    def test_movimientos_disponibles_blanco(self):
        alfil = Bishop('WHITE')
        movimientos_esperados = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(alfil.possible_moves(3, 3), movimientos_esperados)

# Verifica los movimientos permitidos de un alfil negro desde el centro del tablero.Llama al método possible_moves con una fila y columna iniciales, y compara los movimientos obtenidos con los esperados.
    def test_movimientos_disponibles_negro(self):
        alfil = Bishop('BLACK')
        movimientos_esperados = [
            (2, 2), (1, 1), (0, 0),  # Diagonal superior izquierda
            (2, 4), (1, 5), (0, 6),  # Diagonal superior derecha
            (4, 2), (5, 1), (6, 0),  # Diagonal inferior izquierda
            (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal inferior derecha
        ]
        self.assertEqual(alfil.possible_moves(3, 3), movimientos_esperados)

if __name__ == '__main__':
    unittest.main()
