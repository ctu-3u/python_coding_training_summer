import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:

        # monitor mouse and keyboard activities
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # re-draw screen in every cycle
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

    

run_game()