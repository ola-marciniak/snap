from collections import namedtuple


class Card(namedtuple('CardData', ['suit', 'value'])):
    suits = '♣ ♢ ♡ ♠'.split()
    values = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __str__(self):
        return '{} {}'.format(self.suit, self.value)


def generate_deck():
    """Generates a deck of cards"""
    return [Card(suit, value)
            for suit in Card.suits for value in Card.values]
