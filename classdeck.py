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

    def show(self):
        for b in self.cards:
            b.show()

    def randomshuffle(self):
        for i in range(self.cards):
            random = random.ranint(0, i)
