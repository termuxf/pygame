import pygame
class Ship():
    def __init__(self,screen):
        self.screen = screen
        #load
        self.image = pygame.image.load("images/ship.bmp")
        self.scaleimg = pygame.transform.scale(self.image, (60,100))
        self.rect = self.scaleimg.get_rect()
        self.screen_rect = screen.get_rect()
        #put
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #move
        self.moving_right = False
    def blitme(self):
        self.screen.blit(self.scaleimg,self.rect)
    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
