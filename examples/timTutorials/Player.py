import pygame
from Constants import Constants
from MovingObject import SpriteObject

PLAYER_SPRITE_STANDING_I = 1
PLAYER_SPRITE_STANDING_J = 0
PLAYER_SPRITE_LEFT_J = 2
PLAYER_SPRITE_RIGHT_J = 3
PLAYER_SPRITE_FRAMES = 4


class Player(SpriteObject):
    PLAYER_SPRITE_W = 32
    PLAYER_SPRITE_H = 48

    def __init__(self, x, y, speed):
        super().__init__(x, y, speed, pygame.image.load("images/girl_sprite.png"), 1, 0,
                         Player.PLAYER_SPRITE_W, Player.PLAYER_SPRITE_H,
                         PLAYER_SPRITE_STANDING_I, PLAYER_SPRITE_STANDING_J,
                         PLAYER_SPRITE_LEFT_J, PLAYER_SPRITE_RIGHT_J, PLAYER_SPRITE_FRAMES)
        self.isJumping = False
        self.jumpCount = 10

    def move(self, keys):
        is_left_or_right = False

        if keys[pygame.K_LEFT]:
            is_left_or_right = True
            self.move_left()

        if keys[pygame.K_RIGHT]:
            is_left_or_right = True
            self.move_right()

        if is_left_or_right:
            self.advance_animation()
        else:
            self.sprite_i = 3  # standing, keep direction but use last image in the row (has feet together)

        # up and down only when not jumping, this code moves the player up and down, removed in favour of
        # jumping with up and space fires a bullet

        # if not self.isJumping:
        #     if keys[pygame.K_UP]:
        #         self.y = max(self.y - self.speed, 0)
        #     if keys[pygame.K_DOWN]:
        #         self.y = min(self.y + self.speed, Constants.SCREEN_H - Player.sprite_h)
        #     if keys[pygame.K_SPACE]:
        #         self.isJumping = True

        # space jumps except if already jumping
        if not self.isJumping:
            if keys[pygame.K_UP]:
                self.isJumping = True

        elif self.jumpCount >= -10:  # quadratic jump
            jump_direction = 1  # once halfway through (at 0) turns to negative so drops back
            if self.jumpCount < 0:
                jump_direction = -1
            self.y -= int((self.jumpCount ** 2) * 0.3 * jump_direction)
            self.jumpCount -= 1

        else:  # done jumping, reset
            self.isJumping = False
            self.jumpCount = 10

