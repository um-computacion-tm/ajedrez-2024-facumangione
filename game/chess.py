from board import Board
from exceptions import NonPieceOriginError, WrongTurnError, InvalidPieceMoveError, GameOverException

class Chess:
    # Inicializa el juego de ajedrez
    def __init__(self):

        # Función constructora de la clase Chess.
        # Inicializar tablero
        self._tablero_ = Board()
        # Inicializar turno
        self._turno_actual_ = "WHITE"

    # Obtener el estado actual del tablero
    def obtener_tablero(self):
        # Devuelve el tablero del juego.
        return self._tablero_.get_board()

    # Método para mover una pieza    
    def realizar_movimiento(self, fila_origen, columna_origen, fila_destino, columna_destino):
       # Función que maneja el movimiento de una pieza en el tablero.
        try:
            # Obtener el color de la pieza en la posición de origen
            color_pieza = self._tablero_.get_piece_color(fila_origen, columna_origen)
            if color_pieza is None:
                raise NonPieceOriginError()
            
            # Verificar que la pieza sea del jugador con el turno actual
            if color_pieza != self._turno_actual_:
                raise WrongTurnError()
            
            # Verificar que el movimiento sea válido y realizarlo
            if not self._tablero_.es_movimiento_valido(fila_origen, columna_origen, fila_destino, columna_destino):
                raise InvalidPieceMoveError()
            
            self._tablero_.mover_pieza(fila_origen, columna_origen, fila_destino, columna_destino)
            
            # Cambiar el turno después de mover
            self.cambiar_turno()    

        except GameOverException as e:
            raise e    

    # Obtener el turno actual
    @property
    def turno(self):
        # Retorna el turno del jugador actual.
        return self._turno_actual_

    # Método para alternar el turno entre jugadores
    def cambiar_turno(self):
        # Cambia el turno del jugador.
        if self._turno_actual_ == "WHITE":
            self._turno_actual_ = "BLACK"
        else:
            self._turno_actual_ = "WHITE"
