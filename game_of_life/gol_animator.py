from tkinter import Canvas

from utils import Grid, run_animation

from game_of_life import World


class _GameOfLifeAnimator:
    def __init__(self) -> None:
        self.__grid = Grid(100, 100, tile_size_in_pixels=5)  # 50 x 40 cells
        self.__world = self.__setup_initial_state()

    @property
    def width(self) -> int:
        return self.__grid.width

    @property
    def height(self) -> int:
        return self.__grid.height

    def __setup_initial_state(self) -> World:
        cells_left = {
            (0, 0), (0, 1), (0, 2), (1, 1), (2, 1), (3, 0), (3, 2)
        }
        cells_right = {(7 - x, y) for (x, y) in cells_left}
        return World(cells_left.union(cells_right))

    def draw_world(self, canvas: Canvas):
        self.__draw_tiles(canvas)
        self.__world = self.__world.next_generation()

    def __draw_tiles(self, canvas: Canvas):
        for c in self.__world.live_cells:
            rc = self.__grid.get_rectangle_coordinates(*c)
            canvas.create_rectangle(*rc, fill='black', outline='grey')


def run_game_of_life_animation(num_iterations: int = 10000, frame_ms=100):
    animator = _GameOfLifeAnimator()
    run_animation(animator.draw_world, animator.width,
                  animator.height, num_iterations, frame_ms)
