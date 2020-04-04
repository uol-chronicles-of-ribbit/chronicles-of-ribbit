import pygame
from Constants import Constants as const
from Sprite import Sprite
from character import Character
from random import randint

ENEMY_RANDOM_CHANGE_TICKS = 30

# basics of jumping is commented out for now unless we add later
class Enemy(Character):

    def __init__(self, x=const.SCREEN_W // 2, y=const.SCREEN_H * 1 // 3, speed=const.ENEMY_SPEED):
        #TODO: update sprites
        super().__init__(x, y, speed,
                         Sprite([pygame.image.load("images/Fox-idle-front.png"), pygame.image.load("images/Fox-idle-front.png")],     #standing
                                [pygame.image.load("images/Fox-idle-left.png"), pygame.image.load("images/Fox-idle-left.png")],     #left
                                [pygame.image.load("images/Fox-idle-right.png"), pygame.image.load("images/Fox-idle-right.png")],     #right
                                [pygame.image.load("images/Fox-idle-front.png"), pygame.image.load("images/Fox-idle-front.png")],     #up
                                [pygame.image.load("images/Fox-idle-front.png"), pygame.image.load("images/Fox-idle-front.png")]))    #down
        self.state = randint(0, 3)
        self.move_tick = 0

    def move(self):
        # attempt movement first
        if self.state == 0:
            self.move_left()
        elif self.state == 1:
            self.move_up()
        elif self.state == 2:
            self.move_right()
        else:
            self.move_down()

        # check if on border, reverse movement
        if self.x <= const.TILE_SIZE or self.x >= const.SCREEN_W - const.TILE_SIZE - self.width or \
                self.y <= const.TILE_SIZE or self.y >= const.SCREEN_H - const.TILE_SIZE - self.height:
            self.state = (self.state + 2) % 4

        self.move_tick += 1
        if self.move_tick % ENEMY_RANDOM_CHANGE_TICKS == 0:
            self.state = randint(0, 3)
