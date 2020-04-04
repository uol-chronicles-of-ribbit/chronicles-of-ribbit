import pygame
from Constants import Constants as const
from room import Room
from Player import Player
from projectile import *
from enemies import Enemies

# initialize pygame
pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((const.SCREEN_W, const.SCREEN_H))
        self.timer = pygame.time.Clock()
        pygame.display.set_caption(const.GAME_NAME)
        self.player = Player()
        self.enemies = Enemies(count=4)
        self.score = 0
        self.lives = 5
        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def run(self):
        run = True

        while run:

            for event in pygame.event.get():
                # exit game
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.react_to_key_event(event.key)

            self.react_to_keys()
            self.update_objects()
            self.draw()

            Room(self.screen).create()
            pygame.display.update()
            pygame.time.delay(50)
            self.timer.tick(const.FPS)

        pygame.quit()

    def react_to_key_event(self, key):
        if key == pygame.K_SPACE:     # fire bullet
            Bullet.fire_bullet(self.player)

    def react_to_keys(self):
        self.player.move(pygame.key.get_pressed())

    def update_objects(self):
        Projectile.move_projectiles()

    def draw(self):
        self.screen.fill(const.BG_COLOUR)

        # check kills and update score
        self.score += self.enemies.check_if_dead(Projectile.projectiles)

        self.enemies.draw(self.screen)

        if self.lives <= 0:
            game_over = self.font.render('GAME OVER!', True, (255, 255, 255))
            self.screen.blit(game_over, (const.SCREEN_W//2, const.SCREEN_H//2))
            return


        #check if enemy killed player
        if self.player.died(self.enemies.alive_enemies):
            self.lives -= 1

        # draw scoreboard
        scoreboard = self.font.render(f"Score: {self.score} | Lives: {self.lives}", True, (255,255,255))
        self.screen.blit(scoreboard, (const.TILE_SIZE + 5, const.TILE_SIZE + 5))

        self.enemies.move()
        Projectile.draw_projectiles(self.screen)
        self.player.draw(self.screen)




if __name__ == "__main__":
    game = Game()
    game.run()