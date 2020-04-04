import pygame
from Constants import Constants as const
from Sprite import Sprite
from character import Character
from random import randint, choice as random_choice

ENEMY_RANDOM_CHANGE_TICKS = 30

# basics of jumping is commented out for now unless we add later
class Enemy(Character):

    TYPE_FOX = 1
    TYPE_MUSHROOM = 2
    MONSTER_CHOICES = [TYPE_FOX, TYPE_MUSHROOM]
    MONSTER_SPRITES = {
        TYPE_FOX: {
            'front': 'images/Fox-idle-front.png',
            'left': 'images/Fox-idle-left.png',
            'right': 'images/Fox-idle-right.png',
        },
        TYPE_MUSHROOM: {
            'front': 'images/mushroom-front.png',
            'left': 'images/mushroom-left.png',
            'right': 'images/mushroom-right.png',
        }
    }

    def __init__(self, x=const.SCREEN_W // 2, y=const.SCREEN_H * 1 // 3, speed=const.ENEMY_SPEED, monster=None):
        #TODO: update sprites
        self.monster = random_choice(self.MONSTER_CHOICES)
        sprites = self.MONSTER_SPRITES[self.monster]

        super().__init__(x, y, speed,
                         Sprite([pygame.image.load(sprites['front']), pygame.image.load(sprites['front'])],     #standing
                                [pygame.image.load(sprites['left']), pygame.image.load(sprites['left'])],     #left
                                [pygame.image.load(sprites['right']), pygame.image.load(sprites['right'])],     #right
                                [pygame.image.load(sprites['front']), pygame.image.load(sprites['front'])],     #up
                                [pygame.image.load(sprites['front']), pygame.image.load(sprites['front'])]))    #down
        self.state = randint(0, 3)
        self.move_tick = 0

    def respawn(self):
        #TODO: add cool down period?
        self.x = randint(const.TILE_SIZE, const.SCREEN_W - const.TILE_SIZE - self.width)
        self.y = randint(const.TILE_SIZE, const.SCREEN_H - const.TILE_SIZE - self.height)

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
