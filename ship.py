import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,settings,screen):
        self.screen = screen
        super(Ship, self).__init__()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
    def update_ship(self):
        if self.move_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1 
        if self.move_left == True and self.rect.left > 0:
            self.rect.centerx -= 1   
            
    def center_ship(self):
        self.center = self.screen_rect.centerx
        
