from dataclasses import dataclass
from typing import List

from poker_hands import Card


@dataclass
class Hand:
    cards: List[Card]

    def __post_init__(self):
        num_cards = len(self.cards)
        if num_cards != 5:
            raise ValueError('A poker hand must have 5 cards')
        # Check if all 5 cards are unique
        if len(set(self.cards)) != num_cards:
            raise ValueError('Every card must be unique')
