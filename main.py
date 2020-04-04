import pygame
from Constants import Constants as const

# initialize pygame
pygame.init()


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

            pygame.display.update()
            pygame.time.delay(50)
            self.timer.tick(const.FPS)


        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()