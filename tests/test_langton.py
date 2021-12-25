from langton import Langton, Color


def test_ant_turns_white_tile_to_black():
    langton = Langton(ant=(0, 0))
    assert (0, 0) not in langton.tiles(Color.BLACK)
    langton.tick()
    assert (0, 0) in langton.tiles(Color.BLACK)
