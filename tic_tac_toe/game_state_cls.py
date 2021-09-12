from dataclasses import dataclass
from typing import Tuple, List, Optional, Set


def _winning_configurations() -> List:
    rows = [{(row, col) for col in range(3)} for row in range(3)]
    cols = [{(row, col) for row in range(3)} for col in range(3)]
    down_diagonal = {(i, i) for i in range(3)}
    up_diagonal = {(2 - i, i) for i in range(3)}
    return rows + cols + [down_diagonal, up_diagonal]


class _TicTacToeGrid:
    @staticmethod
    def get_positions_score(positions: Set[Tuple[int, int]], reflection: bool, rotation: int) -> int:
        score = 0
        for i, j in positions:
            new_i, new_j = _TicTacToeGrid.__get_transformed_coordinates(i, j, reflection, rotation)
            power = 8 - 3 * new_i - new_j
            score += 3 ** power
        return score

    @staticmethod
    def __get_transformed_coordinates(i: int, j: int, reflection: bool, rotation: int) -> Tuple[int, int]:
        if rotation == 0:
            new_i = i
            new_j = j
        elif rotation == 90:
            new_i = 2 - j
            new_j = i
        elif rotation == 180:
            new_i = 2 - i
            new_j = 2 - j
        else:
            new_i = j
            new_j = 2 - i
        return (new_j, new_i) if reflection else (new_i, new_j)


@dataclass
class TicTacToe:
    __winning_configurations = _winning_configurations()

    def __init__(self, naughts: Optional[Set[Tuple[int, int]]] = None,
                 crosses: Optional[Set[Tuple[int, int]]] = None, is_cross_turn: bool = True):
        self.__naughts = naughts if naughts else set()
        self.__crosses = crosses if crosses else set()
        self.__index = self.__get_index()
        self.__is_cross_turn = is_cross_turn

    @property
    def num_empty_cells(self) -> int:
        return 9 - len(self.__naughts) - len(self.__crosses)

    @property
    def __empty_cells(self) -> List[Tuple[int, int]]:
        cells = []
        for i in range(3):
            for j in range(3):
                if (i, j) not in self.__naughts and (i, j) not in self.__crosses:
                    cells.append((i, j))
        return cells

    @property
    def is_over(self) -> bool:
        if self.num_empty_cells == 0:
            return True
        for winning_config in TicTacToe.__winning_configurations:
            if winning_config.issubset(self.__naughts) or winning_config.issubset(self.__crosses):
                return True

        return False

    def __hash__(self):
        return self.__index

    def __eq__(self, other: "TicTacToe"):
        return self.__index == other.__index

    def play(self, row: int, col: int) -> "TicTacToe":
        naughts = self.__naughts.copy()
        crosses = self.__crosses.copy()
        if self.__is_cross_turn:
            crosses.add((row, col))
        else:
            naughts.add((row, col))
        return TicTacToe(naughts, crosses, not self.__is_cross_turn)

    @property
    def children(self) -> Set["TicTacToe"]:
        if self.is_over:
            return set()
        c = set()
        for cell in self.__empty_cells:
            naughts = self.__naughts.copy()
            crosses = self.__crosses.copy()
            if self.__is_cross_turn:
                crosses.add(cell)
            else:
                naughts.add(cell)
            child = TicTacToe(naughts, crosses, not self.__is_cross_turn)

            c.add(child)
        return c

    def __get_index(self) -> int:
        max_score = 0
        for reflection in (False, True):
            for rotation in (0, 90, 180, 270):
                score = _TicTacToeGrid.get_positions_score(self.__naughts, reflection, rotation) + \
                        2 * _TicTacToeGrid.get_positions_score(self.__crosses, reflection, rotation)
                if score > max_score:
                    max_score = score
        return max_score

    def __str__(self):
        cells = [['*' for _ in range(3)] for _ in range(3)]
        for i, j in self.__crosses:
            cells[i][j] = 'X'
        for i, j in self.__naughts:
            cells[i][j] = 'O'
        return '\n'.join(''.join(cells[i][j] for j in range(3)) for i in range(3))
