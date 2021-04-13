import arcade
from arcade import SpriteList
from pyramid import *


SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Pyramid: Best Game (The Dream !)"

# Constants for sizing
#CARD_SCALE = 0.2

# How big are the cards?
CARD_WIDTH = 330 * CARD_SCALE
CARD_HEIGHT = 600 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.20
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

# Mat positions for the pyramyd
TOP_Y_B1_1 = SCREEN_HEIGHT - MAT_HEIGHT / 2 - (MAT_HEIGHT / VERTICAL_MARGIN_PERCENT) * 0.05
LATERAL_X_B1_1 = SCREEN_WIDTH / 2 - MAT_WIDTH / 2

TOP_Y_B2_1 = TOP_Y_B1_1 - MAT_HEIGHT / 1.5
LATERAL_X_B2_1 = LATERAL_X_B1_1 - (MAT_WIDTH / 2) * 1.25

TOP_Y_B2_2 = TOP_Y_B2_1
LATERAL_X_B2_2 = LATERAL_X_B2_1 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B3_1 = TOP_Y_B2_1 - MAT_HEIGHT / 1.5
LATERAL_X_B3_1 = LATERAL_X_B2_1 - (MAT_WIDTH / 2) * 1.25

TOP_Y_B3_2 = TOP_Y_B3_1
LATERAL_X_B3_2 = LATERAL_X_B3_1 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B3_3 = TOP_Y_B3_1
LATERAL_X_B3_3 = LATERAL_X_B3_2 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B4_1 = TOP_Y_B3_1 - MAT_HEIGHT / 1.5
LATERAL_X_B4_1 = LATERAL_X_B3_1 - (MAT_WIDTH / 2) * 1.25

TOP_Y_B4_2 = TOP_Y_B4_1
LATERAL_X_B4_2 = LATERAL_X_B4_1 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B4_3 = TOP_Y_B4_1
LATERAL_X_B4_3 = LATERAL_X_B4_2 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B4_4 = TOP_Y_B4_1
LATERAL_X_B4_4 = LATERAL_X_B4_3 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B5_1 = TOP_Y_B4_1 - MAT_HEIGHT / 1.5
LATERAL_X_B5_1 = LATERAL_X_B4_1 - (MAT_WIDTH / 2) * 1.25

TOP_Y_B5_2 = TOP_Y_B5_1
LATERAL_X_B5_2 = LATERAL_X_B5_1 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B5_3 = TOP_Y_B5_1
LATERAL_X_B5_3 = LATERAL_X_B5_2 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B5_4 = TOP_Y_B5_1
LATERAL_X_B5_4 = LATERAL_X_B5_3 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B5_5 = TOP_Y_B5_1
LATERAL_X_B5_5 = LATERAL_X_B5_4 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B6_1 = TOP_Y_B5_1 - MAT_HEIGHT / 1.5
LATERAL_X_B6_1 = LATERAL_X_B5_1 - (MAT_WIDTH / 2) * 1.25

TOP_Y_B6_2 = TOP_Y_B6_1
LATERAL_X_B6_2 = LATERAL_X_B6_1 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B6_3 = TOP_Y_B6_1
LATERAL_X_B6_3 = LATERAL_X_B6_2 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B6_4 = TOP_Y_B6_1
LATERAL_X_B6_4 = LATERAL_X_B6_3 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B6_5 = TOP_Y_B6_1
LATERAL_X_B6_5 = LATERAL_X_B6_4 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_B6_6 = TOP_Y_B6_1
LATERAL_X_B6_6 = LATERAL_X_B6_5 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_UB7_1 = TOP_Y_B6_1 - MAT_HEIGHT / 1.5
LATERAL_X_UB7_1 = LATERAL_X_B6_1 - (MAT_WIDTH / 2) * 1.25

