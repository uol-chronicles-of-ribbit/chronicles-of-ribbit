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
        self.room = None

    def run(self):
        run = True

        while run:

            # Create first room
            if self.room is None:
                self.room = Room()
                self.player.warp(self.room.get_player_spawn_point())
                self.room.complete_room()  # TODO Only complete when the player earns it!
                self.room.enemies = Enemies(count=4)

            for event in pygame.event.get():
                # exit game
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.react_to_key_event(event.key)

            self.react_to_keys()
            self.update_objects()
            self.draw()

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
        self.player.draw(self.screen)
        Projectile.draw_projectiles(self.screen)
        self.room.enemies.draw(self.screen)
        self.room.enemies.move()
        self.room.draw(self.screen)



if __name__ == "__main__":
    game = Game()
    game.run()