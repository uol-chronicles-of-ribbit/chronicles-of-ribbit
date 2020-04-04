import pygame


#
class Constants:
    PLAYER_SPEED = 8
    ENEMY_SPEED_STARTING = 3
    ENEMY_COUNT_STARTING = 4
    SCREEN_W = 640
    SCREEN_H = 640
    GAME_NAME = 'Chronicles of Ribbit'
    FPS = 30
    BG_COLOUR = pygame.Color('dark blue')
    TILE_SIZE = 16
    WALL_IMAGE = 'assets/wall.png'

    # Difficulty constants
    INCREASE_SPEED = 0
    INCREASE_COUNT = 1
    SPEED_INCREASE = 2
    COUNT_INCREASE = 1
