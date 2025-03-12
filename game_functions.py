import sys
from time import sleep
import pygame
from bullet import Bullet
from ufo import Ufo

def check_events(ai_settings, screen,stats, play_button,ship,ufos,bullets):
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen,stats, play_button,ship,ufos,bullets, mouse_x, mouse_y)
        

def update_screen(ai_settings , screen ,stats, sb,ship, ufos, bullets,play_button):
    """Update the current screen"""

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ufos.draw(screen)
    sb.show_score()
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(ai_settings,screen,stats,sb,ship,ufos,bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # Check for any bullets that have hit ufos.
    # If so, get rid of the bullet and the ufo.
    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)
    if collisions:
        for ufos in collisions.values():
            stats.score += ai_settings.ufo_points * len(ufos)
        sb.prep_score()
    if len(ufos) == 0:
    # Destroy existing bullets and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, ufos)


def create_fleet(ai_settings,screen,ship,ufos):
    """Create a full fleet of ufos."""
    # Create an ufo and find the number of ufos in a row.
    # Spacing between each ufo is equal to one ufo width.
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
    # Create an ufo and place it in the row.
            ufo = Ufo(ai_settings, screen)
            ufo.x = ufo_width + 2 * ufo_width * ufo_col_number
            y = ufo_height + 2 * ufo_height * ufo_row_number
            ufo.rect.x = ufo.x
            ufo.rect.y = y
            ufos.add(ufo)

def update_ufos(ai_settings,stats,screen,ship,ufos,bullets): 
    """Update the postions of all ufos in the fleet."""
    check_fleet_edges(ai_settings,ufos)

    ufos.update()

    if pygame.sprite.spritecollideany(ship, ufos):
        ship_hit(ai_settings, stats, screen, ship, ufos, bullets)
    
    check_ufos_bottom(ai_settings, stats, screen, ship, ufos, bullets)


def check_fleet_edges(ai_settings, ufos):
    """Respond appropriately if any ufos have reached an edge."""
    for ufo in ufos.sprites():
        if ufo.check_edges():
            change_fleet_direction(ai_settings, ufos)
            break

def change_fleet_direction(ai_settings, ufos):
    """Drop the entire fleet and change the fleet's direction."""
    
    for ufo in ufos.sprites():
        ufo.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def ship_hit(ai_settings, stats, screen, ship, ufos, bullets):
    """Respond to ship being hit by ufo."""
    # Decrement ships_left.
    if stats.ships_left > 0:
        stats.ships_left -= 1

        # Empty the list of ufos and bullets.
        ufos.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, ufos)
        ship.center_ship()

        # Pause.
        sleep(0.5)
    else:
        pygame.mouse.set_visible(True)
        stats.game_active = False

def check_ufos_bottom(ai_settings, stats, screen, ship, ufos, bullets):
    """Check if any ufos have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for ufo in ufos.sprites():
        if ufo.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, ufos, bullets)
            break

def check_play_button(ai_settings, screen,stats, play_button,ship,ufos,bullets,mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # Reset the game statistics.
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        


        # Empty the list of aliens and bullets.
        ufos.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, ufos)
        ship.center_ship()