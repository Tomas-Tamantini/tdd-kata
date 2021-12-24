from bowling_game import BowlingGame


def roll_many(pins: int, times: int = 20) -> BowlingGame:
    game = BowlingGame()
    for _ in range(times):
        game.roll(pins)
    return game


def test_can_score_gutter_game():
    game = roll_many(0)
    assert game.score() == 0


def test_can_score_all_ones():
    game = roll_many(1)
    assert game.score() == 20
