import pygame
from settings import Settings
from ship import Ship
from ufo import Ufo
import game_functions as gf
from pygame.sprite import Group

# pygame setup
def run_game():

    #Settings object
    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #Ship object
    ship = Ship(screen)
    bullets = Group()
    ufos = Group()
    gf.create_fleet(ai_settings,screen,ship,ufos)

    clock = pygame.time.Clock()

    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_ufos(ai_settings,ufos)
        # fill the screen with a color to wipe away anything from last frame
        gf.update_screen(ai_settings,screen,ship,ufos,bullets)
        pygame.display.flip()
        
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

run_game()
