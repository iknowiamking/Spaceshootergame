class Settings:
    def __init__(self):
        """Initializes the game settings"""
        #Screen Settings
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #ufo settings
        self.ufo_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1