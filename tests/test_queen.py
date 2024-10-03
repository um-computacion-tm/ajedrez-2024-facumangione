import unittest
from chess.piece import Piece

class PruebaPieza(unittest.TestCase):

# Verifica que al crear una instancia de la clase Piece con el color blanco, se almacene correctamente.
    def test_pieza_blanca(self):
        color = 'WHITE'
        pieza = Piece(color)
        self.assertEqual(pieza._color_, color)
# Comprueba que al crear una instancia de la clase Piece con el color negro, el color se guarde correctamente.
    def test_pieza_negra(self):
        color = 'BLACK'
        pieza = Piece(color)
        self.assertEqual(pieza._color_, color)

# Verifica que el método get_color devuelva "WHITE" cuando se inicializa una pieza con ese color.

    def test_obtener_color_blanco(self):
        pieza = Piece("WHITE")
        self.assertEqual(pieza.get_color(), "WHITE")
    
# Asegura que el método get_color retorne BLACK al crear una pieza con dicho color.
    
    def test_obtener_color_negro(self):
        pieza = Piece("BLACK")
        self.assertEqual(pieza.get_color(), "BLACK")
        
if __name__ == '__main__':
    unittest.main()
