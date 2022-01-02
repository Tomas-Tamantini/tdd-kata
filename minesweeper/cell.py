class Cell:
    def __init__(self) -> None:
        self.__is_hidden = True
        self.__is_bomb = False
        self.__num_neighboring_bombs = 0

    @property
    def is_hidden(self) -> bool:
        return self.__is_hidden

    @property
    def is_bomb(self) -> bool:
        return self.__is_bomb

    def set_as_bomb(self) -> None:
        self.__is_bomb = True

    def click(self):
        self.__is_hidden = False

    @property
    def num_neighboring_bombs(self) -> int:
        return self.__num_neighboring_bombs

    def increment_num_neighboring_bombs(self) -> None:
        self.__num_neighboring_bombs += 1
