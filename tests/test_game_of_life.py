from typing import Optional, Set, Tuple

from game_of_life import World


def get_next_gen(live_cells: Optional[Set[Tuple[int, int]]] = None) -> World:
    world = World(live_cells)
    return world.next_generation()


def test_default_world_is_empty():
    world = World()
    assert world.num_live_cells == 0


def test_can_setup_world_with_live_cells():
    world = World({(1, 1), (2, 2)})
    assert world.num_live_cells == 2


def test_dead_world_stays_dead():
    second_gen = get_next_gen()
    assert second_gen.num_live_cells == 0


def test_death_by_underpopulation():
    second_gen = get_next_gen({(1, 1)})
    assert second_gen.num_live_cells == 0
