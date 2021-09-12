from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple

from poker_hands import Card, FaceRank
from poker_hands.poker_utils import cards_are_unique


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


@dataclass
class Hand:
    cards: List[Card]

    def __post_init__(self):
        # Validations
        num_cards = len(self.cards)
        if num_cards != 5:
            raise ValueError('A poker hand must have 5 cards')
        if not cards_are_unique(self.cards):
            raise ValueError('Every card must be unique')

        # Get sorted card ranks
        rank_freq, self._sorted_card_ranks = self.__get_rank_freq_and_sorted_ranks()
        self._rank = self._get_hand_rank(rank_freq)

    @property
    def rank(self):
        return self._rank

    def __get_rank_freq_and_sorted_ranks(self) -> Tuple[Dict, Tuple[int, ...]]:
        rank_freq = self._rank_frequency()
        sorted_values = Hand._get_sorted_card_ranks(rank_freq)
        return rank_freq, sorted_values

    def _get_hand_rank(self, rank_freq: Dict) -> HandRank:
        num_different_ranks = len(rank_freq)
        highest_freq = max([f for f in rank_freq.values()])

        if num_different_ranks == 4:
            return HandRank.PAIR
        if num_different_ranks == 3:
            return HandRank.THREE_OF_A_KIND if highest_freq == 3 else HandRank.TWO_PAIRS
        if num_different_ranks == 2:
            return HandRank.FULL_HOUSE if highest_freq == 3 else HandRank.FOUR_OF_A_KIND
        card_suits = [c.suit for c in self.cards]
        is_flush = len(set(card_suits)) == 1
        if Hand.__are_in_sequence(self._sorted_card_ranks):
            return HandRank.STRAIGHT_FLUSH if is_flush else HandRank.STRAIGHT
        return HandRank.FLUSH if is_flush else HandRank.HIGH_CARD

    def showdown_result(self, other: "Hand") -> ShowdownResult:
        # Check if every card is unique
        if not cards_are_unique(self.cards + other.cards):
            raise ValueError('Every card must be unique')
        if self.rank > other.rank:
            return ShowdownResult.WIN
        elif self.rank < other.rank:
            return ShowdownResult.LOSS

        # Check straight/straight flush separately because of A-5 possibility:
        if self.rank == HandRank.STRAIGHT or self.rank == HandRank.STRAIGHT_FLUSH:
            return self._showdown_straight_result(other)

        # Check every other case
        for i in reversed(range(len(self._sorted_card_ranks))):
            if self._sorted_card_ranks[i] > other._sorted_card_ranks[i]:
                return ShowdownResult.WIN
            elif self._sorted_card_ranks[i] < other._sorted_card_ranks[i]:
                return ShowdownResult.LOSS
        return ShowdownResult.TIE

    @staticmethod
    def __are_in_sequence(sorted_card_ranks: Tuple[int, ...]) -> bool:
        """Check if 5 cards ranks are in sequence"""
        if sorted_card_ranks == (2, 3, 4, 5, 14):
            return True  # Sequence from ace to 5
        for i in range(1, len(sorted_card_ranks)):
            if sorted_card_ranks[i] - sorted_card_ranks[i - 1] != 1:
                return False
        return True

    def _rank_frequency(self) -> Dict:
        """Gets the frequency of each card rank. Ex: 2h, 5s, Jd, Js, Kc -> {2: 1, 5: 1, J: 2, K: 1}"""
        out_dict = {}
        for c in self.cards:
            if c.rank not in out_dict:
                out_dict[c.rank] = 1
            else:
                out_dict[c.rank] += 1
        return out_dict

    @staticmethod
    def _get_sorted_card_ranks(rank_frequency) -> Tuple[int, ...]:
        """
        Returns every unique card rank, sorted by their importance (from least to most important).
        Importance is measured by how frequently the rank appears, and in case of a tie, the rank itself.
        Ex. 2h, 5s, Jd, Js, Kc -> (2, 5, K, J) J comes last because it is the most frequent
        """
        sorted_tuples = [(frequency, rank) for rank, frequency in rank_frequency.items()]
        sorted_tuples.sort()
        return tuple(r for _, r in sorted_tuples)

    @staticmethod
    def _straight_highest_card(straight_sorted_ranks: Tuple[int, ...]) -> int:
        last_rank = straight_sorted_ranks[-1]
        if last_rank == FaceRank.ACE and straight_sorted_ranks[-2] == 5:
            return 5
        return last_rank

    def _showdown_straight_result(self, other: "Hand") -> ShowdownResult:
        mine = Hand._straight_highest_card(self._sorted_card_ranks)
        theirs = Hand._straight_highest_card(other._sorted_card_ranks)
        if mine > theirs:
            return ShowdownResult.WIN
        elif mine < theirs:
            return ShowdownResult.LOSS
        return ShowdownResult.TIE

    def __str__(self):
        rank_str = str(self.rank).split('.')[1].replace('_', ' ')
        return ', '.join(map(str, self.cards)) + f' - {rank_str}'
