import random

from Constants import Constants as const
from obstacle import Obstacle


class Room:

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    DIRECTIONS = (NORTH, EAST, SOUTH, WEST)

    def __init__(self, screen, entrance=None, complete=False):
        self.screen = screen
        self.complete = complete
        self.entrance = entrance
        self.exit = self.create_exit()

    def create_border_wall(self, screen):
        """Draws a border of Obstacle objects, clockwise, surrounding the grid"""
        # TODO Add a door?
        for north_wall in range(0, const.SCREEN_W, const.TILE_SIZE):
            x = north_wall
            y = 0
            Obstacle(x, y, const.WALL_IMAGE).draw(screen)
        for east_wall in range(const.SCREEN_H, 0, -const.TILE_SIZE):
            x = const.SCREEN_W - const.TILE_SIZE
            y = east_wall
            Obstacle(x, y, const.WALL_IMAGE).draw(screen)
        for south_wall in range(const.SCREEN_W, 0, -const.TILE_SIZE):
            x = south_wall
            y = const.SCREEN_H - const.TILE_SIZE
            Obstacle(x, y, const.WALL_IMAGE).draw(screen)
        for west_wall in range(0, const.SCREEN_H, const.TILE_SIZE):
            x = 0
            y = west_wall
            Obstacle(x, y, const.WALL_IMAGE).draw(screen)

    def create_exit(self):
        """Creates an exit direction randomly from N, E, S, W, excluding entrance direction if it exists."""
        valid_directions = list(self.DIRECTIONS)
        if self.entrance is not None:
            valid_directions.remove(self.entrance)
        return random.choice(valid_directions)

    def create(self):
        self.create_border_wall(self.screen)

