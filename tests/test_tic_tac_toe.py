from tic_tac_toe import TicTacToe


def test_grid_starts_empty():
    t = TicTacToe()
    assert t.num_empty_cells == 9


def test_grid_initialization():
    t = TicTacToe(naughts={(0, 0), (1, 2)}, crosses={(1, 1), (0, 2), (0, 1)})
    assert t.num_empty_cells == 4


def test_hash_for_empty_grid():
    empty_game = TicTacToe()
    assert hash(empty_game) == 0


def test_hash_for_non_empty_grid():
    # To calculate hash, X = 2, O = 1, EMPTY = 0, and each position is a power of three.
    t = TicTacToe(naughts={(2, 2)}, crosses={(0, 0), (0, 1)})
    assert hash(t) == 17497  # 2 * 3^8 + 2 * 3^7 + 1 * 3^0


def test_hash_should_be_the_same_after_rotation_and_reflection():
    # To calculate hash, X = 2, O = 1, EMPTY = 0, and each position is a power of three. There are at most 8
    # configurations of the grid (2 reflections X 4 rotations). Choose the largest number of all 8
    t = TicTacToe(naughts={(0, 0), (1, 2)}, crosses={(1, 1), (0, 2), (0, 1)})
    t90 = TicTacToe(naughts={(0, 1), (2, 0)}, crosses={(0, 0), (1, 0), (1, 1)})
    t180 = TicTacToe(naughts={(1, 0), (2, 2)}, crosses={(1, 1), (2, 0), (2, 1)})
    t270 = TicTacToe(naughts={(0, 2), (2, 1)}, crosses={(1, 1), (1, 2), (2, 2)})

    tr = TicTacToe(naughts={(0, 0), (2, 1)}, crosses={(1, 1), (2, 0), (1, 0)})
    tr90 = TicTacToe(naughts={(1, 0), (0, 2)}, crosses={(0, 0), (0, 1), (1, 1)})
    tr180 = TicTacToe(naughts={(0, 1), (2, 2)}, crosses={(1, 1), (0, 2), (1, 2)})
    tr270 = TicTacToe(naughts={(2, 0), (1, 2)}, crosses={(1, 1), (2, 1), (2, 2)})

    expected_hash = 18630  # hash(tr90) = XXO|OX*|*** = 2 * 3^8 + 2 * 3^7 + 1 * 3^6 + 1 * 3^5 + 2 * 3^4
    assert hash(t) == hash(t90) == hash(t180) == hash(t270) == hash(tr) == hash(tr90) == hash(tr180) == hash(
        tr270) == expected_hash


def test_play():
    t = TicTacToe()
    t = t.play(0, 1)
    t = t.play(1, 2)
    t = t.play(2, 2)
    assert t == TicTacToe(naughts={(1, 2)}, crosses={(0, 1), (2, 2)})


def test_children():
    t = TicTacToe()
    children = {TicTacToe(crosses={(0, 0)}), TicTacToe(crosses={(0, 1)}), TicTacToe(crosses={(1, 1)})}
    assert t.children == children


def test_game_over():
    t = TicTacToe(naughts={(0, 0), (1, 2)}, crosses={(1, 1), (0, 2), (0, 1)})
    assert not t.is_over
    # 3 in a row
    t = TicTacToe(naughts={(0, 0), (1, 2)}, crosses={(2, 1), (2, 2), (2, 0)})
    assert t.is_over

    # 3 in a column
    t = TicTacToe(naughts={(0, 1), (2, 1), (1, 1)}, crosses={(0, 0), (1, 0), (1, 2), (2, 2)})
    assert t.is_over

    # 3 diagonal
    t = TicTacToe(naughts={(0, 0), (1, 1), (2, 2)}, crosses={(2, 0), (0, 2), (1, 0), (0, 1)})
    assert t.is_over

    # 3 diagonal
    t = TicTacToe(naughts={(0, 0), (2, 2)}, crosses={(0, 2), (1, 1), (2, 0)})
    assert t.is_over
