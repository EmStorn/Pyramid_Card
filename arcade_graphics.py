import arcade
import pyramid

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Pyramid: Best Game (The Dream !)"

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
