from poker_hands import Card, Suit
from poker_hands.card import RANK_REPR


def parse_card(str_format: str) -> Card:
    stripped = str_format.strip()
    return Card(rank=_parse_rank(stripped[0]), suit=Suit(stripped[1].lower()))


def _parse_rank(c: chr) -> int:
    u = c.upper()
    for rank, rank_repr in RANK_REPR.items():
        if u == rank_repr:
            return rank
    if ord('2') <= ord(c) <= ord('9'):
        return int(c)
    raise ValueError('Invalid rank. Must be 2-9, or T, J, Q, K, A.')
