import pygame


class Obstacle:

    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Wall(Obstacle):
    pass
