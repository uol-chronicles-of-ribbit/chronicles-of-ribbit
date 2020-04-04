import pygame
from Constants import Constants as const


class Character:
    def __init__(self, x=const.SCREEN_W//2, y=const.SCREEN_H//2):
        self.x = x
        self.y = y

        # TO be defined by child class
        self.img = None

        # TODO: upd ate these dynamically from imagesize using functions
        self.width = 16
        self.height = 32

    def draw(self, screen):
        # draw the image on x, y; else draw a red rectangle
        # TODO: consider image size and centre it
        if self.img:
            screen.blit(self.img, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height), 0)

