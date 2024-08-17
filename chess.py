from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    
    
    def move(
        from_row,
        from_rol,
        to_row,
        to_col,
    ):
        ...
    self.change_turn()
def change_turn(self):    
    if self.__turn__ == "WHITE":
            self.__turn__ == "BLACK"
    else:
        self.turn__ = "WHITE"