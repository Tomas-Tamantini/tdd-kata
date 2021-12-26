from tkinter import Tk, Canvas
from typing import Callable


def run_animation(callback_on_frame: Callable[[Canvas], None], width: int = 500, height: int = 500, num_frames: int = 10000, frame_duration_ms=100):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    for _ in range(num_frames):
        canvas.delete('all')
        callback_on_frame(canvas)
        canvas.pack()
        root.update()
        root.after(frame_duration_ms)
    root.mainloop()
