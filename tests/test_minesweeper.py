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


def test_cannot_place_bombs_outside_grid():
    sweeper = MineSweeper(10, 8)
    with pytest.raises(IndexError):
        sweeper.place_bombs({(5, 8)})


def test_can_place_bombs_in_grid():
    sweeper = MineSweeper(10, 8)
    sweeper.place_bombs({(5, 5), (3, 2)})
    assert sweeper.num_bombs == 2


def test_can_only_place_bombs_once():
    sweeper = MineSweeper(10, 8)
    sweeper.place_bombs({(5, 5), (3, 2)})
    with pytest.raises(OverflowError):
        sweeper.place_bombs({(0, 0)})


def test_get_num_neighboring_bombs():
    sweeper = MineSweeper(width=4, height=3)
    sweeper.place_bombs({(0, 0), (1, 2), (2, 2)})
    expected_neighbors: List[List[Optional[int]]] = [
        [None for _ in range(4)] for _ in range(3)]
    assert sweeper.num_neighboring_bombs == expected_neighbors
    sweeper.click_cell(1, 1)
    expected_neighbors[1][1] = 3
    assert sweeper.num_neighboring_bombs == expected_neighbors
