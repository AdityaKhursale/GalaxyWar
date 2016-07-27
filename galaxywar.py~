import pygame
from ship import Ship
from alien import Alien
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from pygame.sprite import Group
from button import Button
from score import ScoreBoard

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("GalaxyWar by Aditya") 
    play_button = Button(settings, screen, "Play")
    ship = Ship(settings,screen)
    alien = Alien(screen,settings) 
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings,screen,aliens)
    stats = GameStats(settings)
    sb = ScoreBoard(settings, screen, stats)
    while True:
        gf.check_events(ship,settings,screen,bullets,stats,play_button,aliens,sb)  
        
        if stats.game_active:
            ship.update_ship()  
            gf.update_bullets(bullets,aliens,screen,ship,settings,alien,sb,stats)  
            gf.update_aliens(aliens,settings,ship,stats,screen,bullets,sb)                  
        
        gf.update_screen(settings,ship,screen,bullets,aliens,play_button,stats,sb)      
                    
run_game()
