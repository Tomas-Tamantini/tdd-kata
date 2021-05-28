from dataclasses import dataclass
from enum import Enum


class Suit(str, Enum):
    HEARTS = 'h'
    CLUBS = 'c'
    DIAMONDS = 'd'
    SPADES = 's'


class FaceRank(int, Enum):
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@dataclass
class Card:
    rank: int
    suit: Suit

    def __post_init__(self):
        if self.rank < 1 or self.rank > 14:
            raise ValueError('Invalid rank (must be a number between 1 and 14)')
        if self.rank == 1:
            self.rank = FaceRank.ACE
