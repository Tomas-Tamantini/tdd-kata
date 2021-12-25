from enum import Enum, auto


class Direction(Enum):
    EAST = auto()
    NORTH = auto()
    WEST = auto()
    SOUTH = auto()

    def get_next(current_direction: 'Direction', turn_right: bool) -> 'Direction':
        dirs = [Direction.EAST, Direction.NORTH,
                Direction.WEST, Direction.SOUTH]
        current_index = dirs.index(current_direction)
        offset = -1 if turn_right else 1
        new_index = (current_index + offset) % len(dirs)
        return dirs[new_index]
