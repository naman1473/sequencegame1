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
        random.shuffle(self.cards)

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
            for b in ["Jack", "Queen", "King", "Ace"]:
                self.boardCards.append(BoardCard(suits,b))
            for c in range(100):
                self.boardCards.append(BoardCard(None,c))

                colouredchip = Card("Corner", 0)
                self.boardCards.insert(0, colouredchip)
                colouredchip = Card("Corner1", 0)
                self.boardCards.insert(9, colouredchip)
                colouredchip = Card("Corner2", 0)
                self.boardCards.insert(90, colouredchip)
                colouredchip = Card("Corner3", 0)
                self.boardCards.insert(99, colouredchip)

                card = Card("Spades", 2)
                self.boardCards.insert(1, card)
                card = Card("Spades", 3)
                self.boardCards.insert(2, card)
                card = Card("Spades", 4)
                self.boardCards.insert(3, card)
                card = Card("Spades", 5)
                self.boardCards.insert(4, card)
                card = Card("Spades", 6)
                self.boardCards.insert(5, card)
                card = Card("Spades", 7)
                self.boardCards.insert(6, card)
                card = Card("Spades", 8)
                self.boardCards.insert(7, card)
                card = Card("Spades", 9)
                self.boardCards.insert(8, card)

# 1 row complete from top

                card = Card("Clubs", 6)
                self.boardCards.insert(10, card)
                card = Card("Clubs", 5)
                self.boardCards.insert(11, card)
                card = Card("Clubs", 4)
                self.boardCards.insert(12, card)
                card = Card("Clubs", 3)
                self.boardCards.insert(13, card)
                card = Card("Clubs", 2)
                self.boardCards.insert(14, card)
                card = Card("Hearts", "Ace")
                self.boardCards.insert(15, card)
                card = Card("Hearts", "King")
                self.boardCards.insert(16, card)
                card = Card("Hearts", "Queen")
                self.boardCards.insert(17, card)
                card = Card("Hearts", 10)
                self.boardCards.insert(18, card)
                card = Card("Spades", 10)
                self.boardCards.insert(19, card)

# 2 row complete from top

                card = Card("Clubs", 7)
                self.boardCards.insert(20, card)
                card = Card("Spades", "Ace")
                self.boardCards.insert(21, card)
                card = Card("Diamonds", 2)
                self.boardCards.insert(22, card)
                card = Card("Diamonds", 3)
                self.boardCards.insert(23, card)
                card = Card("Diamonds", 4)
                self.boardCards.insert(24, card)
                card = Card("Diamonds", 5)
                self.boardCards.insert(25, card)
                card = Card("Diamonds", 6)
                self.boardCards.insert(26, card)
                card = Card("Diamonds", 7)
                self.boardCards.insert(27, card)
                card = Card("Hearts", 9)
                self.boardCards.insert(28, card)
                card = Card("Spades", "Queen")
                self.boardCards.insert(29, card)

# 3 row complete from top

                card = Card("Clubs", 8)
                self.boardCards.insert(30, card)
                card = Card("Spades", "King")
                self.boardCards.insert(31, card)
                card = Card("Clubs", 6)
                self.boardCards.insert(32, card)
                card = Card("Clubs", 5)
                self.boardCards.insert(33, card)
                card = Card("Clubs", 4)
                self.boardCards.insert(34, card)
                card = Card("Clubs", 3)
                self.boardCards.insert(35, card)
                card = Card("Clubs", 2)
                self.boardCards.insert(36, card)
                card = Card("Diamonds", 8)
                self.boardCards.insert(37, card)
                card = Card("Hearts", 8)
                self.boardCards.insert(38, card)
                card = Card("Spades", "King")
                self.boardCards.insert(39, card)

# 4 row complete from top

                card = Card("Clubs", 9)
                self.boardCards.insert(40, card)
                card = Card("Spades", "Queen")
                self.boardCards.insert(41, card)
                card = Card("Clubs", 7)
                self.boardCards.insert(42, card)
                card = Card("Hearts", 6)
                self.boardCards.insert(43, card)
                card = Card("Hearts", 5)
                self.boardCards.insert(44, card)
                card = Card("Hearts", 4)
                self.boardCards.insert(45, card)
                card = Card("Hearts", "Ace")
                self.boardCards.insert(46, card)
                card = Card("Diamonds", 9)
                self.boardCards.insert(47, card)
                card = Card("Hearts", 7)
                self.boardCards.insert(48, card)
                card = Card("Spades", "Ace")
                self.boardCards.insert(49, card)

