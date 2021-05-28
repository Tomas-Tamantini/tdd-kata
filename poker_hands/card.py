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


RANK_REPR = {
    10: 'T',
    FaceRank.JACK: 'J',
    FaceRank.QUEEN: 'Q',
    FaceRank.KING: 'K',
    FaceRank.ACE: 'A'
}


@dataclass
class Card:
    rank: int
    suit: Suit

    def __post_init__(self):
        if self.rank < 1 or self.rank > 14:
            raise ValueError('Invalid rank (must be a number between 1 and 14)')
        if self.rank == 1:
            self.rank = FaceRank.ACE

    def __str__(self):
        rank_str = str(self.rank) if self.rank < 10 else RANK_REPR[self.rank]
        return rank_str + self.suit
