import random

from Constants import Constants as const
from obstacle import Obstacle


class Room:

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
    PLAYER_SPAWN_POINTS = {
        NORTH: (const.SCREEN_W / 2, const.TILE_SIZE)
    }

    def __init__(self, entrance=None, complete=False):
        self.complete = complete
        self.entrance = entrance
        self.exit = self.create_exit()
        self.obstacles = list()
        self.enemies = list()
        self.create_border_wall()

    def create_border_wall(self):
        """Creates a border of Obstacle objects, clockwise, surrounding the grid."""
        for north_wall in range(0, const.SCREEN_W, const.TILE_SIZE):
            x = north_wall
            y = 0
            self.obstacles.append(Obstacle(x, y, const.WALL_IMAGE))
        for east_wall in range(const.SCREEN_H, 0, -const.TILE_SIZE):
            x = const.SCREEN_W - const.TILE_SIZE
            y = east_wall
            self.obstacles.append(Obstacle(x, y, const.WALL_IMAGE))
        for south_wall in range(const.SCREEN_W, 0, -const.TILE_SIZE):
            x = south_wall
            y = const.SCREEN_H - const.TILE_SIZE
            self.obstacles.append(Obstacle(x, y, const.WALL_IMAGE))
        for west_wall in range(0, const.SCREEN_H, const.TILE_SIZE):
            x = 0
            y = west_wall
            self.obstacles.append(Obstacle(x, y, const.WALL_IMAGE))

    def create_exit(self):
        """Creates an exit direction randomly from N, E, S, W, excluding entrance direction if it exists."""
        valid_directions = list(self.DIRECTIONS)
        if self.entrance is not None:
            valid_directions.remove(self.entrance)
        return random.choice(valid_directions)

    def open_exit(self):
        # TODO Remove obstacles at direction point
        pass

    def complete_room(self):
        """Flags the room as complete and opens the exit"""
        assert not self.complete, 'Trying to complete an already complete room!'
        self.complete = True
        self.open_exit()

    def get_player_spawn_point(self):
        """Returns a tuple with the X, Y coordinates of where the player will spawn in the room."""
        # Entrance should not be none, but just in case, we'll spawn at N
        if self.entrance is None:
            self.entrance = self.NORTH
        return self.PLAYER_SPAWN_POINTS[self.entrance]

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
