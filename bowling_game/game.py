"""See game rules and kata specification at: https://kata-log.rocks/bowling-game-kata"""


class BowlingGame:
    def __init__(self) -> None:
        self.__rolls = []
        self.__num_standing_pins = 10
        self.__is_start_of_frame = True
        self.__spare_indices = set()
        self.__strike_indices = set()

    def roll(self, pins: int) -> None:
        if pins < 0 or pins > self.__num_standing_pins:
            raise ValueError("Invalid number of pins")
        roll_index = len(self.__rolls)
        if self.__is_start_of_frame:
            if pins == 10:
                self.__strike_indices.add(roll_index)
            else:
                self.__is_start_of_frame = False
                self.__num_standing_pins -= pins
        else:
            self.__is_start_of_frame = True
            self.__num_standing_pins = 10
            if pins + self.__rolls[- 1] == 10:
                self.__spare_indices.add(roll_index)
        self.__rolls.append(pins)

    def score(self) -> int:
        s = sum(self.__rolls)
        for i in self.__spare_indices:
            if i + 1 < len(self.__rolls):
                s += self.__rolls[i+1]
        return s
