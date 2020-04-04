import pygame
from Constants import Constants as const
from Sprite import Sprite


class Character:
    def __init__(self, x, y, speed, sprite=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.sprite = sprite

        if sprite:
            self.width = sprite.width
            self.height = sprite.height
        else:
            self.width = 16
            self.height = 32

    # tomas : commented this out as have added sprite to initializer
    # width and height of image: https://stackoverflow.com/questions/19715251/pygame-getting-the-size-of-a-loaded-image/19715931
    # def width(self):
    #     if self.sprite:
    #         return self.sprite
    #     else:
    #         return 0
    #
    # def height(self):
    #     if self.img:
    #         return self.img.get_rect().size[1]
    #     else:
    #         return 0

    def draw(self, screen):
        # draw the image on x, y; else draw a red rectangle
        if self.sprite:
            self.sprite.draw(self.x, self.y, screen)
        else:
            pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height), 0)

    def is_colliding(self, x, y, w, h):
        if self.x > x + w or x > self.x + self.width:
            return False

        if self.y < y + h or y < self.y + self.height:
            return False

        return True

    def move_left(self):
        if self.sprite:
            self.sprite.face_left()
        self.x = max(self.x - self.speed, const.TILE_SIZE)

    def move_right(self):
        if self.sprite:
            self.sprite.face_right()
        self.x = min(self.x + self.speed, const.SCREEN_W - const.TILE_SIZE - self.width)

    def move_up(self):
        if self.sprite:
            self.sprite.face_up()
        self.y = max(self.y - self.speed, const.TILE_SIZE)

    def move_down(self):
        if self.sprite:
            self.sprite.face_down()
        self.y = min(self.y + self.speed, const.SCREEN_H - const.TILE_SIZE - self.height)


