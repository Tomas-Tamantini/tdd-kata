from tic_tac_toe import TicTacToe


def test_grid_starts_empty():
    t = TicTacToe()
    assert t.num_empty_cells == 9
