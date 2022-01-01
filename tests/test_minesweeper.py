import pytest
from minesweeper import MineSweeper, sweeper


def test_grid_starts_with_all_hidden_cells():
    assert MineSweeper(width=10, height=8).num_hidden_cells == 80


@pytest.mark.parametrize('i, j', [(-1, 0), (0, -1), (10, 5), (5, 8)])
def test_cannot_show_cell_not_on_grid(i, j):
    sweeper = MineSweeper(width=10, height=8)
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
