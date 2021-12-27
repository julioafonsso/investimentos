from getch import getch


class GetChar:
    UP_KEY = 'UP_KEY'
    DOWN_KEY = 'DOWN_KEY'
    RIGHT_KEY = 'RIGHT_KEY'
    LEFT_KEY = 'LEFT_KEY'

    ARROW_FUNCTIONS = {
        'A': UP_KEY,
        'B': DOWN_KEY,
        'C': RIGHT_KEY,
        'D': LEFT_KEY
    }

    def __init__(self):
        self.valor = getch()
        if self.valor == '\x1b':
            self.valor = getch()
            self.valor = self.ARROW_FUNCTIONS[getch()]

    def is_up_key(self):
        return self.valor == self.UP_KEY

    def is_down_key(self):
        return self.valor == self.DOWN_KEY

    def is_right_key(self):
        return self.valor == self.RIGHT_KEY

    def is_left_key(self):
        return self.valor == self.LEFT_KEY

    def get_value(self):
        return self.valor
