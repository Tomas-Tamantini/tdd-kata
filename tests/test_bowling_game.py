from bowling_game import BowlingGame


def test_can_score_gutter_game():
    game = BowlingGame()
    for _ in range(20):
        game.roll(0)
    assert game.score() == 0
