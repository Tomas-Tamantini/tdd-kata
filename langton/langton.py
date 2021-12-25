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

    def tick(self) -> None:
        p = self.__ant.position
        current_color = self.get_color(*p)
        next_color = Color.get_next(current_color, self.__num_colors)

        if current_color in self.__tiles:
            self.__tiles[current_color].remove(p)
        if next_color in self.__tiles:
            self.__tiles[next_color].add(p)

    def get_color(self, x: int, y: int) -> Color:
        for c in Color:
            if (x, y) in self.__tiles.get(c, set()):
                return c
        return Color.WHITE
