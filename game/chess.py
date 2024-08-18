from game.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        if self.__board__.get_piece(from_row, from_col) == "No piece":
            message = "You can't move a piece that doesn't exist"
            print(message)
            return message

        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        self.change_turn()

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
