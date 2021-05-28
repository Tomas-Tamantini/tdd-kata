from poker_hands import Card, Suit, FaceRank


def parse_card(str_format: str) -> Card:
    stripped_and_lower = str_format.strip().lower()
    return Card(rank=_parse_rank(stripped_and_lower[0]), suit=_parse_suit(stripped_and_lower[1]))


def _parse_rank(c: chr) -> int:
    return 5


def _parse_suit(c: chr) -> Suit:
    return Suit.HEARTS
