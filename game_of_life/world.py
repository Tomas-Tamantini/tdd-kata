from typing import Optional, Set, Tuple


class World:

    def __init__(self, live_cells: Optional[Set[Tuple[int, int]]] = None):
        self.__live_cells = live_cells or set()

    @property
    def num_live_cells(self) -> int:
        return len(self.__live_cells)
