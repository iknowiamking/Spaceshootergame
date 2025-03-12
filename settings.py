class Settings:
    def __init__(self):
        """Initializes the game settings"""
        #Screen Settings
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60