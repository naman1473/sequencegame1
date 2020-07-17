import random

cards = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
royals = ["Jack", "Queen", "King", "Ace"]
carddeck = []

ranks = ["♣", "♦", "♥", "♠"]
# https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
suits = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

#for rank in ranks:
   # for suit in suits:
      #  print(rank + suit)

# create cards - TODO: refactor
for i in range(2,11):
    cards.append(str(i))
for a in range(len(royals)):
    cards.append(royals[a])
for c in range(4):
    for d in range(13):
        card = {
            "name" : cards[d] + " of " + suits[c],
            "player" : 0
        }
     #   card1 = cards[d] + " of " + suits[c]
        carddeck.append(card)

# double the deck
carddeck.extend(carddeck)

# check the lenght of the list
print(len(carddeck))

# shuffle
random.shuffle(carddeck)


# create players - DRY (Don't repeat yourself) <=> WET (Wasting everyone's time)
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

player = Player("Bill")
player.cards = ["A", "B"]

"""
TODO:
- recreate cards as Class/Object
- add given number of random cards to each player => of course remove them from the deck
- create Deck/Table Class/Object
"""
