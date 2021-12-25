from typing import Tuple
from langton.directions import Direction


class Ant:
    def __init__(self, x: int = 0, y: int = 0, direction: Direction = Direction.EAST) -> None:
        self.__x = x
        self.__y = y
        self.__direction = direction

    @property
    def position(self) -> Tuple[int, int]:
        return (self.__x, self.__y)

    @property
    def direction(self) -> Direction:
        return self.__direction

    def turn(self, right: bool):
        self.__direction = Direction.get_next(self.__direction, right)

    def move_forward(self):
        if self.__direction == Direction.EAST:
            self.__x += 1
        elif self.__direction == Direction.NORTH:
            self.__y += 1
        elif self.__direction == Direction.WEST:
            self.__x -= 1
        elif self.__direction == Direction.SOUTH:
            self.__y -= 1
