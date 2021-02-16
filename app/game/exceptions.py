class GameNotFoundError(RuntimeError):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class WrongTurnError(RuntimeError):
    def __init__(self, arg):
        super().__init__(arg)
        self.arg = arg