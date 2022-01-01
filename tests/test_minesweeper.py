import pytest
from minesweeper import MineSweeper


def test_grid_starts_with_all_hidden_cells():
    assert MineSweeper(width=10, height=8).num_hidden_cells == 80


@pytest.mark.parametrize('i, j', [(-1, 0), (0, -1), (10, 5), (5, 8)])
def test_cannot_show_cell_not_on_grid(i, j):
    sweeper = MineSweeper(width=10, height=8)
    with pytest.raises(ValueError):
        sweeper.click_cell(i, j)
