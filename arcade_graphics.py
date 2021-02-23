import arcade
import pyramid

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Pyramid: Best Game (The Dream !)"

# Constants for sizing
CARD_SCALE = 0.6

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

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

# Card constants
CARD_VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

class pyramid_game(arcade.Window):

    def __init__(self, Deck):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        Deck.initial_deck = []

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self, Deck):
        "function that starts the game"
        Deck.initial_deck = arcade.Spritelist()
        # understand how to use method in deck class that creates card and apply to this case


    def on_draw(self):
        # clear the screen
        arcade.start_render()

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass


class playing_card(Card, arcade.Sprite): #multiple inheritance concept to be checked and fully understood
    # class that inherits from Card class and arcade sprite class
    def __init__ (self, suit, value, scale=1):

        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png" #cards sprites to be created as png

        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")




def main(): #to be moved after in game file
    windows = pyramid_game()
    windows.setup()
    arcade.run()

main()
