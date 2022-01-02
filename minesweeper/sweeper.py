from typing import List, Set, Tuple

from minesweeper.cell import Cell


class MineSweeper:
    def __init__(self, width: int, height: int) -> None:
        self.__cells = [
            [Cell() for _ in range(height)]
            for __ in range(width)]

    @property
    def width(self) -> int:
        return len(self.__cells)

    @property
    def height(self) -> int:
        return len(self.__cells[0])

    def __is_inside_grid(self, i: int, j: int) -> bool:
        return 0 <= i < self.width and 0 <= j < self.height

    @property
    def __flat_cells(self) -> List[Cell]:
        return [self.__cells[i][j]
                for i in range(self.width)
                for j in range(self.height)]

    @property
    def num_hidden_cells(self) -> int:
        return len([1 for c in self.__flat_cells if c.is_hidden])

    @property
    def num_bombs(self) -> int:
        return len([1 for c in self.__flat_cells if c.is_bomb])

    def click_cell(self, i: int, j: int):
        if not self.__is_inside_grid(i, j):
            raise IndexError('Cannot click outside of grid')
        self.__cells[i][j].click()

    def place_bombs(self, bombs: Set[Tuple[int, int]]) -> None:
        if self.num_bombs > 0:
            raise OverflowError('Can only place bombs once')
        for i, j in bombs:
            if not self.__is_inside_grid(i, j):
                raise IndexError('Cannot place bomb outside of grid')
            self.__cells[i][j].set_as_bomb()
