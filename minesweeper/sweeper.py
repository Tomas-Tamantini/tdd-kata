class MineSweeper:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height

    @property
    def num_hidden_cells(self) -> int:
        return self.__width * self.__height
