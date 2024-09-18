from game.chess import Chess
from exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)
        if check_game_over(chess):
            break

def play(chess):
    try:
        print(chess.show_board())  # Mostrar el tablero
        print("Turn: ", "White" if chess.turn == "WHITE" else "Black")

        # Mostrar movimientos válidos para la pieza seleccionada (opcional)
        from_row = get_input("From row: ")
        from_col = get_input("From col: ")

        show_valid_moves(chess, from_row, from_col)

        to_row = get_input("To row: ")
        to_col = get_input("To col: ")

        chess.move(from_row, from_col, to_row, to_col)
        
    except InvalidMove as e:
        print("Invalid Move:", e)
    except InvalidTurn as e:
        print("Invalid Turn:", e)
    except EmptyPosition as e:
        print("Empty Position:", e)
    except Exception as e:
        print("Error:", e)

def get_input(prompt):
    while True:
        try:
            val = int(input(f"{prompt} (0-7) or '9' to resign: "))
            if val == 9:
                return None  # Permite al jugador renunciar
            if val not in range(8):
                raise ValueError("Input out of bounds. Please enter a number between 0 and 7.")
            return val
        except ValueError as e:
            print(e)

def show_valid_moves(chess, from_row, from_col):
    piece = chess.board.get_piece(from_row, from_col)
    if piece and piece.color == chess.turn:
        valid_moves = piece.get_valid_moves(chess.board)
        print(f"Valid moves for {piece}: {valid_moves}")
    else:
        print("No valid moves or wrong piece selected.")

def check_game_over(chess):
    if chess.is_checkmate("WHITE"):
        print("Checkmate! Black wins!")
        return True
    elif chess.is_checkmate("BLACK"):
        print("Checkmate! White wins!")
        return True
    elif chess.is_stalemate("WHITE") or chess.is_stalemate("BLACK"):
        print("Stalemate! It's a draw!")
        return True
    return False

if __name__ == '__main__':
    main()
