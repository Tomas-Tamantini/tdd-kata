import pytest
from bowling_game import BowlingGame


def roll_many(game: BowlingGame, pins: int, times: int = 20) -> None:
    for _ in range(times):
        game.roll(pins)


@pytest.mark.parametrize("bad_roll", [11, -1])
def test_cannot_roll_invalid_number_of_pins(bad_roll: int):
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(bad_roll)


def test_game_must_keep_track_of_standing_pins():
    game = BowlingGame()
    for pins in (10, 2, 3, 7):
        game.roll(pins)
    with pytest.raises(ValueError):
        game.roll(4)  # only 3 standing pins


def test_can_score_gutter_game():
    game = BowlingGame()
    roll_many(game, 0)
    assert game.score() == 0


def test_can_score_all_ones():
    game = BowlingGame()
    roll_many(game, 1)
    assert game.score() == 20


def test_can_score_spare():
    game = BowlingGame()
    game.roll(8)
    game.roll(2)
    game.roll(3)
    roll_many(game, 0, 17)
    assert game.score() == 16


def test_can_score_strike():
    game = BowlingGame()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 0, 16)
    assert game.score() == 24


def test_can_score_perfect_game():
    game = BowlingGame()
    roll_many(game, 10, 12)
    assert game.score() == 300


def test_cannot_play_more_than_10_frames():
    game = BowlingGame()
    roll_many(game, 10, 9)
    roll_many(game, 4, 2)
    with pytest.raises(ValueError):
        game.roll(0)
