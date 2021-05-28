import pytest

from poker_hands.card import Card, Suit, FaceRank


def test_initialize_card():
    # Valid initializations
    Card(rank=5, suit=Suit.CLUBS)
    Card(rank=12, suit=Suit.CLUBS)
    Card(rank=FaceRank.QUEEN, suit=Suit.DIAMONDS)

    # Invalid initializations
    with pytest.raises(ValueError):
        Card(rank=15, suit=Suit.HEARTS)
        Card(rank=-3, suit=Suit.HEARTS)


