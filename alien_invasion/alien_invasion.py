import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings,screen,stats)

    play_button = Button(ai_settings,screen,"Play")

    ship = Ship(ai_settings,screen)
    bullets = Group()
    
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True:

        # monitor mouse and keyboard activities
        gf.check_events(ai_settings,stats,sb,screen,ship,aliens,bullets,play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,stats,sb,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        
        # re-draw screen in every cycle
        gf.update_screen(ai_settings,stats,sb,screen,ship,aliens,bullets,play_button)

    

run_game()