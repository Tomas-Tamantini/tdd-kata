from typing import Optional, Set, Tuple


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
        num_neighbors_dead_cells = dict()
        for coords in self.__live_cells:
            num_alive_neighbors = 0
            for n in _neighboring_coordinates(*coords):
                if n in self.__live_cells:
                    num_alive_neighbors += 1
                elif n not in num_neighbors_dead_cells:
                    num_neighbors_dead_cells[n] = 1
                else:
                    num_neighbors_dead_cells[n] += 1
            if 2 <= num_alive_neighbors <= 3:
                next_gen.add(coords)
        for cell_coord, num_neighbors in num_neighbors_dead_cells.items():
            if num_neighbors == 3:
                next_gen.add(cell_coord)
        return World(next_gen)


def _neighboring_coordinates(x, y) -> Set[Tuple[int, int]]:
    return {(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)
            if not (dx == 0 and dy == 0)}
