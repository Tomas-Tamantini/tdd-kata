from dataclasses import dataclass
from typing import List

from poker_hands import Card


@dataclass
class Hand:
    cards: List[Card]

    def __post_init__(self):
        if len(self.cards) != 5:
            raise ValueError('A poker hand must have 5 cards')