# 5 row complete from top

                card = Card("Clubs", 10)
                self.boardCards.insert(50, card)
                card = Card("Spades", 10)
                self.boardCards.insert(51, card)
                card = Card("Clubs", 8)
                self.boardCards.insert(52, card)
                card = Card("Hearts", 7)
                self.boardCards.insert(53, card)
                card = Card("Hearts", 2)
                self.boardCards.insert(54, card)
                card = Card("Hearts", 3)
                self.boardCards.insert(55, card)
                card = Card("Hearts", "King")
                self.boardCards.insert(56, card)
                card = Card("Diamonds", 10)
                self.boardCards.insert(57, card)
                card = Card("Hearts", 6)
                self.boardCards.insert(58, card)
                card = Card("Diamonds", 2)
                self.boardCards.insert(59, card)

# 6 row complete from top

                card = Card("Clubs", "Queen")
                self.boardCards.insert(60, card)
                card = Card("Spades", 9)
                self.boardCards.insert(61, card)
                card = Card("Clubs", 9)
                self.boardCards.insert(62, card)
                card = Card("Hearts", 8)
                self.boardCards.insert(63, card)
                card = Card("Hearts", 9)
                self.boardCards.insert(64, card)
                card = Card("Hearts", 10)
                self.boardCards.insert(65, card)
                card = Card("Hearts", "Queen")
                self.boardCards.insert(66, card)
                card = Card("Diamonds", "Queen")
                self.boardCards.insert(67, card)
                card = Card("Hearts", 5)
                self.boardCards.insert(68, card)
                card = Card("Diamonds", 3)
                self.boardCards.insert(69, card)

# 7 row complete from top

                card = Card("Clubs", "King")
                self.boardCards.insert(70, card)
                card = Card("Spades", 8)
                self.boardCards.insert(71, card)
                card = Card("Clubs", 10)
                self.boardCards.insert(72, card)
                card = Card("Clubs", "Queen")
                self.boardCards.insert(73, card)
                card = Card("Clubs", "King")
                self.boardCards.insert(74, card)
                card = Card("Clubs", "Ace")
                self.boardCards.insert(75, card)
                card = Card("Diamonds", "Ace")
                self.boardCards.insert(76, card)
                card = Card("Diamonds", "King")
                self.boardCards.insert(77, card)
                card = Card("Hearts", 4)
                self.boardCards.insert(78, card)
                card = Card("Diamonds", 4)
                self.boardCards.insert(79, card)

# 8 row complete from top

                card = Card("Clubs", "Ace")
                self.boardCards.insert(80, card)
                card = Card("Spades", 7)
                self.boardCards.insert(81, card)
                card = Card("Spades", 6)
                self.boardCards.insert(82, card)
                card = Card("Spades", 5)
                self.boardCards.insert(83, card)
                card = Card("Spades", 4)
                self.boardCards.insert(84, card)
                card = Card("Spades", 3)
                self.boardCards.insert(85, card)
                card = Card("Spades", 2)
                self.boardCards.insert(86, card)
                card = Card("Hearts", 2)
                self.boardCards.insert(87, card)
                card = Card("Hearts", 3)
                self.boardCards.insert(88, card)
                card = Card("Diamonds", 5)
                self.boardCards.insert(89, card)

# 9 row complete from top

                card = Card("Diamonds", "Ace")
                self.boardCards.insert(91, card)
                card = Card("Diamonds", "King")
                self.boardCards.insert(92, card)
                card = Card("Diamonds", "Queen")
                self.boardCards.insert(93, card)
                card = Card("Diamonds", 10)
                self.boardCards.insert(94, card)
                card = Card("Diamonds", 9)
                self.boardCards.insert(95, card)
                card = Card("Diamonds", 8)
                self.boardCards.insert(96, card)
                card = Card("Diamonds", 7)
                self.boardCards.insert(97, card)
                card = Card("Diamonds", 6)
                self.boardCards.insert(98, card)

# 10 row complete from top

# 1.
deck = Deck()

# 2.
deck.build()

# 3.
deck.randomshuffle()

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

