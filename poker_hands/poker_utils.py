from typing import List

from poker_hands import Card


def cards_are_unique(cards: List[Card]) -> bool:
    return len(cards) == len(set(cards))
