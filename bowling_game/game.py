"""See game rules and kata specification at: https://kata-log.rocks/bowling-game-kata"""
from typing import List


class _Frame:
    def __init__(self, is_tenth_frame: bool = False):
        self.__is_tenth_frame = is_tenth_frame
        self.__rolls = []

    def add_roll(self, pins: int) -> None:
        if self.__is_tenth_frame and self.is_over:
            raise ValueError("Game is already over")
        if pins < 0 or pins > self.num_standing_pins():
            raise ValueError("Invalid number of pins")
        self.__rolls.append(pins)

    @property
    def rolls(self) -> List[int]:
        return self.__rolls

    @property
    def score(self) -> int:
        return sum(self.__rolls)

    def num_standing_pins(self) -> int:
        n = 10 - self.score
        if self.is_strike:
            if len(self.__rolls) > 1 and self.__rolls[1] == 10:
                return n + 20
            return n + 10
        if self.is_spare:
            return n + 10
        return n

    @property
    def is_strike(self) -> bool:
        return len(self.__rolls) > 0 and self.__rolls[0] == 10

    @property
    def is_spare(self) -> bool:
        if len(self.__rolls) < 2 or self.__rolls[0] == 10:
            return False
        return self.__rolls[0] + self.__rolls[1] == 10

    @property
    def is_over(self) -> bool:
        if len(self.__rolls) == 0:
            return False
        if not self.__is_tenth_frame:
            return len(self.__rolls) == 2 or self.__rolls[0] == 10
        if len(self.__rolls) == 2:
            return self.__rolls[0] + self.__rolls[1] < 10
        return len(self.__rolls) == 3


class BowlingGame:
    def __init__(self) -> None:
        self.__frames = []

    def __current_frame(self) -> _Frame:
        if len(self.__frames) == 0 or (len(self.__frames) < 10 and self.__frames[-1].is_over):
            is_tenth_frame = len(self.__frames) == 9
            self.__frames.append(_Frame(is_tenth_frame))
        return self.__frames[-1]

    def __subsequent_rolls(self, frame: _Frame) -> List[int]:
        frame_index = self.__frames.index(frame)
        rolls = []
        for i in range(frame_index + 1, len(self.__frames)):
            rolls += self.__frames[i].rolls
        return rolls

    def roll(self, pins: int) -> None:
        frame = self.__current_frame()
        frame.add_roll(pins)

    def score(self) -> int:
        s = 0
        for i, frame in enumerate(self.__frames):
            s += frame.score
            if i + 1 >= len(self.__frames):
                continue
            rolls = self.__subsequent_rolls(frame)
            if frame.is_spare and len(rolls) > 0:
                s += rolls[0]
            elif frame.is_strike:
                if len(rolls) > 0:
                    s += rolls[0]
                if len(rolls) > 1:
                    s += rolls[1]
        return s
