"""See game rules and kata specification at: https://codingdojo.org/kata/LangtonAnt/"""
from typing import Optional, Set, Tuple, Dict

from langton.colors import Color
from langton.ant import Ant
from langton.directions import Direction


class Langton:
    def __init__(self, ant: Ant = None, num_colors: int = 2, tiles: Optional[Dict[Color, Set[Tuple[int, int]]]] = None):
        if num_colors < 2 or num_colors > 3:
            raise ValueError("Invalid number of colors")
        self.__num_colors = num_colors
        self.__ant = Ant() if ant is None else ant
        self.__tiles = dict()
        for c in Color:
            if c == Color.WHITE:
                continue
            self.__tiles[c] = set() if tiles is None else tiles.get(c, set())

    @property
    def ant_direction(self) -> Direction:
        return self.__ant.direction

    @property
    def ant_position(self) -> Tuple[int, int]:
        return self.__ant.position

    def tick(self) -> None:
        current_color = self.get_color(*self.__ant.position)
        self.__cycle_color(current_color)
        if current_color == Color.WHITE:
            self.__ant.turn(right=True)
        elif current_color == Color.BLACK:
            self.__ant.turn(right=False)
        self.__ant.move_forward()

    def __cycle_color(self, current_color):
        next_color = Color.get_next(current_color, self.__num_colors)
        if current_color in self.__tiles:
            self.__tiles[current_color].remove(self.__ant.position)
        if next_color in self.__tiles:
            self.__tiles[next_color].add(self.__ant.position)

    def get_color(self, x: int, y: int) -> Color:
        for c in Color:
            if (x, y) in self.__tiles.get(c, set()):
                return c
        return Color.WHITE

    def tiles(self, color: Color = Color.BLACK) -> Set[Tuple[int, int]]:
        if color == Color.WHITE:
            raise ValueError("White tiles are not stored")
        return self.__tiles.get(color, set())
