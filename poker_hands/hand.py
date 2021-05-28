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
            for r in card_ranks:
                if card_ranks.count(r) == 3:
                    return HandRank.THREE_OF_A_KIND
            return HandRank.TWO_PAIRS
        if Hand.__are_in_sequence(card_ranks):
            return HandRank.STRAIGHT
        return HandRank.HIGH_CARD

    @staticmethod
    def __are_in_sequence(ranks: List[int]) -> bool:
        """Check if 5 cards ranks are in sequence"""
        ranks.sort()
        if ranks == [2, 3, 4, 5, 14]:
            return True  # Sequence from ace to 5
        for i in range(1, len(ranks)):
            if ranks[i] - ranks[i - 1] != 1:
                return False
        return True
