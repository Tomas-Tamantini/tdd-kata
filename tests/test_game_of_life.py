from game_of_life import World


def test_default_world_is_empty():
    world = World()
    assert world.num_live_cells == 0
