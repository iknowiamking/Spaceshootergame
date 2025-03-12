import sys
import pygame
from bullet import Bullet

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
        

def update_screen(ai_settings , screen , ship, ufo, bullets):
    """Update the current screen"""

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ufo.blitme()
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