import random
import cards
from random import randint
from time import sleep

NAME_1 = 'Coco'
NAME_2 = 'Dora'

MIN_THINKING = 1
MAX_THINKING = 2


def draw():
    print('draw!!!!')
    exit()


class Snap:

    #shuffle cards and divide into two players
    def get_decks(self):
        self.deck = cards.generate_deck()
        random.shuffle(self.deck)
        deck1 = self.deck[:len(self.deck) // 2]
        deck2 = self.deck[len(self.deck) // 2:]
        return deck1, deck2

    #take a card and remove it from player's deck
    def get_top_card(self, deck):
        if len(deck) !=0:
            return deck.pop(-1)
        else:
            draw()


    def think(self, card_1, card_2):
        sleep(randint(MIN_THINKING, MAX_THINKING))
        if card_1.value == card_2.value:
            players = [NAME_1, NAME_2]
            winner = random.choice(players)
            print(winner, ': Snap!')
            print(winner, 'wins!')
            exit()
        else:
            return



    def start_game(self):
        global deck, name
        print('Starting the game Snap')
        #get player's decks
        deck_1, deck_2 = self.get_decks()

        #initialise the game with two cards
        card_1 = self.get_top_card(deck_1)
        print('displayed card of ', NAME_1, ': ', card_1)
        sleep(randint(MIN_THINKING, MAX_THINKING))
        card_2 = self.get_top_card(deck_2)
        print('displayed card of ', NAME_2, ': ', card_2)
        winner = 0

        while not(len(deck_1) == 0 or len(deck_2) == 0):
            self.think(card_1, card_2)
            card_1 = self.get_top_card(deck_1)
            print('displayed card of ', NAME_1, ': ', card_1)
            self.think(card_1, card_2)

            card_2 = self.get_top_card(deck_2)
            print('displayed card of ', NAME_2, ': ', card_2)
            # if self.think(card_1, card_2) == 1:
            #     break
            self.think(card_1, card_2)


        if (len(deck_1) == 0 or len(deck_2) == 0):
            draw()
