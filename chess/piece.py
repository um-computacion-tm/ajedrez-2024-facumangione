class Piece:
    
    # Constructor de la clase
    def __init__(self, color):
        #Constructor de la clase.
        self._color_ = color
        self._movimientos_dama_rey = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Obtener el color de la pieza
    def get_color(self):
        #Esta función devuelve el valor del atributo privado _color de la pieza.
        return self._color_

    # Movimientos posibles de las piezas
    def possible_moves_general(self, fila_inicio, columna_inicio, direcciones, un_paso=False):
        #La función devuelve los movimientos posibles de la pieza desde su posición actual.
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
