import arcade
from arcade import SpriteList
from pyramid import *


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Pyramid: Best Game (The Dream !)"

# Constants for sizing
CARD_SCALE = 0.2

# How big are the cards?
CARD_WIDTH = 40 * CARD_SCALE
CARD_HEIGHT = 90 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# Mat positions for the pyramyd
TOP_Y_B1_1 = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT
LATERAL_X_B1_1 = SCREEN_WIDTH / 2 - MAT_WIDTH / 2


# Card constants
suits = ["Ori", "Spade", "Coppe", "Bastoni"]
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class pyramid_game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)
        self.card_position_mat_list = []




    def setup(self):
        "function that starts the game"
        #Deck.initial_deck = arcade.Spritelist()
        # understand how to use method in deck class that creates card and apply to this case
        #Deck.initial_deck.add_cards(value, suits) # GIVES AN ERROR BEACUSE WE CALL THE METHOD ON A LIST DEFINIED IN INIT, NOT ON DECK OBJECT, HOW TO FIX ???
        cards = [Card(v, s) for v in value for s in suits]
        self.deck = Deck()
        self.deck.initial_deck = arcade.SpriteList()
        self.deck.add_cards(value, suits)
        #self.deck.shuffle_deck()
        #self.deck.initial_deck = arcade.SpriteList()


        # Sprite list with all the mats for card positioning
        self.card_position_mat_list: arcade.SpriteList = arcade.SpriteList()
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = TOP_Y_B1_1, LATERAL_X_B1_1
        self.card_position_mat_list.append(pile)




    def on_draw(self):
        # clear the screen
        arcade.start_render()
        # Draw the mats for card positioning
        self.card_position_mat_list.draw()
        #draw cards
        self.deck.initial_deck.draw()


    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass


#class Playing_card(Card, arcade.Sprite): #multiple inheritance concept to be checked and fully understood
    # class that inherits from Card class and arcade sprite class
    #def __init__ (self, suit, value, scale=1):

        #self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png" #cards sprites to be created as png

        #super().__init__(self.image_file_name, scale, hit_box_algorithm="None")




def main(): #to be moved after in game file

    #deck = Deck()
    #deck.add_cards(value, suits)
    windows = pyramid_game()
    windows.setup()
    arcade.run()


main()
