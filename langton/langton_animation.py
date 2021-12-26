from tkinter import Canvas
from langton import Langton, Color, Direction
from utils import run_animation, Grid


class LangtonAnimator:
    def __init__(self, num_colors: int) -> None:
        self.__grid = Grid(50, 40)  # 50 x 40 cells
        self.__langton = self.__setup_initial_state(num_colors)

    @property
    def width(self) -> int:
        return self.__grid.width

    @property
    def height(self) -> int:
        return self.__grid.height

    def __setup_initial_state(self, num_colors: int) -> Langton:
        if num_colors < 2 or num_colors > 3:
            raise ValueError('num_colors must be 2 or 3')
        if num_colors == 2:
            return Langton()
        return Langton(num_colors=3, tiles={
            Color.BLACK: {(0, 0), (5, 0), (-5, 0), (0, 15)},
            Color.RED: {(0, 5), (0, -5)}
        })

    def draw_world(self, canvas: Canvas):
        self.__draw_tiles(canvas)
        self.__draw_ant(canvas)
        self.__langton.tick()

    def __draw_tiles(self, canvas: Canvas):
        for color, color_name in [(Color.BLACK, 'black'), (Color.RED, 'red')]:
            tiles = self.__langton.tiles(color)
            for t in tiles:
                rect_coordinates = self.__grid.get_rectangle_coordinates(*t)
                canvas.create_rectangle(
                    *rect_coordinates, fill=color_name, outline='grey')

    def __draw_ant(self, canvas: Canvas):
        body_size = (self.__grid.tile_size * 3) // 5
        head_size = body_size // 2
        x, y = self.__langton.ant_position
        x0, y0, *_ = self.__grid.get_rectangle_coordinates(x, y)
        x0_body = x0 + (self.__grid.tile_size - body_size) // 2
        y0_body = y0 + (self.__grid.tile_size - body_size) // 2
        x0_head = x0 + (self.__grid.tile_size - head_size) // 2
        y0_head = y0 + (self.__grid.tile_size - head_size) // 2
        dir_offset = body_size // 3
        if self.__langton.ant_direction == Direction.EAST:
            x0_body -= dir_offset
            x0_head += dir_offset
        elif self.__langton.ant_direction == Direction.WEST:
            x0_body += dir_offset
            x0_head -= dir_offset
        elif self.__langton.ant_direction == Direction.NORTH:
            y0_body += dir_offset
            y0_head -= dir_offset
        elif self.__langton.ant_direction == Direction.SOUTH:
            y0_body -= dir_offset
            y0_head += dir_offset

        x1_body = x0_body + body_size
        y1_body = y0_body + body_size

        x1_head = x0_head + head_size
        y1_head = y0_head + head_size

        canvas.create_oval(x0_body, y0_body, x1_body, y1_body,
                           fill='blue', outline='black')
        canvas.create_oval(x0_head, y0_head, x1_head, y1_head,
                           fill='blue', outline='black')


def run_langton_animation(num_colors: int = 3, num_iterations: int = 10000, frame_ms=100):
    langton_animator = LangtonAnimator(num_colors)
    run_animation(langton_animator.draw_world, langton_animator.width,
                  langton_animator.height, num_iterations, frame_ms)
