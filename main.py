import pygame
from Constants import Constants as const
from room import Room
from Player import Player

# initialize pygame
pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((const.SCREEN_W, const.SCREEN_H))
        self.timer = pygame.time.Clock()
        pygame.display.set_caption(const.GAME_NAME)
        self.player = Player()

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

            Room(self.screen).create()
            pygame.display.update()
            pygame.time.delay(50)
            self.timer.tick(const.FPS)

        pygame.quit()

    def react_to_keys(self):
        self.player.move(pygame.key.get_pressed())


    def update_objects(self):
        print("nothing updated yet")

    def draw(self):
        self.screen.fill(const.BG_COLOUR)
        self.player.draw(self.screen)



if __name__ == "__main__":
    game = Game()
    game.run()