import pygame as pg
from settings import Settings
import game_functions as gf

from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
import sys

#tried getting the menu class to work
# class Button():
# 	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
# 		self.image = image
# 		self.x_pos = pos[0]
# 		self.y_pos = pos[1]
# 		self.font = font
# 		self.base_color, self.hovering_color = base_color, hovering_color
# 		self.text_input = text_input
# 		self.text = self.font.render(self.text_input, True, self.base_color)
# 		if self.image is None:
# 			self.image = self.text
# 		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
# 		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

# 	def update(self, screen):
# 		if self.image is not None:
# 			screen.blit(self.image, self.rect)
# 		screen.blit(self.text, self.text_rect)

# 	def checkForInput(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			return True
# 		return False

# 	def changeColor(self, position):
# 		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
# 			self.text = self.font.render(self.text_input, True, self.hovering_color)
# 		else:
# 			self.text = self.font.render(self.text_input, True, self.base_color)

# def get_font(size):
#     return pg.font.Font("images/font.ttf", size)

# class Menu():
#     def __init__(self, game):
#         self.game = game
#         self.settings = Settings()
#         self.mid_w, self.mid_h = self.game.settings.screen_width / 2, self.game.settings.screen_height / 2
#         self.run_display = True
#         self.cursor_rect = pg.Rect(0, 0, 20, 20)
#         self.offset = - 100

#     def draw_cursor(self):
#         self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

#     def blit_screen(self):
#         self.game.window.blit(self.game.display, (0,0))
#         pg.display.update()
#         self.game.reset_keys()

# class MainMenu(Menu):
#     def __init__(self, game):
#         Menu.__init__(self, game)
#         self.state = "Start"
#         self.settings = Settings()
#         self.startx, self.starty = self.mid_w, self.mid_h + 30
#         self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
#         self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
#         self.cursor_rect.midtop = (self.startx +self.offset, self.starty)

#     def display_menu(self):
#         self.run_display = True
#         while self.run_display:
#             self.game.check_menu()
#             self.game.display.fill(self.game.BLACK)
#             self.game.draw_text('Main Menu', 20, self.settings.screen_width / 2, self.settings.screen_width / 2 - 20)
#             self.game.draw_text('Start Game', 20, self.startx, self.starty)
#             self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
#             self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
#             self.draw_cursor()

#     def move_cursor(self):
#         if self.game.DOWN_KEY:
#             if self.state == 'Start':
#                 self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
#                 self.state = 'Options'
#             elif self.state == 'Options':
#                 self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
#                 self.state = 'Credits'
#             elif self.state == 'Credits':
#                 self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
#                 self.state = 'Start'
#             elif self.game.UP_KEY:
#                 if self.state == 'Start':
#                     self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
#                     self.state = 'Credits'
#                 elif self.state == 'Options':
#                     self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
#                     self.state = 'Start'
#                 elif self.state == 'Credits':
#                     self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
#                     self.state = 'Options'

#     def check_input(self):
#         self.move_cursor()
#         if self.game.START_KEY:
#             if self.state == 'Start':
#                 self.game.playing = True
#             elif self.state == 'Options':
#                 self.game.curr_menu = self.game.options
#             elif self.state == 'Credits':
#                 self.game.curr_menu = self.game.credits
#             self.run_display = False

# class OptionsMenu(Menu):
#     def __init__(self, game):
#         Menu.__init__(self, game)
#         self.state = 'Volume'
#         self.volx, self.voly = self.mid_w, self.mid_h + 20
#         self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
#         self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

#     def display_menu(self):
#         self.run_display = True
#         while self.run_display:
#             self.game.check_events()
#             self.check_input()
#             self.game.display.fill((0, 0, 0))
#             self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
#             self.game.draw_text("Volume", 15, self.volx, self.voly)
#             self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
#             self.draw_cursor()
#             self.blit_screen()

#     def check_input(self):
#         if self.game.BACK_KEY:
#             self.game.curr_menu = self.game.main_menu
#             self.run_display = False
#         elif self.game.UP_KEY or self.game.DOWN_KEY:
#             if self.state == 'Volume':
#                 self.state = 'Controls'
#                 self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
#             elif self.state == 'Controls':
#                 self.state = 'Volume'
#                 self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
#         elif self.game.START_KEY:
#             self.game.play()
            

# class CreditsMenu(Menu):

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.sound = Sound(bg_music="sounds/startrek.wav")
        self.scoreboard = Scoreboard(game=self)  

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.settings.initialize_speed_settings()

         #     ##trying to create the main menu screen
    #     self.running, self.playing = True, False
    #     self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    #     self.window = self.screen
    #     self.display = pg.Surface((self.settings.screen_width, self.settings.screen_height))
    #     self.font_name = "images/font.TTF"
    #     self.BLACK, self.WHITE = (0,0,0), (255,255,255)

    # ##in main it will check the inputs of the user and determine whether to start game or exit
    # def check_menu(self):
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             self.running, self.playing = False, False
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_RETURN:
    #                 self.START_KEY = True
    #             if event.key == pg.K_BACKSPACE:
    #                 self.BACK_KEY = True
    #             if event.key == pg.K_DOWN:
    #                 self.DOWN_KEY = True
    #             if event.key == pg.K_UP:
    #                 self.UP_KEY = True

    ##once a cycle ends the keys will be reset             
    # def reset_keys(self):
    #     self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    # def draw_text(self, text, size, x, y):
    #     font = pg.font.Font(self.font_name,size)
    #     text_surface = font.render(text, True, self. WHITE)
    #     text_rect = text_surface.get_rect()
    #     text_rect.center = (x, y)
    #     self.display.blit(text_surface, text_rect)

    def reset(self):
        print('Resetting game...')
        # self.lasers.reset()
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
        # self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        pg.quit()
        sys.exit()

        #def play(self):
        #tried making the main menu
        # while self.playing:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
        #     self.check_menu()
        #     if self.START_KEY:
        #         self.playing = False
            # self.display.fill(self.BLACK)
            # self.draw_text('Thanks For Playing', 20, self.settings.screen_width/2, self.settings.screen_height/2)
        # pg.display.update()
        # self.reset_keys() 

    def play(self):
        self.sound.play_bg()
        while True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.aliens.update()
            self.barriers.update()
            # self.lasers.update()
            self.scoreboard.update()
            pg.display.flip()

        # def main_menu(self):
    #         while True:
    #             self.screen.blit(self.bg_menu, (0, 0))

    #             MENU_MOUSE_POS = pg.mouse.get_pos()

    #             MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
    #             MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    #             PLAY_BUTTON = Button(image=pg.image.load("images/Play Rect.png"), pos=(640, 250), 
    #                                 text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    #             OPTIONS_BUTTON = Button(image=pg.image.load("images/Options Rect.png"), pos=(640, 400), 
    #                                 text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
    #             QUIT_BUTTON = Button(image=pg.image.load("images/Quit Rect.png"), pos=(640, 550), 
    #                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

    #             self.screen.blit(MENU_TEXT, MENU_RECT)

    #             for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
    #                 button.changeColor(MENU_MOUSE_POS)
    #                 button.update(self.screen)
                
    #             for event in pg.event.get():
    #                 if event.type == pg.QUIT:
    #                     pg.quit()
    #                     sys.exit()
    #                 if event.type == pg.MOUSEBUTTONDOWN:
    #                     if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
    #                         self.play()
    #                     if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
    #                         pg.quit()
    #                         sys.exit()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
