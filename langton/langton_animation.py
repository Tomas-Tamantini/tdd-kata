from tkinter import *
from langton import Langton, Color, Direction
from utils import run_animation

WIDTH = 500
HEIGHT = 500
TILE_SIZE = 12


def _setup_initial_grid(num_colors: int) -> Langton:
    if num_colors == 2:
        return Langton()
    elif num_colors == 3:
        return Langton(num_colors=3, tiles={
            Color.BLACK: {(0, 0), (5, 0), (-5, 0), (0, 15)},
            Color.RED: {(0, 5), (0, -5)}
        })
    raise ValueError('num_colors must be 2 or 3')


def run_langton_animation(num_colors: int = 3, num_iterations: int = 10000, frame_ms=100):
    langton = _setup_initial_grid(num_colors)

    def callback_on_frame(canvas: Canvas):
        _draw_world(canvas, langton)
        langton.tick()
    run_animation(callback_on_frame, WIDTH, HEIGHT, num_iterations, frame_ms)


def _draw_world(canvas: Canvas, langton: Langton):
    _draw_tiles(canvas, langton)
    _draw_ant(canvas, langton)


def _draw_tiles(canvas: Canvas, langton: Langton):
    for color, color_name in [(Color.BLACK, 'black'), (Color.RED, 'red')]:
        tiles = langton.tiles(color)
        for x, y in tiles:
            x0 = x * TILE_SIZE + WIDTH // 2
            y0 = -y * TILE_SIZE + HEIGHT // 2
            x1 = x0 + TILE_SIZE
            y1 = y0 + TILE_SIZE
            canvas.create_rectangle(
                x0, y0, x1, y1, fill=color_name, outline='grey')


def _draw_ant(canvas: Canvas, langton: Langton):
    body_size = (TILE_SIZE * 3) // 5
    head_size = body_size // 2
    x, y = langton.ant_position
    x0_body = x * TILE_SIZE + (WIDTH + TILE_SIZE - body_size) // 2
    y0_body = -y * TILE_SIZE + (HEIGHT + TILE_SIZE - body_size) // 2
    x0_head = x * TILE_SIZE + (WIDTH + TILE_SIZE - head_size) // 2
    y0_head = -y * TILE_SIZE + (HEIGHT + TILE_SIZE - head_size) // 2
    dir_offset = body_size // 3
    if langton.ant_direction == Direction.EAST:
        x0_body -= dir_offset
        x0_head += dir_offset
    elif langton.ant_direction == Direction.WEST:
        x0_body += dir_offset
        x0_head -= dir_offset
    elif langton.ant_direction == Direction.NORTH:
        y0_body += dir_offset
        y0_head -= dir_offset
    elif langton.ant_direction == Direction.SOUTH:
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
