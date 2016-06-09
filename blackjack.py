# Classes:
#   Person
#       \Dealer
#       \Player
#   Deck
#   Card
#   Game

import random

class Person(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def show_hand(self, hand=self.hand):
        return " ".join(hand)



class Dealer(Person):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.name = "Dealer"

    def reveal(self):
        # Reveals second card
        pass


class Player(Person):
    def __init__(self, name, money=50):
        super(self.__class__, self).__init__(name)
        self.name = name
        self.bet = 0
        self.money = money

    def hit(self, target, hand, deck):
        deck.give_card(target, hand)

    def double(self, target):
        # Double bet and get one hit, end turn
        pass

    def can_split(self):
        if self.hand[0].value == self.hand[1].value:
            return True

    def split(self, target, deck):
        # Split hand on duplicate cards only, play separate hands
        if self.can_split():
            self.hand2 = self.hand.pop(1)
            self.hit(self, self.hand, deck)
            self.hit(self, self.hand2, deck)


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Deck(object):
    def __init__(self):
        self.cards = []
        self.discard = []
        self.suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(str(value), suit))
        self.shuffle(self.cards)

    def give_card(self, target, handnum):
        # take first card, give to target, adding to target's hand, removing the card from deck
        target.handnum.append(self.cards.pop(0))

    def shuffle(self, arr):
        # shuffle the deck
        self.discard += self.cards
        self.cards = []
        for i in range(0,52):
            randnum = round(random.random() * len(self.discard))
            self.cards.append(self.discard.pop(randnum))


class Game(object):
    def __init__(self):
        self.turns = 0
        self.setup = True
        self.dealer = Dealer()
        self.people = []
        self.deck = Deck()
        self.run_game()

        while(self.setup):
            print("Please enter players, type 'start' to complete setup and begin game.")
            response = input("Player Name: ")
            if response.lower() == 'start':
                self.setup = False
            else:
                self.people.append(Player(response))

    def deal(self):
        for person in self.people:
            self.deck.give_card(person, person.hand)
            self.deck.give_card(person, person.hand)

    def wager(self, target, value):
        # Increase bet
        if target.money >= value:
            target.bet += value
        else:
            # You don't have enough money

    def check_hand(self, target):
        play_value = 0
        for card in target.hand:
            if type(card.value) == int:
                play_value += card.value
            else:
                if card.value == "King" or card.value == "Queen" or card.value == "Jack":
                    play_value += 10
                elif card.value == "Ace" and play_value + 11 <= 21:
                    play_value += 11
                else:
                    play_value += 1
        return play_value

    def run_game(self):
        self.deal()  # deal two cards to each player
        playing = True
        players_in_game = self.people
        players_in_game += self.dealer
        while(playing):
            # repeat game turns by player
            for person in players_in_game:
                print("You have "+person.show_hand())
                split = ""
                if person.can_split():
                    split = ", or 'split' to split your hand and bet separately "
                choice = input("Enter 'hit' to hit, 'stand' to stand, 'double' to double your bet and hit once"+split+", \nor 'leave' to leave the game").lower()
                if choice == 'hit':

                elif choice == 'stand':

                elif choice == 'double':

                elif choice == 'leave':

                else:
                    # please enter a valid choice
            if len(players_in_game) == 1:
                playing = False


# deck = Deck()
# deck.create_deck()
# deck.show_cards()