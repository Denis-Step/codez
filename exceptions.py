class GameNotFoundError(RuntimeError):
    def __init__(self, arg):
        super().__init__(arg)
        self.args = arg


class WrongTurnError(RuntimeError):
    def __init__(self, arg):
        super().__init__(arg)
        self.args = arg