TOP_Y_UB7_2 = TOP_Y_UB7_1
LATERAL_X_UB7_2 = LATERAL_X_UB7_1 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_UB7_3 = TOP_Y_UB7_1
LATERAL_X_UB7_3 = LATERAL_X_UB7_2 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_UB7_4 = TOP_Y_UB7_1
LATERAL_X_UB7_4 = LATERAL_X_UB7_3 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_UB7_5 = TOP_Y_UB7_1
LATERAL_X_UB7_5 = LATERAL_X_UB7_4 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_UB7_6 = TOP_Y_UB7_1
LATERAL_X_UB7_6 = LATERAL_X_UB7_5 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_UB7_7 = TOP_Y_UB7_1
LATERAL_X_UB7_7 = LATERAL_X_UB7_6 + MAT_WIDTH + (CARD_WIDTH * 0.15)

TOP_Y_AD_1 = BOTTOM_Y + VERTICAL_MARGIN_PERCENT + MAT_HEIGHT
LATERAL_X_AD_1 = START_X

TOP_Y_AD_2 = TOP_Y_AD_1 + VERTICAL_MARGIN_PERCENT + MAT_HEIGHT
LATERAL_X_AD_2 = START_X

TOP_Y_AD_3 = TOP_Y_AD_2 + VERTICAL_MARGIN_PERCENT + MAT_HEIGHT
LATERAL_X_AD_3 = START_X

TOP_Y_AD_4 = TOP_Y_AD_3 + VERTICAL_MARGIN_PERCENT + MAT_HEIGHT
LATERAL_X_AD_4 = START_X

