class Settings:
    def __init__(self):
        """Initializes the game settings"""
        #Screen Settings
        self.screen_width = 1000
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3