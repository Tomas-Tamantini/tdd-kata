"""See game rules and kata specification at: https://codingdojo.org/kata/LangtonAnt/"""
from typing import Optional, Set, Tuple, Dict

from langton.colors import Color


class Langton:
    def __init__(self, ant: Tuple[int, int] = (0, 0), num_colors: int = 2, tiles: Optional[Dict[Color, Set[Tuple[int, int]]]] = None):
        self.__ant = ant
        self.__tiles = {c: set() for c in Color if c !=
                        Color.WHITE} if tiles is None else tiles

    def tick(self) -> None:
        colors = [Color.WHITE, Color.BLACK]
        for i, c in enumerate(colors):
            if c not in self.__tiles or self.__ant not in self.__tiles[c]:
                continue
            self.__tiles[c].remove(self.__ant)
            next_color = colors[(i + 1) % len(colors)]
            if next_color != Color.WHITE:
                self.__tiles[next_color].add(self.__ant)
            return
        self.__tiles[Color.BLACK].add(self.__ant)

    def get_color(self, x: int, y: int) -> Color:
        for c in Color:
            if (x, y) in self.__tiles.get(c, set()):
                return c
        return Color.WHITE
