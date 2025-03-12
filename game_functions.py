import sys
import pygame
from bullet import Bullet
from ufo import Ufo

def check_events(ai_settings, screen, ship, bullets):
    """Respond to key movements"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
            # Move the ship to the right.
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
            # Move the ship to the right.
                ship.moving_left = True
            elif event.key == pygame.K_SPACE:
                # Create a new bullet and add it to the bullets group.
                if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
            # Move the ship to the right.
                ship.moving_left = False
        

def update_screen(ai_settings , screen , ship, ufos, bullets):
    """Update the current screen"""

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ufos.draw(screen)
    # Make the most recently drawn screen visible.
    pygame.display.flip()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings,screen,ship,ufos):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    ufo = Ufo(ai_settings,screen)
    ufo_width = ufo.rect.width
    ufo_height = ufo.rect.height
    available_space_x = ai_settings.screen_width  - (2 * ufo_width)
    available_space_y = ai_settings.screen_height  - (3 * ufo_height) - ship.rect.height
    number_ufos_x = int(available_space_x/(2*ufo_width))
    number_rows = int(available_space_y  / (2*ufo_height)) - 2

    #Create first row of ufos
    for ufo_row_number in range(number_rows):
        for ufo_col_number in range(number_ufos_x):
    # Create an alien and place it in the row.
            ufo = Ufo(ai_settings, screen)
            ufo.x = ufo_width + 2 * ufo_width * ufo_col_number
            y = ufo_height + 2 * ufo_height * ufo_row_number
            ufo.rect.x = ufo.x
            ufo.rect.y = y
            ufos.add(ufo)

def update_ufos(ai_settings,ufos): 
    """Update the postions of all aliens in the fleet."""
    check_fleet_edges(ai_settings,ufos)
    ufos.update()


def check_fleet_edges(ai_settings, ufos):
    """Respond appropriately if any aliens have reached an edge."""
    for ufo in ufos.sprites():
        if ufo.check_edges():
            change_fleet_direction(ai_settings, ufos)
            break

def change_fleet_direction(ai_settings, ufos):
    """Drop the entire fleet and change the fleet's direction."""
    
    for ufo in ufos.sprites():
        ufo.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    print("fleetdirection = ",ai_settings.fleet_direction)

    