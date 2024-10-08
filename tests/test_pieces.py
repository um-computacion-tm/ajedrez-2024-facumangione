import unittest
from chess.piece import Piece

class VerificacionPieza(unittest.TestCase):
# Comprueba que al instanciar una pieza con el color blanco, este se almacene correctamente.
    def test_color_pieza_blanca(self):
        color_blanco = 'WHITE'
        pieza_blanca = Piece(color_blanco)
        self.assertEqual(pieza_blanca._color_, color_blanco)

# Verifica que al crear una pieza con el color negro, dicho color se asigne correctamente.
    def test_color_pieza_negra(self):
        color_negro = 'BLACK'
        pieza_negra = Piece(color_negro)
        self.assertEqual(pieza_negra._color_, color_negro)

# Evalúa que el método get_color de una pieza blanca devuelva "WHITE" como color.
    def test_obtener_color_pieza_blanca(self):
        pieza = Piece("WHITE")
        self.assertEqual(pieza.get_color(), "WHITE")
    
    # Verifica que el método get_color devuelva "BLACK" cuando la pieza creada es de color negro.
    def test_obtener_color_pieza_negra(self):
        pieza = Piece("BLACK")
        self.assertEqual(pieza.get_color(), "BLACK")

if __name__ == '__main__':
    unittest.main()
