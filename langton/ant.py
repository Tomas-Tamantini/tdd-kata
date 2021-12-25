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
