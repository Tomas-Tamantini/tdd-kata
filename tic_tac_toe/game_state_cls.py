from dataclasses import dataclass
from typing import Tuple, List, Optional


class _TicTacToeGrid:
    @staticmethod
    def get_positions_score(positions: List[Tuple[int, int]], reflection: bool, rotation: int) -> int:
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
    def __init__(self, naughts: Optional[List[Tuple[int, int]]] = None,
                 crosses: Optional[List[Tuple[int, int]]] = None, is_cross_turn: bool = True):
        self.__naughts = naughts if naughts else []
        self.__crosses = crosses if crosses else []
        self.__index = self.__get_index()
        self.__is_cross_turn = is_cross_turn

    @property
    def num_empty_cells(self) -> int:
        return 9 - len(self.__naughts) - len(self.__crosses)

    def __hash__(self):
        return self.__index

    def __eq__(self, other: "TicTacToe"):
        return self.__index == other.__index

    def play(self, row, col):
        naughts = self.__naughts.copy()
        crosses = self.__crosses.copy()
        if self.__is_cross_turn:
            crosses.append((row, col))
        else:
            naughts.append((row, col))
        return TicTacToe(naughts, crosses, not self.__is_cross_turn)

    def __get_index(self):
        max_score = 0
        for reflection in (False, True):
            for rotation in (0, 90, 180, 270):
                score = _TicTacToeGrid.get_positions_score(self.__naughts, reflection, rotation) + \
                        2 * _TicTacToeGrid.get_positions_score(self.__crosses, reflection, rotation)
                if score > max_score:
                    max_score = score
        return max_score
