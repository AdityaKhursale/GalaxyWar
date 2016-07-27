
class Settings():

    def initialize_dynamic_settings(self):
            self.ship_speed = 1.5
            self.bullet_speed = 1
            self.alien_speed = 1
            self.alien_direction = 1    #right
            self.alien_points = 10

    def __init__(self):
    
        #screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)
        
        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.max_bullet_count = 4
        
        #Alien settings
        self.alien_drop_speed = 10       
        
        
        #ship settings
        self.ship_limit = 2
        
        self.speedup_scale = 1.5
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
       
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed  *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
