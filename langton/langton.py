"""See game rules and kata specification at: https://codingdojo.org/kata/LangtonAnt/"""
from typing import Optional, Set, Tuple, Dict

from langton.colors import Color


class Langton:
    def __init__(self, ant: Tuple[int, int] = (0, 0), tiles: Optional[Dict[Color, Set[Tuple[int, int]]]] = None):
        self.__ant = ant
        self.__tiles = {c: set() for c in Color} if tiles is None else tiles

    def tick(self) -> None:
        self.__tiles[Color.BLACK].add(self.__ant)

    def tiles(self, color: Color) -> Set[Tuple[int, int]]:
        return self.__tiles.get(color, set())
