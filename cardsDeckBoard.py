import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def real(self):
        print("{} of {}".format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suits in ["Spades", "Diamonds", "Clubs", "Hearts"]:
            for a in range(2,11):
                self.cards.append(Card(suits,a))
            #
            # What about this way?
            #
            for b in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suits,b))

    def show(self):
        for b in self.cards:
            b.show()

    def randomshuffle(self):
    #    random.shuffle(self.cards)

        """
        for card in self.cards:
            index = self.cards.index(card)
            rnd = randint(0, len(self.cards)-1)
            print("{} of {}".format(card.value,card.suit))
         """

class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.playerCards = []


class BoardCard:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        self.row = 0
        self.column = 0

class Board:
    def __init__(self):
        self.boardCards = []
        self.build()

    def build(self):
        for suits in ["Spades", "Diamonds", "Clubs", "Hearts"]:
            for a in range(2,11):
                self.boardCards.append(BoardCard(suits,a))

 #   def rows_and_cols(self):

 # 1.
deck = Deck()

# 2.
deck.build()

# 3.
deck.randomshuffle()
random.shuffle(deck.cards)

# 4. Get two players' name and create objects
players = []

#
# TODO: try to optimize... with 'input'
#

playerName = input("Give me a name:")
player1 = Player(playerName, 1)
players.append(player1)

playerName = input("Give me a name:")
player2 = Player(playerName, 2)
players.append(player2)

# 5. Give 6 cards to each of them
for player in players:
    for i in range(6):
        player.playerCards.append(deck.cards[i])
        deck.cards.remove(deck.cards[i])
    for card in player.playerCards:
        print("{} has {} of {}".format(player.name,card.value,card.suit))


"""TODO:
1. Create a Board Class with List[Board Card]
2. Create a Board Card Class with value, suit, column, row
"""
