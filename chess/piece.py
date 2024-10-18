from .constants import QUEEN_KING_DIRECTIONS  # Importar las direcciones comunes

class Piece:
    
    def __init__(self, color):
        self._color_ = color
        self._movimientos_dama_rey = QUEEN_KING_DIRECTIONS  # Usar la constante de direcciones
    
    def get_color(self):
        return self._color_

    def possible_moves_general(self, fila_inicio, columna_inicio, direcciones, un_paso=False):
        movimientos = []
        for direccion in direcciones:
            nueva_fila, nueva_columna = fila_inicio, columna_inicio
            while True:
                nueva_fila += direccion[0]
                nueva_columna += direccion[1]
                if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                    movimientos.append((nueva_fila, nueva_columna))
                    if un_paso:
                        break
                else:
                    break
        return movimientos
