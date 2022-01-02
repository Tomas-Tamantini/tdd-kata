from typing import List, Optional

import pytest
from minesweeper import MineSweeper


def test_grid_starts_with_all_hidden_cells():
    assert MineSweeper(width=10, height=8).num_hidden_cells == 80


@pytest.mark.parametrize('i, j', [(-1, 0), (0, -1), (8, 5), (5, 10)])
def test_cannot_show_cell_not_on_grid(i, j):
    sweeper = MineSweeper(height=8, width=10)
    with pytest.raises(IndexError):
        sweeper.click_cell(i, j)


def test_click_should_show_cell():
    sweeper = MineSweeper(10, 8)
    sweeper.click_cell(5, 5)
    assert sweeper.num_hidden_cells < 80


def test_cannot_place_mines_outside_grid():
    sweeper = MineSweeper(10, 8)
    with pytest.raises(IndexError):
        sweeper.place_mines({(5, 8)})


def test_can_place_mines_in_grid():
    sweeper = MineSweeper(10, 8)
    sweeper.place_mines({(5, 5), (3, 2)})
    assert sweeper.num_mines == 2


def test_can_only_place_mines_once():
    sweeper = MineSweeper(10, 8)
    sweeper.place_mines({(5, 5), (3, 2)})
    with pytest.raises(OverflowError):
        sweeper.place_mines({(0, 0)})


def get_3x4_game() -> MineSweeper:
    sweeper = MineSweeper(height=3, width=4)
    sweeper.place_mines({(0, 0), (2, 1), (2, 2)})
    return sweeper


def test_get_num_neighboring_mines():
    sweeper = get_3x4_game()
    expected_neighbors: List[List[Optional[int]]] = [
        [None for _ in range(4)] for _ in range(3)]
    assert sweeper.num_neighboring_mines == expected_neighbors
    sweeper.click_cell(1, 1)
    expected_neighbors[1][1] = 3
    assert sweeper.num_neighboring_mines == expected_neighbors


def test_game_is_over_when_stepping_on_a_mine():
    sweeper = get_3x4_game()
    assert not sweeper.game_is_over
    sweeper.click_cell(2, 1)
    assert sweeper.game_is_over


def test_game_is_over_when_only_mines_are_left():
    sweeper = get_3x4_game()
    non_mines = {
        (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 3)
    }
    for i, j in non_mines:
        sweeper.click_cell(i, j)
    assert sweeper.game_is_over


def test_game_clicks_safe_cells_automatically():
    sweeper = get_3x4_game()
    sweeper.click_cell(0, 3)
    # Since there are no neighboring mines,
    # all neighbors are clicked, and this is done recursively
    assert sweeper.num_hidden_cells == 6
    expected_neighbors = [
        [None, 1, 0, 0],
        [None, 3, 2, 1],
        [None, None, None, None]
    ]
    assert sweeper.num_neighboring_mines == expected_neighbors
