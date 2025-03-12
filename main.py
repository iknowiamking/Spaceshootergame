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
    ufo = Ufo(ai_settings,screen)
    #gf.create_fleet(ai_settings,screen,ufos)

    clock = pygame.time.Clock()

    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while True:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # fill the screen with a color to wipe away anything from last frame
        gf.update_screen(ai_settings,screen,ship,ufo,bullets)


        """pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt"""


        pygame.display.flip()
        
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

run_game()
