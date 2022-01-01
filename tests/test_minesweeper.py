from minesweeper import MineSweeper


def test_grid_starts_with_all_hidden_cells():
    assert MineSweeper(width=10, height=8).num_hidden_cells == 80
