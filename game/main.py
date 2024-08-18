from game.chess import Chess

def main():
    chess = Chess()
    continue_game = "y"

    try:
        while continue_game.lower() == "y":
            from_row = int(input("From row: "))
            from_col = int(input("From col: "))
            selected_piece = chess.__board__.get_piece(from_row, from_col)
            print(f"The piece you have chosen is: {selected_piece}")

            to_row = int(input("To row: "))
            to_col = int(input("To col: "))

            chess.move(from_row, from_col, to_row, to_col)

            print(f"The piece in the original position is now: {chess.__board__.get_piece(from_row, from_col)}")
            print(f"The piece in the new position is: {chess.__board__.get_piece(to_row, to_col)}")

            continue_game = input("Do you want to continue? (y/n): ")
            chess.change_turn()
            print(f"It's now {chess.__turn__}'s turn")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
