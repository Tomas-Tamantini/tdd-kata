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
    second_gen = get_next_gen({(1, 1), (1, 2)})
    assert second_gen.num_live_cells == 0


def test_death_by_overpopulation():
    second_gen = get_next_gen({(1, 1), (2, 2), (3, 3), (2, 1), (1, 3)})
    assert (2, 2) not in second_gen.live_cells


def test_cell_with_two_neighbors_survives():
    second_gen = get_next_gen({(1, 1), (2, 2), (2, 1)})
    assert (2, 2) in second_gen.live_cells


def test_cell_with_three_neighbors_survives():
    second_gen = get_next_gen({(1, 1), (2, 2), (2, 1), (1, 2)})
    assert (2, 2) in second_gen.live_cells


def test_dead_cell_with_three_neighbors_comes_to_life():
    second_gen = get_next_gen({(1, 1), (1, 2), (1, 3)})
    assert (2, 2) in second_gen.live_cells
