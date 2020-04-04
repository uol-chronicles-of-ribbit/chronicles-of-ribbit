import pygame
from Constants import Constants as const
from random import choice, randint
from enemy import Enemy
from projectile import Bullet


class Enemies:
    def __init__(self, count=6):
        self.alive_enemies = []
        for _ in range(count):
            self.alive_enemies.append(Enemy(x=randint(const.TILE_SIZE, const.SCREEN_W - const.TILE_SIZE - 32), y = randint(const.TILE_SIZE, const.SCREEN_H - const.TILE_SIZE - 32 )))

    def draw(self, screen):
        for enemy in self.alive_enemies:
            enemy.draw(screen)

    def move(self):
        for enemy in self.alive_enemies:
            enemy.move()

    def check_if_dead(self, active_projectiles):
        kill_count = 0

        for enemy in self.alive_enemies:
            for proj in active_projectiles:
                if enemy.is_colliding(proj.x, proj.y, Bullet.bullet_radius, Bullet.bullet_radius):
                    kill_count += 1
                    print('hit an enemy')
                    enemy.respawn()

        return kill_count
