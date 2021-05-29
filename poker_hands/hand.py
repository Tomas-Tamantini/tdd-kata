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


class ShowdownResult(int, Enum):
    LOSS = -1
    TIE = 0
    WIN = 1


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
        highest_rank_count = max([card_ranks.count(r) for r in card_ranks])
        num_different_ranks = len(set(card_ranks))
        if num_different_ranks == 4:
            return HandRank.PAIR
        if num_different_ranks == 3:
            return HandRank.THREE_OF_A_KIND if highest_rank_count == 3 else HandRank.TWO_PAIRS
        if num_different_ranks == 2:
            return HandRank.FULL_HOUSE if highest_rank_count == 3 else HandRank.FOUR_OF_A_KIND
        card_suits = [c.suit for c in self.cards]
        is_flush = len(set(card_suits)) == 1
        if Hand.__are_in_sequence(card_ranks):
            return HandRank.STRAIGHT_FLUSH if is_flush else HandRank.STRAIGHT
        return HandRank.FLUSH if is_flush else HandRank.HIGH_CARD

    def showdown_result(self, other: "Hand") -> ShowdownResult:
        # Check if every card is unique
        all_cards = set.union(set(self.cards), set(other.cards))
        if len(all_cards) < len(self.cards) + len(other.cards):
            raise ValueError('Every card must be unique')
        return ShowdownResult.LOSS

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
