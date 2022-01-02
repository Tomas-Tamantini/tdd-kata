class Cell:
    def __init__(self) -> None:
        self.__is_hidden = True
        self.__is_bomb = False

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
