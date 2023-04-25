#
#
#
import random
from dataclasses import dataclass
from itertools import product


@dataclass()
class PlayingCard:
    suit: str
    rank: str

    def __post_init__(self):
        self.suit = self.suit.lower()
        self.rank = self.rank.lower()


class CardDeck:
    SUITS = ['spades', 'diamonds', 'clubs', 'hearts']
    RANKS = list('ajkq') + list(str(n) for n in range(2, 11))

    @staticmethod
    def _filter_playing_cards(from_sequence):
        return list(filter(lambda a: type(a) == PlayingCard, from_sequence))

    def __init__(self, cards=None):
        playing_cards = None

        if type(cards) == list and len(cards) > 0:
            playing_cards = self._filter_playing_cards(cards)

        if playing_cards:
            self._cards = playing_cards
        else:
            self._cards = [PlayingCard(*args) for args in product(self.SUITS, self.RANKS)]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        if type(item) == slice:
            return CardDeck(self._cards[item])

        return self._cards[item]

    def __add__(self, other):
        if type(other) == PlayingCard:
            return CardDeck([*self._cards, other])
        elif type(other) == CardDeck:
            return CardDeck([*self._cards, *other._cards])

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if type(other) == int:
            return CardDeck(self._cards * other)

    def __rmul__(self, other):
        return self * other

    def draw(self, n=1):
        drawn_cards = list()

        for _ in range(n):
            idx = random.randrange(len(self))
            drawn_cards.append(self._cards.pop(idx))

        if n == 1:
            return drawn_cards[0]
        else:
            return CardDeck(drawn_cards)

    def __repr__(self):
        return f"CardDeck(cards={repr(self._cards)})"


if __name__ == "__main__":
    cd = CardDeck()
    cd2 = CardDeck(cards=[PlayingCard('spades', '4')])
    cd3 = CardDeck(cards=[PlayingCard('spades', '4'), PlayingCard('spades', '5'), "Andy"])
    cd4 = CardDeck(cards=[2, "a", "Andy"])
