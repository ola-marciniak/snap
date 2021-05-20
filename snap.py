import random
import cards
from random import randint
from time import sleep
import constant as c
import user_interface as ui


class Snap:
    """ The Snap object

    To start a game, call the run_game() method

    Attributes:
        self.deck - a deck of cards used in the game (sorted)
        get_decks - shuffles the deck and divides it equally among the players
        start_game - starts a game of snap

    """

    def __init__(self):
        self.deck = cards.generate_deck()

    def get_decks(self):
        """ Shuffles a deck of cards and divides it into two (for two players)"""
        random.shuffle(self.deck)
        deck1 = self.deck[:len(self.deck) // 2]
        deck2 = self.deck[len(self.deck) // 2:]
        return deck1, deck2

    def start_game(self):
        """ Starts a game of Snap"""
        print('Starting the game Snap...')
        sleep(1)
        # get player's decks
        deck_1, deck_2 = self.get_decks()

        # initialise the game with two cards
        card_1 = ui.get_top_card(deck_1)
        print(c.NAME_1, 'displays card', card_1)
        # wait before displaying the second card
        sleep(randint(c.MIN_THINKING, c.MAX_THINKING))

        card_2 = ui.get_top_card(deck_2)
        print(c.NAME_2, 'displays card', card_2)

        while not (len(deck_1) == 0 or len(deck_2) == 0):
            # check if the values are the same
            ui.think(card_1, card_2)

            # display another card
            card_1 = ui.get_top_card(deck_1)
            print(c.NAME_1, 'displays card', card_1)
            ui.think(card_1, card_2)

            card_2 = ui.get_top_card(deck_2)
            print(c.NAME_2, 'displays card', card_2)
            ui.think(card_1, card_2)

        # draw if a player runs out of their cards
        if len(deck_1) == 0 or len(deck_2) == 0:
            ui.draw()
