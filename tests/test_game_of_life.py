from game_of_life import World


def test_default_world_is_empty():
    world = World()
    assert world.num_live_cells == 0


def test_can_setup_world_with_live_cells():
    world = World({(1, 1), (2, 2)})
    assert world.num_live_cells == 2
