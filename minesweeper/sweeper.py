class _Cell:
    def __init__(self) -> None:
        self.__is_hidden = True

    @property
    def is_hidden(self) -> bool:
        return self.__is_hidden

    def click(self):
        self.__is_hidden = False


class MineSweeper:
    def __init__(self, width: int, height: int) -> None:
        self.__cells = [
            [_Cell() for _ in range(height)]
            for __ in range(width)]

    @property
    def width(self) -> int:
        return len(self.__cells)

    @property
    def height(self) -> int:
        return len(self.__cells[0])

    @property
    def num_hidden_cells(self) -> int:
        flat_cells = [self.__cells[i][j]
                      for i in range(self.width)
                      for j in range(self.height)]
        return len([1 for c in flat_cells if c.is_hidden])

    def click_cell(self, i: int, j: int):
        if i < 0 or i >= self.width or j < 0 or j >= self.height:
            raise ValueError('Cannot click outside of grid')
        self.__cells[i][j].click()
