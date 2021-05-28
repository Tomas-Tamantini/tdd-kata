from poker_hands import Card, Suit, Hand
from poker_hands.card import RANK_REPR


def parse_card(str_format: str) -> Card:
    """Load card from strings of the form: 2h, 7s, Tc, Jd, Ah..."""
    stripped = str_format.strip()
    return Card(rank=_parse_rank(stripped[0]), suit=Suit(stripped[1].lower()))


def parse_hand(str_format: str) -> Hand:
    """Load hand from strings. The cards should be separated by comma such as in example: 2h, 7s, Tc, Jd, Ah"""
    card_strings = str_format.split(',')
    return Hand(cards=[parse_card(s) for s in card_strings])


def _parse_rank(c: chr) -> int:
    u = c.upper()
    for rank, rank_repr in RANK_REPR.items():
        if u == rank_repr:
            return rank
    if ord('2') <= ord(c) <= ord('9'):
        return int(c)
    raise ValueError('Invalid rank. Must be 2-9, or T, J, Q, K, A.')
