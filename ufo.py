import pygame
from pygame.sprite import Sprite


class Ufo(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ufo image
        self.image = pygame.image.load("images/ufo.bmp").convert_alpha()
        self.rect = self.image.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height
        self.image = pygame.transform.scale(self.image,(self.w * 0.1,self.h * 0.1))
        self.rect = self.image.get_rect()
        

        #start each alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the exact position of the ufo
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw the alien at the current position
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """Move the alien right."""
        self.x += (self.ai_settings.ufo_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

