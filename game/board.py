from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.pieces.king import King
from game.pieces.queen import Queen
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from exceptions import GameOverException, NonCaptureOwnPieceError, NonPassOverPieceError, NonCaptureForwardError

class Board:
    def __init__(self):
        # Inicializa la clase Board con las posiciones de las piezas en el tablero de ajedrez.
        # Crear el tablero vacío
        self._positions_ = [[None] * 8 for _ in range(8)]

        # Colocar las piezas en sus posiciones iniciales
        self._iniciar_posiciones_iniciales()

    def _iniciar_posiciones_iniciales(self):
        # Coloca todas las piezas en sus posiciones de inicio.
        # Torres (Rooks)
        self._positions_[0][0] = Rook("BLACK")
        self._positions_[0][7] = Rook("BLACK")
        self._positions_[7][0] = Rook("WHITE")
        self._positions_[7][7] = Rook("WHITE")

        # Peones (Pawns)
        for i in range(8):
            self._positions_[1][i] = Pawn("BLACK")
            self._positions_[6][i] = Pawn("WHITE")

        # Caballos (Knights)
        self._positions_[0][1] = Knight("BLACK")
        self._positions_[0][6] = Knight("BLACK")
        self._positions_[7][1] = Knight("WHITE")
        self._positions_[7][6] = Knight("WHITE")

        # Alfiles (Bishops)
        self._positions_[0][2] = Bishop("BLACK")
        self._positions_[0][5] = Bishop("BLACK")
        self._positions_[7][2] = Bishop("WHITE")
        self._positions_[7][5] = Bishop("WHITE")

        # Reyes y Reinas (Kings and Queens)
        self._positions_[0][3] = Queen("BLACK")
        self._positions_[7][3] = Queen("WHITE")
        self._positions_[0][4] = King("BLACK")
        self._positions_[7][4] = King("WHITE")

    def get_piece(self, row, col):
        # Obtiene la pieza en la posición especificada.
        
        return self._positions_[row][col]

    def get_board_state(self):
        # Retorna el estado actual del tablero en forma de matriz con representaciones de las piezas.
        board_repr = []
        for row in self._positions_:
            row_repr = [str(piece) if piece else '.' for piece in row]
            board_repr.append(row_repr)
        return board_repr

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        # Verifica si el movimiento desde una posición a otra es válido.
        piece = self.get_piece(from_row, from_col)
        if not piece:
            return False

        posibles_movimientos = piece.possible_moves(from_row, from_col)
        return (to_row, to_col) in posibles_movimientos

    def move_piece(self, from_row, from_col, to_row, to_col):
        # Mueve una pieza en el tablero si las reglas del juego lo permiten.
        piece = self.get_piece(from_row, from_col)
        target_piece = self.get_piece(to_row, to_col)

        if not piece:
            raise ValueError("No hay ninguna pieza en la posición de origen")

        if target_piece and piece.get_color() == target_piece.get_color():
            raise NonCaptureOwnPieceError("No puedes capturar tus propias piezas")

        if not self._ruta_despejada(from_row, from_col, to_row, to_col):
            raise NonPassOverPieceError("No puedes saltar sobre otras piezas")

        if isinstance(piece, Pawn):
            if not self._es_movimiento_valido_peon(from_row, from_col, to_row, to_col, target_piece):
                raise NonCaptureForwardError("Un peón no puede capturar hacia adelante")

        self._realizar_movimiento(from_row, from_col, to_row, to_col)
        self._verificar_fin_partida()

    def _es_movimiento_valido_peon(self, from_row, from_col, to_row, to_col, target_piece):
        # Valida las reglas específicas para el movimiento de un peón.
        direccion = 1 if self._positions_[from_row][from_col].get_color() == 'BLACK' else -1
        return not (to_row == from_row + direccion and target_piece is not None and from_col == to_col)

    def _ruta_despejada(self, from_row, from_col, to_row, to_col):
        # Verifica si hay piezas entre el punto de origen y destino.
        if isinstance(self._positions_[from_row][from_col], Knight):
            return True  # El caballo puede saltar sobre otras piezas.

        fila_paso = 1 if to_row > from_row else -1 if to_row < from_row else 0
        columna_paso = 1 if to_col > from_col else -1 if to_col < from_col else 0

        fila_actual, columna_actual = from_row + fila_paso, from_col + columna_paso
        while fila_actual != to_row or columna_actual != to_col:
            if self._positions_[fila_actual][columna_actual]:
                return False
            fila_actual += fila_paso
            columna_actual += columna_paso
        return True

    def _realizar_movimiento(self, from_row, from_col, to_row, to_col):
        # Realiza el movimiento de una pieza en el tablero.
        self._positions_[to_row][to_col] = self._positions_[from_row][from_col]
        self._positions_[from_row][from_col] = None

    def _verificar_fin_partida(self):
        # Verifica si el juego ha terminado (cuando todas las piezas de un color han sido eliminadas).
        piezas_blancas, piezas_negras = 0, 0

        for fila in self._positions_:
            for pieza in fila:
                if pieza:
                    if pieza.get_color() == 'WHITE':
                        piezas_blancas += 1
                    elif pieza.get_color() == 'BLACK':
                        piezas_negras += 1

        if piezas_negras == 0:
            raise GameOverException("White wins")
        elif piezas_blancas == 0:
            raise GameOverException("Black wins")
