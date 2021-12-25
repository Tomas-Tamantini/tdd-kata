from enum import Enum, auto


class Color(Enum):
    WHITE = auto()
    BLACK = auto()
    RED = auto()

    def get_next(current_color: 'Color', cycle_size: int) -> 'Color':
        if current_color == Color.WHITE:
            return Color.BLACK
        if current_color == Color.RED:
            return Color.WHITE
        return Color.RED if cycle_size == 3 else Color.WHITE
