from typing import List, Optional, Set, Tuple


class World:

    def __init__(self, live_cells: Optional[Set[Tuple[int, int]]] = None):
        self.__live_cells = live_cells or set()

    @property
    def num_live_cells(self) -> int:
        return len(self.__live_cells)

    @property
    def live_cells(self) -> Set[Tuple[int, int]]:
        return self.__live_cells

    def next_generation(self) -> 'World':
        next_gen = set()
        for x, y in self.__live_cells:
            cell = Cell(x, y)
            for n in cell.neighbor_coordinates():
                if n in self.__live_cells:
                    cell.increment_num_live_neighbors()
            if 2 <= cell.num_live_neighbors <= 3:
                next_gen.add((x, y))
        return World(next_gen)


class Cell:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self.__num_live_neighbors = 0

    def increment_num_live_neighbors(self) -> None:
        self.__num_live_neighbors += 1

    @property
    def num_live_neighbors(self) -> int:
        return self.__num_live_neighbors

    def neighbor_coordinates(self) -> List[Tuple[int, int]]:
        coords = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                coords.append((self.__x + dx, self.__y + dy))
        return coords
