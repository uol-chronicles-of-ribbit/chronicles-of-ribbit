import pygame
from Constants import Constants as const
from Sprite import Sprite
from character import Character
from random import choice, randint


# basics of jumping is commented out for now unless we add later
class Enemy(Character):

    def __init__(self, x=const.SCREEN_W -100 + randint(1, 100), y=const.SCREEN_H *1 // 3, speed=const.PLAYER_SPEED):
        #TODO: update sprites
        super().__init__(x, y, speed,
                         Sprite([pygame.image.load("images/Fox-idle-front.png"), pygame.image.load("images/Fox-idle-front.png")],     #standing
                                [pygame.image.load("images/Fox-idle-left.png"), pygame.image.load("images/Fox-idle-left.png")],     #left
                                [pygame.image.load("images/Fox-idle-right.png"), pygame.image.load("images/Fox-idle-right.png")],     #right
                                [pygame.image.load("images/Fox-idle-front.png"), pygame.image.load("images/Fox-idle-front.png")],     #up
                                [pygame.image.load("images/Fox-idle-front.png"), pygame.image.load("images/Fox-idle-front.png")]))    #down
        self.state = -1 # 1: moving right, -1 moving left


    def move(self):
        # check if on border
        if self.x <= const.TILE_SIZE:
            self.state = 1
        elif self.x >= const.SCREEN_H - const.TILE_SIZE - self.height:
            self.state = -1

        # move in direction
        if self.state == 1:
            self.move_right()
        else:
            self.move_left()