TOP_Y_PAIRED = 90
LATERAL_X_PAIRED = 1000



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
        self.cards = [Card(v, s) for v in value for s in suits]
        self.deck = Deck(self.cards)
        self.deck.initial_deck = arcade.SpriteList()
        self.deck.add_cards(value, suits)
        #self.deck.shuffle_deck() to be fixed
        self.board = Board(self.deck, self.cards)
        self.board.placing_cards(self.deck)
        self.board.assign_position(self.deck)

        self.covered_pyramid_sprites = arcade.SpriteList()
        self.covered_pyramid_sprites.extend(self.board.covered_cards_in_pyramid)

        self.uncovered_pyramid_sprites = arcade.SpriteList()
        self.uncovered_pyramid_sprites.extend(self.board.uncovered_cards_in_pyramid)

        self.paired_cards = arcade.SpriteList()






        # Sprite list with all the mats for card positioning
        self.card_position_mat_list: arcade.SpriteList = arcade.SpriteList()
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_2_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_2_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_3_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_3_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_3_3 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_4_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_4_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_4_3 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_4_4 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_5_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_5_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_5_3 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_5_4 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_5_5 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_6_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_6_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_6_3 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_6_4 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_6_5 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_6_6 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_3 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_4 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_5 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_6 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_6 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_7_7 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)

        pile_ad_1 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_ad_2 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_ad_3 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile_ad_4 = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)

        pile.position = LATERAL_X_B1_1, TOP_Y_B1_1
        pile_2_1.position = LATERAL_X_B2_1, TOP_Y_B2_1
        pile_2_2.position = LATERAL_X_B2_2, TOP_Y_B2_2
        pile_3_1.position = LATERAL_X_B3_1, TOP_Y_B3_1
        pile_3_2.position = LATERAL_X_B3_2, TOP_Y_B3_2
        pile_3_3.position = LATERAL_X_B3_3, TOP_Y_B3_3
        pile_4_1.position = LATERAL_X_B4_1, TOP_Y_B4_1
        pile_4_2.position = LATERAL_X_B4_2, TOP_Y_B4_2
        pile_4_3.position = LATERAL_X_B4_3, TOP_Y_B4_3
        pile_4_4.position = LATERAL_X_B4_4, TOP_Y_B4_4
        pile_5_1.position = LATERAL_X_B5_1, TOP_Y_B5_1
        pile_5_2.position = LATERAL_X_B5_2, TOP_Y_B5_2
        pile_5_3.position = LATERAL_X_B5_3, TOP_Y_B5_3
        pile_5_4.position = LATERAL_X_B5_4, TOP_Y_B5_4
        pile_5_5.position = LATERAL_X_B5_5, TOP_Y_B5_5
        pile_6_1.position = LATERAL_X_B6_1, TOP_Y_B6_1
        pile_6_2.position = LATERAL_X_B6_2, TOP_Y_B6_2
        pile_6_3.position = LATERAL_X_B6_3, TOP_Y_B6_3
        pile_6_4.position = LATERAL_X_B6_4, TOP_Y_B6_4
        pile_6_5.position = LATERAL_X_B6_5, TOP_Y_B6_5
        pile_6_6.position = LATERAL_X_B6_6, TOP_Y_B6_6

        pile_7_1.position = LATERAL_X_UB7_1, TOP_Y_UB7_1
        pile_7_2.position = LATERAL_X_UB7_2, TOP_Y_UB7_2
        pile_7_3.position = LATERAL_X_UB7_3, TOP_Y_UB7_3
        pile_7_4.position = LATERAL_X_UB7_4, TOP_Y_UB7_4
        pile_7_5.position = LATERAL_X_UB7_5, TOP_Y_UB7_5
        pile_7_6.position = LATERAL_X_UB7_6, TOP_Y_UB7_6
        pile_7_7.position = LATERAL_X_UB7_7, TOP_Y_UB7_7

        pile_ad_1.position = LATERAL_X_AD_1, TOP_Y_AD_1
        pile_ad_2.position = LATERAL_X_AD_2, TOP_Y_AD_2
        pile_ad_3.position = LATERAL_X_AD_3, TOP_Y_AD_3
        pile_ad_4.position = LATERAL_X_AD_4, TOP_Y_AD_4

        self.card_position_mat_list.append(pile)
        self.card_position_mat_list.append(pile_2_1)
        self.card_position_mat_list.append(pile_2_2)
        self.card_position_mat_list.append(pile_3_1)
        self.card_position_mat_list.append(pile_3_2)
        self.card_position_mat_list.append(pile_3_3)
        self.card_position_mat_list.append(pile_4_1)
        self.card_position_mat_list.append(pile_4_2)
        self.card_position_mat_list.append(pile_4_3)
        self.card_position_mat_list.append(pile_4_4)
        self.card_position_mat_list.append(pile_5_1)
        self.card_position_mat_list.append(pile_5_2)
        self.card_position_mat_list.append(pile_5_3)
        self.card_position_mat_list.append(pile_5_4)
        self.card_position_mat_list.append(pile_5_5)
        self.card_position_mat_list.append(pile_6_1)
        self.card_position_mat_list.append(pile_6_2)
        self.card_position_mat_list.append(pile_6_3)
        self.card_position_mat_list.append(pile_6_4)
        self.card_position_mat_list.append(pile_6_5)
        self.card_position_mat_list.append(pile_6_6)
        self.card_position_mat_list.append(pile_7_1)
        self.card_position_mat_list.append(pile_7_2)
        self.card_position_mat_list.append(pile_7_3)
        self.card_position_mat_list.append(pile_7_4)
        self.card_position_mat_list.append(pile_7_5)
        self.card_position_mat_list.append(pile_7_6)
        self.card_position_mat_list.append(pile_7_7)

        self.card_position_mat_list.append(pile_ad_1)
        self.card_position_mat_list.append(pile_ad_2)
        self.card_position_mat_list.append(pile_ad_3)
        self.card_position_mat_list.append(pile_ad_4)

        self.covered_pyramid_sprites[0].position = pile.position
        self.covered_pyramid_sprites[1].position = pile_2_1.position
        self.covered_pyramid_sprites[2].position = pile_2_2.position
        self.covered_pyramid_sprites[3].position = pile_3_1.position
        self.covered_pyramid_sprites[4].position = pile_3_2.position
        self.covered_pyramid_sprites[5].position = pile_3_3.position
        self.covered_pyramid_sprites[6].position = pile_4_1.position
        self.covered_pyramid_sprites[7].position = pile_4_2.position
        self.covered_pyramid_sprites[8].position = pile_4_3.position
        self.covered_pyramid_sprites[9].position = pile_4_4.position
        self.covered_pyramid_sprites[10].position = pile_5_1.position
        self.covered_pyramid_sprites[11].position = pile_5_2.position
        self.covered_pyramid_sprites[12].position = pile_5_3.position
        self.covered_pyramid_sprites[13].position = pile_5_4.position
        self.covered_pyramid_sprites[14].position = pile_5_5.position
        self.covered_pyramid_sprites[15].position = pile_6_1.position
        self.covered_pyramid_sprites[16].position = pile_6_2.position
        self.covered_pyramid_sprites[17].position = pile_6_3.position
        self.covered_pyramid_sprites[18].position = pile_6_4.position
        self.covered_pyramid_sprites[19].position = pile_6_5.position
        self.covered_pyramid_sprites[20].position = pile_6_6.position

        self.uncovered_pyramid_sprites[0].position = pile_7_1.position
        self.uncovered_pyramid_sprites[1].position = pile_7_2.position
        self.uncovered_pyramid_sprites[2].position = pile_7_3.position
        self.uncovered_pyramid_sprites[3].position = pile_7_4.position
        self.uncovered_pyramid_sprites[4].position = pile_7_5.position
        self.uncovered_pyramid_sprites[5].position = pile_7_6.position
        self.uncovered_pyramid_sprites[6].position = pile_7_7.position


        #self.board.pyramid_board['B1.1'].position = pile.position
        #self.board.covered_cards_in_pyramid.append(self.board.pyramid_board['B1.1'])

    def on_draw(self):
        # clear the screen
        arcade.start_render()
        # Draw the mats for card positioning
        self.card_position_mat_list.draw()
        #draw cards
        self.deck.initial_deck.draw()
        #self.board.covered_cards_in_pyramid.draw()
        self.covered_pyramid_sprites.draw()
        self.uncovered_pyramid_sprites.draw()

        self.paired_cards.draw()


    def on_mouse_press(self, x, y, button, key_modifiers):
        print(len(self.uncovered_pyramid_sprites), 'in uncovered_pyramid_sprites')
        print(len(self.board.uncovered_cards_in_pyramid), 'in uncovered cards in pyramid')
        #pass
        selection = arcade.get_sprites_at_point((x, y), self.uncovered_pyramid_sprites)
        self.board.selected_cards.append(selection[-1])
        print(self.board.selected_cards[-1].position_in_list)
        print(len(self.board.selected_cards), 'items in selected list')
        print(self.board.selected_cards, 'selected card')
        print(self.uncovered_pyramid_sprites[0], 'first acrd in list')
        print(self.uncovered_pyramid_sprites[0].value)
        print(self.board.selected_cards[-1].value)
        for card in self.board.selected_cards:
            print(card.value, 'value of item selected')


    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):

        if len(self.board.selected_cards) <= 2:
            self.board.cards_value_check(self.board)
            if self.board.checked_value == True:
                print(len(self.board.paired_cards), 'in board paired cards')
                print(self.board.checked_value)
                for Card in self.board.paired_cards: #execute the following line only if value check is positive (idea use true false)
                    Card.set_position(LATERAL_X_PAIRED, TOP_Y_PAIRED)
                    #Card.self.uncovered_pyramid_sprites.pop()
                self.board.checked_value = False
                print(self.board.checked_value)
                    #Card.update_location() needed ?

        else:
            self.board.selected_cards = []


        print(len(self.uncovered_pyramid_sprites), 'in uncovered_pyramid_sprites')
        print(len(self.board.uncovered_cards_in_pyramid), 'in uncovered cards in pyramid')

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
