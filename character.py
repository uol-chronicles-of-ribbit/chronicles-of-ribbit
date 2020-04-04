import pygame
from Constants import Constants as const


class Character:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

        # TO be defined by child class
        self.img = None

    # width and height of image: https://stackoverflow.com/questions/19715251/pygame-getting-the-size-of-a-loaded-image/19715931
    def width(self):
        if self.img:
            return self.img.get_rect().size[0]
        else:
            return 0

    def height(self):
        if self.img:
            return self.img.get_rect().size[1]
        else:
            return 0



    def draw(self, screen):
        # draw the image on x, y; else draw a red rectangle
        # TODO: consider image size and centre it
        if self.img:
            screen.blit(self.img, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 16, 32), 0)


    def is_colliding(self, x, y, w, h):
        if (self.x > x + w or x > self.x + self.width()):
            return False

        if (self.y < y + h or y < self.y + self.height()):
            return False

        return True


    def move_left(self):
        self.x = max(self.x - self.speed, 0)

    def move_right(self):
        self.x = min(self.x + self.speed, const.SCREEN_W - self.width())

    def move_up(self):
        self.y = max(self.y - self.speed, 0)

    def move_down(self):
        self.y = min(self.y + self.speed, const.SCREEN_H - self.height())

    # TODO: thinking sprite class will be used by this class
    def advance_animation(self):
        pass

    def stop_moving_animation(self):
        pass

