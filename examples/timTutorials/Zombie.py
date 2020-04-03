import pygame
from Constants import Constants
from MovingObject import SpriteObject

ZOMBIE_SPRITE_STANDING_I = 0
ZOMBIE_SPRITE_STANDING_J = 0
ZOMBIE_SPRITE_LEFT_J = 2
ZOMBIE_SPRITE_RIGHT_J = 2
ZOMBIE_SPRITE_FRAMES = 4


class Zombie(SpriteObject):
    ZOMBIE_SPRITE_W = 48
    ZOMBIE_SPRITE_H = 50

    def __init__(self, x, y, speed):
        super().__init__(x, y, speed, pygame.image.load("images/zombie-sprite.png"), 0, 0,
                         Zombie.ZOMBIE_SPRITE_W, Zombie.ZOMBIE_SPRITE_H,
                         ZOMBIE_SPRITE_STANDING_I, ZOMBIE_SPRITE_STANDING_J,
                         ZOMBIE_SPRITE_LEFT_J, ZOMBIE_SPRITE_RIGHT_J, ZOMBIE_SPRITE_FRAMES)
        self.isJumping = False
        self.jumpCount = 10

    # just have zombie move right across the screen and then begin again other side
    def move(self):
        self.move_right()
        self.advance_animation()

        if self.x == Constants.SCREEN_W - self.sprite_w:
            self.x = -self.sprite_w

