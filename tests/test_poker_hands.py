import pytest

from poker_hands import Card, Suit, FaceRank, parse_card, Hand, parse_hand, HandRank


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


def test_parse_card_from_str():
    c = parse_card('5h')
    assert c.rank == 5 and c.suit == Suit.HEARTS

    c = parse_card(' Ac ')
    assert c.rank == FaceRank.ACE and c.suit == Suit.CLUBS

    c = parse_card(' jd ')
    assert c.rank == FaceRank.JACK and c.suit == Suit.DIAMONDS

    with pytest.raises(ValueError):
        parse_card('1d')
    with pytest.raises(ValueError):
        parse_card('2p')


def test_initialize_poker_hand():
    # Valid initializations - 5 unique cards
    Hand(cards=[
        Card(rank=5, suit=Suit.CLUBS),
        Card(rank=FaceRank.JACK, suit=Suit.CLUBS),
        Card(rank=FaceRank.JACK, suit=Suit.SPADES),
        Card(rank=1, suit=Suit.HEARTS),
        Card(rank=14, suit=Suit.DIAMONDS),
    ])

    # Invalid initializations
    with pytest.raises(ValueError):
        # Less than 5 cards
        Hand(cards=[])

    with pytest.raises(ValueError):
        # Less than 5 cards
        Hand(cards=[Card(rank=5, suit=Suit.CLUBS), Card(rank=FaceRank.JACK, suit=Suit.CLUBS), ])

    with pytest.raises(ValueError):
        # Cards are not all unique (ace of hearts appears twice)
        Hand(cards=[
            Card(rank=5, suit=Suit.CLUBS),
            Card(rank=FaceRank.JACK, suit=Suit.CLUBS),
            Card(rank=FaceRank.JACK, suit=Suit.SPADES),
            Card(rank=1, suit=Suit.HEARTS),
            Card(rank=14, suit=Suit.HEARTS),
        ])


def test_parse_hand_from_str():
    hand = parse_hand('2h, 7s, Tc, Jd, Ah')
    expected_cards = {
        Card(rank=2, suit=Suit.HEARTS),
        Card(rank=7, suit=Suit.SPADES),
        Card(rank=10, suit=Suit.CLUBS),
        Card(rank=11, suit=Suit.DIAMONDS),
        Card(rank=14, suit=Suit.HEARTS)
    }
    assert expected_cards == set(hand.cards)


def test_hand_rank():
    test_cases = {
        HandRank.HIGH_CARD: ['2h, 7s, Tc, Jd, Ah', '2h, 3s, 4c, 5d, 7h', 'Ah, 3h, Jh, 5h, Qc'],
        HandRank.PAIR: ['2h, 3s, 5c, 5d, 6h', '2h, as, 5c, Ad, 6h', '2h, 3s, Jc, 5d, Jh'],
        HandRank.TWO_PAIRS: ['6s, 3s, 5c, 5d, 6h', '2h, as, 2c, Ad, 6h', '2h, 3s, Jc, 3d, Jh'],
        HandRank.THREE_OF_A_KIND: ['5h, 3s, 5c, 5d, 6h', '2h, as, 5c, Ad, ah', '2h, js, Jc, 5d, Jh'],
        HandRank.STRAIGHT: ['2h, 3s, 4c, 5d, 6h', '3h, 2s, ac, 5d, 4h', 'Jh, Th, Qh, Ah, Kc'],
        HandRank.FLUSH: ['2h, 7h, Th, Jh, Ah', '2d, 3d, 4d, 5d, 7d', 'Ah, 3h, Jh, 5h, Qh'],
        HandRank.FULL_HOUSE: ['6c, 6s, 5c, 5d, 6h', '2h, as, 2c, Ad, 2d', 'Jh, 3s, Jc, 3d, Js'],
        HandRank.FOUR_OF_A_KIND: ['5h, 5s, 5c, 5d, 6h', '2h, as, ac, Ad, ah', 'jh, js, Jc, 5d, Jd'],
    }
    for rank, tcs in test_cases.items():
        for tc in tcs:
            hand = parse_hand(tc)
            assert hand.rank == rank
