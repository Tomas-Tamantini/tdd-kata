from tkinter import *
from langton import Langton, Color, Direction

WIDTH = 500
HEIGHT = 500
TILE_SIZE = 20


def run_langton_animation(num_iterations: int = 10000):
    root = Tk()
    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    langton = Langton(num_colors=2)
    for _ in range(num_iterations):
        canvas.delete('all')
        _draw_world(canvas, langton)
        canvas.pack()
        root.update()
        root.after(1000)
        langton.tick()
    root.mainloop()


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
    if langton.ant_direction == Direction.EAST:
        x0_body -= body_size // 3
        x0_head += body_size // 3
    elif langton.ant_direction == Direction.WEST:
        x0_body += body_size // 3
        x0_head -= body_size // 3
    elif langton.ant_direction == Direction.NORTH:
        y0_body += body_size // 3
        y0_head -= body_size // 3
    elif langton.ant_direction == Direction.SOUTH:
        y0_body -= body_size // 3
        y0_head += body_size // 3

    x1_body = x0_body + body_size
    y1_body = y0_body + body_size

    x1_head = x0_head + head_size
    y1_head = y0_head + head_size

    canvas.create_oval(x0_body, y0_body, x1_body, y1_body,
                       fill='blue', outline='black')
    canvas.create_oval(x0_head, y0_head, x1_head, y1_head,
                       fill='blue', outline='black')
