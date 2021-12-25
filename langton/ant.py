from typing import Tuple


class Ant:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__x = x
        self.__y = y

    @property
    def position(self) -> Tuple[int, int]:
        return (self.__x, self.__y)
