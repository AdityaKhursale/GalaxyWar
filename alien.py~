import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,screen,settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings
        
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
       
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def check_edges(self):
      #  screen_rect = self.screen.get_rect()
        if self.rect.right >= 1000:
            return True
        elif self.rect.left <= 0:
            return True
            
    def update(self,settings):
        self.x += (settings.alien_speed * settings.alien_direction)
        self.rect.x = self.x
