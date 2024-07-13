import sys

import pygame

from bullet import Bullet
from alien import Alien

# monitor events

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)

    elif event.type == pygame.K_q:
        sys.exit()
        pygame.quit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

# bullets operation

def fire_bullets(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

# aliens motion

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_aliens_rows(ai_settings,ship_height,alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_aliens_rows = int(available_space_y / (2 * alien_height))
    return number_aliens_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien.x = alien.rect.width + 2 * alien_number * alien.rect.width
    alien.y = alien.rect.height + 2 * row_number * alien.rect.height
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_aliens_row = get_number_aliens_rows(ai_settings,ship.rect.height,alien.rect.height)

    for row_number in range(number_aliens_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
        

def update_aliens(aliens):
    aliens.update()

# update screen

def update_screen(ai_settings,screen,ship,aliens,bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()