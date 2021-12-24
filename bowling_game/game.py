"""See game rules and kata specification at: https://kata-log.rocks/bowling-game-kata"""


class BowlingGame:
    def __init__(self) -> None:
        self.__rolls = []
        self.__num_standing_pins = 10
        self.__is_start_of_frame = True

    def roll(self, pins: int) -> None:
        if pins < 0 or pins > self.__num_standing_pins:
            raise ValueError("Invalid number of pins")
        self.__rolls.append(pins)
        if self.__is_start_of_frame and pins < 10:
            self.__num_standing_pins -= pins
            self.__is_start_of_frame = False
        else:
            self.__num_standing_pins = 10
            self.__is_start_of_frame = True

    def score(self) -> int:
        return sum(self.__rolls)
