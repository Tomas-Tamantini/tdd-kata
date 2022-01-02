from typing import List, Optional, Set, Tuple

from minesweeper.cell import Cell


class MineSweeper:
    def __init__(self, height: int, width: int) -> None:
        self.__num_uncovered_cells = 0
        self.__game_is_over = False
        self.__cells = [
            [Cell() for _ in range(width)]
            for __ in range(height)]

    @property
    def game_is_over(self) -> bool:
        return self.__game_is_over

    @property
    def width(self) -> int:
        return len(self.__cells[0])

    @property
    def height(self) -> int:
        return len(self.__cells)

    @property
    def num_neighboring_mines(self) -> List[List[Optional[int]]]:
        def get_num_neighbors(cell: Cell) -> Optional[int]:
            if cell.is_mine or cell.is_hidden:
                return None
            return cell.num_neighboring_mines
        return [[get_num_neighbors(cell) for cell in row] for row in self.__cells]

    def __is_inside_grid(self, i: int, j: int) -> bool:
        return 0 <= i < self.height and 0 <= j < self.width

    @property
    def __flat_cells(self) -> List[Cell]:
        return [self.__cells[i][j]
                for i in range(self.height)
                for j in range(self.width)]

    @property
    def num_hidden_cells(self) -> int:
        return len([1 for c in self.__flat_cells if c.is_hidden])

    @property
    def num_mines(self) -> int:
        return len([1 for c in self.__flat_cells if c.is_mine])

    def click_cell(self, i: int, j: int):
        if self.__game_is_over:
            raise ValueError('Game is over')
        if not self.__is_inside_grid(i, j):
            raise IndexError('Cannot click outside of grid')
        self.__cells[i][j].click()
        if self.__cells[i][j].is_mine:
            self.__game_is_over = True
        else:
            self.__num_uncovered_cells += 1
            if self.__num_uncovered_cells + self.num_mines >= self.width * self.height:
                self.__game_is_over = True

    def __neighbors(self, i: int, j: int) -> List[Cell]:
        out = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                if self.__is_inside_grid(i + di, j + dj):
                    out.append(self.__cells[i + di][j + dj])
        return out

    def place_mines(self, mines: Set[Tuple[int, int]]) -> None:
        if self.num_mines > 0:
            raise OverflowError('Can only place mines once')
        for i, j in mines:
            if not self.__is_inside_grid(i, j):
                raise IndexError('Cannot place mine outside of grid')
            self.__cells[i][j].set_as_mine()
            for c in self.__neighbors(i, j):
                c.increment_num_neighboring_mines()
