from langton import Langton, Color, Direction


def test_ant_turns_white_tile_to_black():
    langton = Langton()
    assert langton.get_color(0, 0) == Color.WHITE
    langton.tick()
    assert langton.get_color(0, 0) == Color.BLACK


def test_ant_turns_black_tile_to_white_when_two_colors():
    langton = Langton(tiles={Color.BLACK: {(0, 0)}})
    assert langton.get_color(0, 0) == Color.BLACK
    langton.tick()
    assert langton.get_color(0, 0) == Color.WHITE


def test_ant_turns_black_tile_to_red_when_three_colors():
    langton = Langton(num_colors=3, tiles={Color.BLACK: {(0, 0)}})
    assert langton.get_color(0, 0) == Color.BLACK
    langton.tick()
    assert langton.get_color(0, 0) == Color.RED


def test_ant_turns_red_tile_to_white():
    langton = Langton(num_colors=3, tiles={Color.RED: {(0, 0)}})
    assert langton.get_color(0, 0) == Color.RED
    langton.tick()
    assert langton.get_color(0, 0) == Color.WHITE


def test_ant_turns_right_on_white_tile():
    langton = Langton()
    assert langton.ant_direction == Direction.EAST
    langton.tick()
    assert langton.ant_direction == Direction.SOUTH


def test_ant_turns_left_on_black_tile():
    langton = Langton(tiles={Color.BLACK: {(0, 0)}})
    assert langton.ant_direction == Direction.EAST
    langton.tick()
    assert langton.ant_direction == Direction.NORTH


def test_ant_does_not_turn_on_red_tile():
    langton = Langton(num_colors=3, tiles={Color.RED: {(0, 0)}})
    assert langton.ant_direction == Direction.EAST
    langton.tick()
    assert langton.ant_direction == Direction.EAST
