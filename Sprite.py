import pygame
from Constants import Constants as const

# local constants
STANDING = 0
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4


class Sprite(object):
    def __init__(self, stand_imgs, move_left_imgs, move_right_imgs, move_up_imgs, move_down_imgs):
        self.stand_imgs = stand_imgs
        self.move_left_imgs = move_left_imgs
        self.move_right_imgs = move_right_imgs
        self.move_up_imgs = move_up_imgs
        self.move_down_imgs = move_down_imgs
        self.width = stand_imgs[0].get_rect().size[0]
        self.height = stand_imgs[0].get_rect().size[1]
        self.image_idx = 0
        self.direction = STANDING
        self.current_imgs = self.stand_imgs
        self.draw_count = 0  # it's too fast to animate every frame

    def draw(self, x, y, screen):
        screen.blit(self.current_imgs[self.image_idx], (x, y))
        self.draw_count += 1
        if self.draw_count % 4 == 0:
            self.advance_animation()

    def face_forwards(self):
        if self.direction != STANDING:
            self.image_idx = 0
            self.direction = STANDING
            self.current_imgs = self.stand_imgs

    def face_left(self):
        if self.direction != LEFT:
            self.image_idx = 0
            self.direction = LEFT
            self.current_imgs = self.move_left_imgs

    def face_right(self):
        if self.direction != RIGHT:
            self.image_idx = 0
            self.direction = RIGHT
            self.current_imgs = self.move_right_imgs

    def face_up(self):
        if self.direction != UP:
            self.image_idx = 0
            self.direction = UP
            self.current_imgs = self.move_up_imgs

    def face_down(self):
        if self.direction != DOWN:
            self.image_idx = 0
            self.direction = DOWN
            self.current_imgs = self.move_down_imgs

    def advance_animation(self):
        self.image_idx += 1
        if self.image_idx == len(self.current_imgs):
            self.image_idx = 0



