class Settings:
    def __init__(self):
        """Initializes the game settings"""
        #Screen Settings
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        #ufo settings
        
        self.fleet_drop_speed = 10
        #stats
        self.ship_limit = 3

        #level up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 6
        self.bullet_speed_factor = 10
        self.ufo_speed_factor = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.ufo_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ufo_speed_factor *= self.speedup_scale
        self.ufo_points = int(self.score_scale * self.ufo_points)
        print(self.ufo_points)