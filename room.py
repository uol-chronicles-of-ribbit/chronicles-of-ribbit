import random

from Constants import Constants as const
from obstacle import Obstacle, Wall


class Room:

    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    DIRECTIONS = (NORTH, EAST, SOUTH, WEST)
    OPPOSITE_DIRECTIONS = {
        NORTH: SOUTH,
        EAST: WEST,
        SOUTH: NORTH,
        WEST: EAST,
    }
    PLAYER_SPAWN_POINTS = {
        NORTH: (const.SCREEN_W / 2, const.TILE_SIZE),
        EAST: (const.SCREEN_H - const.TILE_SIZE*2, const.SCREEN_H / 2),
        SOUTH: (const.SCREEN_W / 2, const.SCREEN_H - const.TILE_SIZE*3),
        WEST: (const.TILE_SIZE, const.SCREEN_H / 2),
    }

    def __init__(self, entrance=None, complete=False):
        self.complete = complete
        self.entrance = entrance
        self.exit = self.create_exit()
        self.obstacles = list()
        self.walls = list()
        self.exits = list()
        self.enemies = list()
        self.create_border_wall()

    def create_border_wall(self):
        """Creates a border of Obstacle objects, clockwise, surrounding the grid."""
        for north_wall in range(0, const.SCREEN_W, const.TILE_SIZE):
            x = north_wall
            y = 0
            self.walls.append(Wall(x, y, const.WALL_IMAGE))
        for east_wall in range(0, const.SCREEN_H-const.TILE_SIZE, const.TILE_SIZE):
            x = const.SCREEN_W - const.TILE_SIZE
            y = east_wall
            self.walls.append(Wall(x, y, const.WALL_IMAGE))
        for south_wall in range(const.SCREEN_W-const.TILE_SIZE, 0, -const.TILE_SIZE):
            x = south_wall
            y = const.SCREEN_H - const.TILE_SIZE
            self.walls.append(Wall(x, y, const.WALL_IMAGE))
        for west_wall in range(const.SCREEN_H-const.TILE_SIZE, 0, -const.TILE_SIZE):
            x = 0
            y = west_wall
            self.walls.append(Wall(x, y, const.WALL_IMAGE))


    def create_exit(self):
        """Creates an exit direction randomly from N, E, S, W, excluding entrance direction if it exists."""
        valid_directions = list(self.DIRECTIONS)
        if self.entrance is not None:
            valid_directions.remove(self.entrance)
        return random.choice(valid_directions)

    def reveal_exit(self):
        """Reveals the exit tiles and saves them in self.exits"""
        # midpoint = int((len(self.walls)/8) * (self.exit*2))
        #
        # self.exits = self.walls[midpoint-2:midpoint+2]

        # TODO Move hardcoded values or generate dynamically based on width/height
        if self.exit == self.NORTH:
            self.exits = self.walls[19:23]
        elif self.exit == self.EAST:
            self.exits = self.walls[57:61]
            for exit_ in self.exits:
                exit_.x -= const.TILE_SIZE
                exit_.y -= const.TILE_SIZE
        elif self.exit == self.SOUTH:
            self.exits = self.walls[97:101]
            # adjust hitbox so user can hit it
            for exit_ in self.exits:
                exit_.x -= const.TILE_SIZE
                exit_.y -= const.TILE_SIZE
        elif self.exit == self.WEST:
            self.exits = self.walls[137:141]

        for exit_tile in self.exits:
            self.walls.remove(exit_tile)

    def complete_room(self):
        """Flags the room as complete and opens the exit"""
        assert not self.complete, 'Trying to complete an already complete room!'
        self.complete = True
        self.reveal_exit()

    def get_player_spawn_point(self):
        """Returns a tuple with the X, Y coordinates of where the player will spawn in the room."""
        # Entrance should not be none, but just in case, we'll spawn at N
        if self.entrance is None:
            self.entrance = self.NORTH
        return self.PLAYER_SPAWN_POINTS[self.entrance]

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)
