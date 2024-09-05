from piece import Piece

class Knight(Piece):
    def __init__(self, color, board):
        super().__init__(color)
        self.__board__ = board

    def basic_knight_moves(self, row, col):
        # Movimientos en L del caballo
        possible_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        # Filtrar movimientos fuera del tablero
        moves = [(row + dr, col + dc) for dr, dc in possible_moves
                 if 0 <= row + dr < 8 and 0 <= col + dc < 8]
        return moves

    def possible_positions(self, row, col):
        valid_positions = []
        moves = self.basic_knight_moves(row, col)
        
        for move in moves:
            r, c = move
            piece_at_destination = self.__board__.get_piece(r, c)
            if piece_at_destination is None:
                valid_positions.append(move)  # Casilla vacía
            elif piece_at_destination.color != self.color:
                valid_positions.append(move)  # Captura posible
            # El caballo puede saltar, no necesita detenerse ante piezas en el camino
        return valid_positions

    withe_str = "♘"
    black_str = "♞"

    def __str__(self):
        return self.withe_str if self.color == "WHITE" else self.black_str
