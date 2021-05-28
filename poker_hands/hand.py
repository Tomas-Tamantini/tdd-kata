from dataclasses import dataclass
from enum import Enum
from typing import List

from poker_hands import Card


class HandRank(int, Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9


@dataclass(frozen=True)
class Hand:
    cards: List[Card]

    def __post_init__(self):
        num_cards = len(self.cards)
        if num_cards != 5:
            raise ValueError('A poker hand must have 5 cards')
        # Check if all 5 cards are unique
        if len(set(self.cards)) != num_cards:
            raise ValueError('Every card must be unique')

    @property
    def rank(self) -> HandRank:
        card_ranks = [c.rank for c in self.cards]
        set_size = len(set(card_ranks))
        if set_size == 4:
            return HandRank.PAIR
        if set_size == 3:
            return HandRank.TWO_PAIRS
        return HandRank.HIGH_CARD
