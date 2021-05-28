import pytest

from poker_hands import Card, Suit, FaceRank


def test_initialize_card():
    # Valid initializations
    Card(rank=5, suit=Suit.CLUBS)
    Card(rank=12, suit=Suit.CLUBS)
    Card(rank=FaceRank.QUEEN, suit=Suit.DIAMONDS)

    # Invalid initializations
    with pytest.raises(ValueError):
        Card(rank=15, suit=Suit.HEARTS)
        Card(rank=-3, suit=Suit.HEARTS)


def test_ace_can_be_1_or_14():
    c = Card(rank=14, suit=Suit.SPADES)
    assert c.rank == FaceRank.ACE

    c = Card(rank=1, suit=Suit.DIAMONDS)
    assert c.rank == FaceRank.ACE
