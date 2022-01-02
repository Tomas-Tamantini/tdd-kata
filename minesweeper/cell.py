class Cell:
    def __init__(self) -> None:
        self.__is_hidden = True
        self.__is_mine = False
        self.__num_neighboring_mines = 0

    @property
    def is_hidden(self) -> bool:
        return self.__is_hidden

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    def set_as_mine(self) -> None:
        self.__is_mine = True

    def click(self):
        self.__is_hidden = False

    @property
    def num_neighboring_mines(self) -> int:
        return self.__num_neighboring_mines

    def increment_num_neighboring_mines(self) -> None:
        self.__num_neighboring_mines += 1

    def __str__(self) -> str:
        if self.__is_hidden:
            return '*'
        if self.__is_mine:
            return 'M'
        return str(self.__num_neighboring_mines)
