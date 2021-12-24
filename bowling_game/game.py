"""See game rules and kata specification at: https://kata-log.rocks/bowling-game-kata"""


class BowlingGame:
    def __init__(self) -> None:
        self.__score = 0

    def roll(self, pins: int) -> None:
        self.__score += pins

    def score(self) -> int:
        return self.__score
