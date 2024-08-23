from game.chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)
        if game_over(chess):
            break

def play(chess):
    try:
        print(chess.show_board())  # Mostrar el tablero
        print("Turn: ", "White" if chess.turn == "WHITE" else "Black")

        from_row, from_col = get_input("From")
        to_row, to_col = get_input("To")

        chess.move(from_row, from_col, to_row, to_col)
    except Exception as e:
        print("Error:", e)

def get_input(prompt):
    while True:
        try:
            row = int(input(f"{prompt} row (0-7): "))
            col = int(input(f"{prompt} col (0-7): "))
            if row not in range(8) or col not in range(8):
                raise ValueError("Input out of bounds. Please enter a number between 0 and 7.")
            return row, col
        except ValueError as e:
            print(e)

def game_over(chess):
    if all_pieces_captured("WHITE", chess):
        print("All White pieces captured! Black wins!")
        return True
    elif all_pieces_captured("BLACK", chess):
        print("All Black pieces captured! White wins!")
        return True
    return False

def all_pieces_captured(color, chess):
    for row in range(8):
        for col in range(8):
            piece = chess.get_piece(row, col)
            if piece is not None and piece.color == color:
                return False
    return True

if __name__ == '__main__':
    main()
