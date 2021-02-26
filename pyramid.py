# we create a class for playing card which will have a value and a suit
suits = ["Denari", "Spade", "Coppe", "Bastoni"]
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import random


#class that create object for cards, with value and suit
class Card(object):

    def __init__(self, value, suit, scale=1):
        self.value = value
        self.suit = suit
        self.covered = True
        self.card_name = f"{self.value} of {self.suit}"

    #Test to print (not working)
    def test(self):
        print(f"{self.value} of {self.suit}") #to understand why ot prints lists of value and suit and not just 1 result for created card

#class that creates a deck as a list
class Deck(object):

    def __init__(self):

        self.initial_deck = []

    #add cards from class Card
    def add_cards(self, value, suit): #function that creates cards, using Class Card
        for v in value:
            for s in suits:
                created_card = Card(v, s) #variable that stores the card
                self.initial_deck.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.initial_deck)

# class that creates the board and pyramid shape
class Board(object):

    def __init__(self, Deck):
        self.covered_cards_in_pyramid = []
        self.uncovered_cards_in_pyramid = []
        self.uncovered_additional_cards = []
        self.pyramid_board = {}

        covered_cards_placeholders = ["B1.1", "B2.1", "B2.2", "B3.1", "B3.2", "B3.3",
                                      "B4.1", "B4.2", "B4.3", "B4.4", "B5.1", "B5.2",
                                      "B5.3", "B5.4", "B5.5", "B6.1", "B6.2", "B6.3",
                                      "B6.4", "B6.5", "B6.6"]
        uncovered_cards_placeholders = ["UB7.1", "UB7.2", "UB7.3", "UB7.4", "UB7.5",
                                        "UB7.6", "UB7.7"]
        for i in covered_cards_placeholders:
            self.covered_cards_in_pyramid.append(Deck.initial_deck.pop())
        for j in uncovered_cards_placeholders:
            self.uncovered_cards_in_pyramid.append(Deck.initial_deck.pop())

        # create dict that match each card to a specific place in the pyramid (B are covered, UB uncovered)
        self.pyramid_board = dict(zip(covered_cards_placeholders+uncovered_cards_placeholders,
                                      self.covered_cards_in_pyramid+self.uncovered_cards_in_pyramid))

        #create the part of deck that will be placed down the pyramid
        self.remaining_deck = Deck.initial_deck


    def turn_cards(self, Card):
        self.pyramid_board['UB7.1'].covered = False
        self.pyramid_board['UB7.2'].covered = False
        self.pyramid_board['UB7.3'].covered = False
        self.pyramid_board['UB7.4'].covered = False
        self.pyramid_board['UB7.5'].covered = False
        self.pyramid_board['UB7.6'].covered = False
        self.pyramid_board['UB7.7'].covered = False

    def additional_cards(self, Card):
        if len(self.remaining_deck) == 0:
            pass
        else:
            self.uncovered_additional_cards.append(self.remaining_deck.pop())


    def test_places(self):
        #print(len(self.initial_deck))
        print(len(self.covered_cards_in_pyramid)) #should print 21 to be correct
        print(len(self.uncovered_cards_in_pyramid)) #should print 7 to be correct
        print(len(self.pyramid_board)) #should print 28 to be correct
        print(self.covered_cards_in_pyramid)
        print(self.uncovered_cards_in_pyramid)
        print(self.pyramid_board)
        print(len(self.remaining_deck)) #should print 12 to be correct
        print(self.remaining_deck)
        print(self.pyramid_board['UB7.1'].covered)
        print(self.pyramid_board['UB7.1'].card_name)
        print(self.remaining_deck[3].card_name)
        print(self.uncovered_additional_cards)


class Game(object):

    def __init__(self):
        # se carte nel dizionario = 0 gioco vinto
        #se > 0 possibilita' di scegliere 2 carte da accoppiare
        pass

    #impplementare funzione che controlla se ci sono mosse possibili

    # come gestire input ?


#create 40 instances of the Card Class and put them into a list
cards = [Card(value, suits) for v in value for s in suits]
#print(cards) #test if cards are in list
#print(len(cards)) #should print 40 to be correct
cards[3].test()
print(',,'*10)
#create an instance for the deck
deck = Deck()
#build the deck
deck.add_cards(value, suits)
#print(deck.initial_deck) #test if cards are in list
#print(len(deck.initial_deck)) #test if correct amount of card was created, should be 40

deck.shuffle_deck()
#print(deck.initial_deck)

board = Board(deck)
board.turn_cards(cards)
board.test_places()
board.additional_cards(cards)
