import sys
import pygame
from bullet import Bullet
from alien import Alien
from ship import Ship
from time import sleep

def check_keydown_events(event,ship,screen,settings,bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True    
    elif event.key == pygame.K_SPACE:
       fire_bullets(bullets,settings,ship,screen)
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False

def check_events(ship,settings,screen,bullets,stats,play_button,aliens,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,screen,settings,bullets)      
           
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
           
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings,ship,screen,bullets,aliens,stats, play_button, mouse_x, mouse_y,sb)
            
def check_play_button(settings,ship,screen,bullets,aliens,stats, play_button, mouse_x, mouse_y,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,aliens)
        ship.center_ship()
            
def update_screen(settings,ship,screen,bullets,aliens,play_button,stats,sb):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #alien.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    
def update_bullets(bullets,aliens,screen,ship,settings,alien,sb,stats):
    bullets.update()
        
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(settings, screen, aliens)
            
def fire_bullets(bullets,settings,ship,screen):
     if len(bullets) <= settings.max_bullet_count:
        new_bullet = Bullet(settings, ship, screen)
        bullets.add(new_bullet)
     
def get_number_aliens(settings,screen,alien):
    alien_width = alien.rect.width
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
 
def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height -(3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(settings,screen,aliens,alien_number,row_number):
        alien = Alien(settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)
        
def create_fleet(settings,screen,aliens):
    alien = Alien(settings,screen)
    number_aliens_x = get_number_aliens(settings,screen,alien)
    number_rows = get_number_rows(settings, 48,58)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings,screen,aliens,alien_number,row_number)

def check_alien_edges(aliens,settings):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(aliens,settings)
            break
        
def change_alien_direction(aliens,settings):
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed   
    settings.alien_direction *= (-1)

def update_aliens(aliens,settings,ship,stats,screen,bullets,sb):
    check_alien_edges(aliens,settings)
    aliens.update(settings)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets,sb)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets,sb)
    
def ship_hit(settings, stats, screen, ship, aliens, bullets,sb):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets,sb)
            break
            
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


