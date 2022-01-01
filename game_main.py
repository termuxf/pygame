import sys, pygame
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("琉鲸游戏")
    bg_color = (230,230,230)
    #game loop
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,Ship)
run_game()