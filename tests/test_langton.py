from langton import Langton, Color


def test_ant_turns_white_tile_to_black():
    langton = Langton(ant=(0, 0))
    assert langton.get_color(0, 0) == Color.WHITE
    langton.tick()
    assert langton.get_color(0, 0) == Color.BLACK


def test_ant_turns_black_tile_to_white_when_two_colors():
    langton = Langton(ant=(0, 0), num_colors=2, tiles={Color.BLACK: {(0, 0)}})
    assert langton.get_color(0, 0) == Color.BLACK
    langton.tick()
    assert langton.get_color(0, 0) == Color.WHITE
