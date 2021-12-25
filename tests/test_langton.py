from langton import Langton


def test_ant_turns_white_tile_to_black():
    first_gen = Langton(ant=(0, 0))
    second_gen = first_gen.next_generation()
    assert (0, 0) in second_gen.black_tiles
