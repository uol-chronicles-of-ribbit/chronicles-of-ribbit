import pygame
from Constants import Constants as const
from Obstacles import Obstacle

# initialize pygame
pygame.init()


def create_border_wall(screen):  # TODO move to Rooms.py
    """Draws a border of Obstacle objects, clockwise, surrounding the grid"""
    # TODO Add a door?
    for north_wall in range(0, const.SCREEN_W, const.TILE_SIZE):
        x = north_wall
        y = 0
        Obstacle(x, y, const.WALL_IMAGE).draw(screen)
    for east_wall in range(const.SCREEN_H, 0, -const.TILE_SIZE):
        x = const.SCREEN_W-const.TILE_SIZE
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


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((const.SCREEN_W, const.SCREEN_H))
        self.timer = pygame.time.Clock()
        pygame.display.set_caption(const.GAME_NAME)

    def run(self):
        run = True

        while run:

            for event in pygame.event.get():
                # exit game
                if event.type == pygame.QUIT:
                    run = False

            self.react_to_keys()
            self.update_objects()
            self.draw()

            create_border_wall(screen=self.screen)
            pygame.display.update()
            pygame.time.delay(50)
            self.timer.tick(const.FPS)

        pygame.quit()

    def react_to_keys(self):
        keys = pygame.key.get_pressed()

    def update_objects(self):
        print("nothing updated yet")

    def draw(self):
        self.screen.fill(const.BG_COLOUR)



if __name__ == "__main__":
    game = Game()
    game.run()