import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """ initialize the ship's setting and its original place"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship's image and the outside rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set every new ship at the screen's center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # make the ship's setting can sotre float
        self.center = float(self.rect.centerx)
    

        #moving signal
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust the ship's position based on the moving signal"""
        # upade the center value not the rect value
        if self.moving_right and self.rect.right < self.screen.rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_spped_factor



    def blitme(self):
        """draw a ship at a pointed place"""
        self.screen.blit(self.image, self.rect)