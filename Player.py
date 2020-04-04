import pygame
from Constants import Constants as const
from Sprite import Sprite
from character import Character


# basics of jumping is commented out for now unless we add later
class Player(Character):

    def __init__(self, x=const.SCREEN_W / 2, y=const.SCREEN_H / 2, speed=const.PLAYER_SPEED):
        super().__init__(x, y, speed,
                         Sprite([pygame.image.load("images/Rabbit_Idle_Left.png")],     #standing
                                [pygame.image.load("images/Rabbit_Idle_Left.png")],     #left
                                [pygame.image.load("images/Rabbit_Idle_Right.png")],     #right
                                [pygame.image.load("images/Rabbit_Idle_Up.png")],     #up
                                [pygame.image.load("images/Rabbit_Idle_Down.png")]))    #down

    def move(self, keys):
        is_moving = False

        if keys[pygame.K_LEFT]:
            is_moving = True
            self.move_left()

        if keys[pygame.K_RIGHT]:
            is_moving = True
            self.move_right()

        if keys[pygame.K_UP]:
            is_moving = True
            self.move_up()

        if keys[pygame.K_DOWN]:
            is_moving = True
            self.move_down()

        if not is_moving:
            self.sprite.face_forwards()

        # up and down only when not jumping, this code moves the player up and down, removed in favour of
        # jumping with up and space fires a bullet

        # if not self.isJumping:
        #     if keys[pygame.K_UP]:
        #         self.y = max(self.y - self.speed, 0)
        #     if keys[pygame.K_DOWN]:
        #         self.y = min(self.y + self.speed, Constants.SCREEN_H - Player.sprite_h)
        #     if keys[pygame.K_SPACE]:
        #         self.isJumping = True
        #
        # # space jumps except if already jumping
        # if not self.isJumping:
        #     if keys[pygame.K_UP]:
        #         self.isJumping = True
        #
        # elif self.jumpCount >= -10:  # quadratic jump
        #     jump_direction = 1  # once halfway through (at 0) turns to negative so drops back
        #     if self.jumpCount < 0:
        #         jump_direction = -1
        #     self.y -= int((self.jumpCount ** 2) * 0.3 * jump_direction)
        #     self.jumpCount -= 1
        #
        # else:  # done jumping, reset
        #     self.isJumping = False
        #     self.jumpCount = 10
