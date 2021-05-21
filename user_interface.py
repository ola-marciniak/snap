import random
from random import randint
from time import sleep
import constant as c


def draw():
    """ Draw situation """
    print('Draw! There\'s no winner.')
    exit()


def think(card_1, card_2):
    """ After a random period of time checks if the values of the displayed cards are the same
     If yes, randomly chooses a winner
     Parameters:
        card_1, card_2 - cards displayed at the moment
     """
    sleep(randint(c.MIN_THINKING, c.MAX_THINKING))
    if card_1.value == card_2.value:
        players = [c.NAME_1, c.NAME_2]
        winner = random.choice(players)
        print(winner, ': Snap!')
        print(winner, 'wins!')
        exit()
    else:
        return


def get_top_card(deck):
    """ Takes a card and removes it from the player's deck
    Parameters:
        deck - the deck to take the card from
    """
    if len(deck) != 0:
        return deck.pop(-1)
    else:
        draw()
