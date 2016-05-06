# coding=utf-8
import itertools
import random




class Deck(object):
    game = {"Player 1":[], "Dealer":[]}



    def __init__(self):
        self.suits = self.SUITS()
        self.ranks = self.RANKS()
        self.cards = sorted(self.CARDS(), key=lambda k: random.random())



    @staticmethod
    def SUITS():
        return {
            'Spades': '♠',
            'Diamonds': '♦',
            'Hearts': '♥',
            'Clubs': '♣',
        }

    @staticmethod
    def RANKS():
        return {
            'Ace': 11,  # value of the ace is high until it needs to be low
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10
        }

    @staticmethod
    def CARDS():
        return [Card(card[0], card[1]) for card in itertools.product(Deck.SUITS(), Deck.RANKS())]

    def join_lines(self, strings):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [string.splitlines() for string in strings]
        return '\n'.join(''.join(lines) for lines in zip(*liness))

    def face_down(self, cards):
        """
        Essentially the dealers method of print ascii cards. This method hides the first card, shows it flipped over
        :param cards: A list of card objects, the first will be hidden
        :return: A string, the nice ascii version of cards
        """

        def card_to_string(card):
            # add the individual card on a line by line basis
            return card.hidden_card()  # Card.PLAYINGCARD().format(rank=rank, suit=Deck.SUITS()[card.suit])

        return self.join_lines(map(card_to_string, cards))


    def face_up(self, cards):
        """
        Instead of a boring text version of the card we render an ASCII image of the card.
        :param cards: One or more card objects
        :return: A string, the nice ascii version of cards
        """


        def card_to_string(card):
            # add the individual card on a line by line basis
            return card.card()  # Card.PLAYINGCARD().format(rank=rank, suit=Deck.SUITS()[card.suit])


        return self.join_lines(map(card_to_string, cards))

    def player_deal(self):
        for player in self.game:
            self.game[player].append(self.cards.pop())

    def deal(self):

        for i in range(5):
            if i < 5:
                self.player_deal()


class Card(object):
    def __repr__(self):
        return "<Card %s %s>" % (self.rank, self.suit)


    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = Deck.RANKS()[rank]

    def card(self):

        ranknum = self.rank == "10" and 2 or 1

        return self.PLAYINGCARD().format(rank=self.rank[:ranknum], suit=Deck.SUITS()[self.suit])

    def hidden_card(self):
        ranknum = self.rank == "10" and 2 or 1

        return self.HIDDEN_PLAYINGCARD()

    @staticmethod
    def PLAYINGCARD():
        return """\
┌─────────┐
│ {}      │
│         │
│         │
│    {}    │
│         │
│         │
│      {} │
└─────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')

    @staticmethod
    def HIDDEN_PLAYINGCARD():
        return """\
┌─────────┐
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
│░░░░░░░░░│
└─────────┘
"""



#print Deck.CARDS()
deck = Deck()
deck.deal()

for player in deck.game:
    if player:
        print player
        print "========================="
        if player == "Dealer":
            print deck.face_down(deck.game[player])
        else:
            print deck.face_up(deck.game[player])

print len(deck.cards)
# print deck.face_up(Deck.CARDS()[:10])

#print(ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))

# for card in Deck.CARDS():
#     print card.card()