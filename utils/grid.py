from typing import Tuple


class Grid:
    def __init__(self, num_cells_horizontal: int = 40, num_cells_vertical: int = 30, tile_size_in_pixels: int = 15) -> None:
        self.__cells_hor = num_cells_horizontal
        self.__cells_ver = num_cells_vertical
        self.__tile_size = tile_size_in_pixels

    @property
    def tile_size(self) -> int:
        return self.__tile_size

    @property
    def width(self):
        return self.__cells_hor * self.__tile_size

    @property
    def height(self):
        return self.__cells_ver * self.__tile_size

    def get_rectangle_coordinates(self, x: int, y: int) -> Tuple[int, int, int, int]:
        x0 = x * self.__tile_size + self.width // 2
        y0 = -y * self.__tile_size + self.height // 2
        x1 = x0 + self.__tile_size
        y1 = y0 + self.__tile_size
        return x0, y0, x1, y1
