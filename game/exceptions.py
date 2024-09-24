# Exceptions
class InvalidMove(Exception):
    message = "Invalid piece movement"
    def _str_(self):
        return self.message

class OutOfBoundsError(InvalidMove):
    message = "Row and column values must be between 0 and 7."

class NonNumericInputError(InvalidMove):
    message = "You must enter numeric values between 0 and 7."

class WrongTurnError(InvalidMove):
    message = "It is not the turn of the selected piece."

class InvalidPieceMoveError(InvalidMove):
    message = "Invalid move for the selected piece."

class NonPieceOriginError(InvalidMove):
    message = "There is no piece at the origin position."

class NonCaptureOwnPieceError(InvalidMove):
    message = "You cannot capture your own pieces."

class NonPassOverPieceError(InvalidMove):
    message = "You cannot pass over other pieces."

class NonCaptureForwardError(InvalidMove):
    message = "You cannot capture forward."

class GameOverException(Exception):
    def _init_(self, message):
        self._message_ = message
        super()._init_(message)