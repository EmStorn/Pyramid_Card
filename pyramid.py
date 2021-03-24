# we create a class for playing card which will have a value and a suit
suits = ["Ori", "Spade", "Coppe", "Bastoni"]
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Constants for sizing
CARD_SCALE = 0.2

# How big are the cards?
CARD_WIDTH = 330 * CARD_SCALE
CARD_HEIGHT = 600 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.2
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 2
HORIZONTAL_MARGIN_PERCENT = 1

# The Y of the bottom row (2 piles)
BOTTOM_Y = 90 #MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = 50 #MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

import random
import arcade


#class that create object for cards, with value and suit
class Card(arcade.Sprite):

    def __init__(self, value, suit, scale=1):
        self.value = value
        self.suit = suit
        self.covered = True
        self.card_name = f"{self.value} of {self.suit}"
        self.image_file_name = f"images/cards/card{self.value}{self.suit}.png"

        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")

    #Test to print
    def test(self):
        print(f"{self.value} of {self.suit}")

#class that creates a deck as a list
class Deck(object):

    def __init__(self, Card):

        self.initial_deck = []

    #add cards from class Card
    def add_cards(self, value, suit): #function that creates cards, using Class Card
        for v in value:
            for s in suits:
                created_card = Card(v, s, CARD_SCALE) #variable that stores the card
                created_card.position = START_X, BOTTOM_Y
                self.initial_deck.append(created_card)
                print(created_card.value)


    def shuffle_deck(self):
        random.shuffle(self.initial_deck)

# class that creates the board and pyramid shape
class Board(object):

    def __init__(self, Deck, Card):
        self.covered_cards_in_pyramid = []
        self.uncovered_cards_in_pyramid = []
        self.uncovered_additional_cards = []
        self.selected_cards = []
        self.paired_cards = []
        self.pyramid_board = {}

    def placing_cards(self, Deck):

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

    #DEFINE A WAY TO TRACK SELECTED CARDS
    # understand how to use on mouse press and realease function to perform selection and removal/return to original place
    # to remember: rendered card are class aracde sprites (should have .value attribute ?) work from that

    def cards_value_check(self):
        total_value = sum(Card.value for Card in self.selected_cards)
        print(total_value)
        if total_value == 10:
            for card in self.selected_cards:
                self.paired_cards.append(self.selected_cards.pop())
        else:
            pass
            #self.selected_cards = []





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
#cards = [Card(value, suits) for v in value for s in suits]
#print(cards) #test if cards are in list
#print(len(cards)) #should print 40 to be correct
#cards[3].test()
print(',,'*10)
#create an instance for the deck
#deck = Deck()
#build the deck
#deck.add_cards(value, suits)
#print(deck.initial_deck) #test if cards are in list
#print(len(deck.initial_deck)) #test if correct amount of card was created, should be 40

#deck.shuffle_deck()
#print(deck.initial_deck)

#board = Board(deck)
#board.turn_cards(cards)
#board.test_places()
#board.additional_cards(cards)
