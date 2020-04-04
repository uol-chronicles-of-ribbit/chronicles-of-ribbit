import random

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
        self.score = 0
        self.lives = 5
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def new_room(self, last_exit, enemies_count):
        self.room = Room(entrance=Room.OPPOSITE_DIRECTIONS[last_exit])
        self.player.warp(self.room.get_player_spawn_point())
        self.room.enemies = Enemies(enemies_count)

    def run(self):
        run = True

        while run:

            # Create first room
            if self.room is None:
                self.new_room(Room.SOUTH, 4)

            for event in pygame.event.get():
                # exit game
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.react_to_key_event(event.key)

            if len(self.room.enemies.alive_enemies) > 0:
                pass
                # for enemy in self.room.enemies.alive_enemies:
                #     if self.player.is_colliding(enemy.x, enemy.y, 32, 32):
                #         print("Dead!!!")
            elif not self.room.complete:
                self.room.complete_room()

            if self.room.complete:
                for exit_tile in self.room.exits:
                    if self.player.is_colliding(exit_tile.x, exit_tile.y, const.TILE_SIZE*2, const.TILE_SIZE*2):
                        self.new_room(last_exit=self.room.exit, enemies_count=4)

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
        # if key == pygame.K_k:  # kill an enemy key TODO Remove, this is for debugging
        #     print('Enemy killed!')
        #     enemy = random.choice(self.room.enemies.alive_enemies)
        #     self.room.enemies.alive_enemies.remove(enemy)
        # if key == pygame.K_n and self.room.complete:  # next room key TODO Remove, this is for debugging
        #     self.new_room(self.room.exit, 4)

    def react_to_keys(self):
        self.player.move(pygame.key.get_pressed())

    def update_objects(self):
        Projectile.move_projectiles()

    def draw(self):
        self.screen.fill(const.BG_COLOUR)
        self.player.draw(self.screen)
        self.room.draw(self.screen)
        Projectile.draw_projectiles(self.screen)

        # check kills and update score
        self.score += self.room.enemies.check_if_dead(Projectile.projectiles)

        self.room.enemies.check_if_dead(Projectile.projectiles)
        self.room.enemies.draw(self.screen)
        self.room.enemies.move()

        #check if enemy killed player
        if self.player.died(self.room.enemies.alive_enemies):
            self.lives -= 1

        # draw scoreboard
        scoreboard = self.font.render(f"Score: {self.score} | Lives: {self.lives}", True, (255,255,255))
        self.screen.blit(scoreboard, (const.TILE_SIZE + 5, const.TILE_SIZE + 5))


if __name__ == "__main__":
    game = Game()
    game.run()