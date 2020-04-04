import pygame
from Constants import Constants
from Sprite import STANDING

FRAME_DELAY_BETWEEN_BULLETS = 300  # so spaced out
BULLET_SPEED = 30
# TODO be nice to make this transparent, but it's a nice to have right now
spell_img = pygame.image.load("images/magic_spell.png")


class Projectile:
    # bullets list
    projectiles = []
    last_bullet_frame_count = -1

    def __init__(self, x, y, speed, vector):
        self.x = round(x)
        self.y = round(y)
        self.vx = round(speed * vector[0])
        self.vy = round(speed * vector[1])
        self.start_tick = pygame.time.get_ticks()

    def draw(self, win):
        pass

    def move(self):
        pass

    @staticmethod
    def draw_projectiles(win):
        for b in Projectile.projectiles:
            b.draw(win)

    @staticmethod
    def move_projectiles():
        for b in Projectile.projectiles:
            b.move()


class Bullet(Projectile):
    bullet_radius = 5

    def __init__(self, x, y, speed, vector):
        super().__init__(x, y, speed, vector)
        self.on_screen = True
        Bullet.last_bullet_frame_count = pygame.time.get_ticks()

    def draw(self, win):
        elapsed = pygame.time.get_ticks() - self.start_tick
        for i in range(4):
            r = round(Bullet.bullet_radius * i * elapsed * 0.005)
            image = pygame.transform.scale(spell_img, (r*2, r*2))
            win.blit(image, (self.x - r, self.y -r))

            # this isn't very nice, but transparency doesn't seem to work that well either
            # s = pygame.Surface((r * 2, r * 2))
            # s.set_alpha(100)
            # s.fill((255, 255, 255))
            # pygame.transform.rotate(s, 90 * i)
            # win.blit(spell_img, (self.x - r, self.y -r))
            # pygame.draw.circle(win, (255, 255, 255, 20), (self.x, self.y), int(r / 2))


    def move(self):
        if 10 < self.x < Constants.SCREEN_W - 10:
            self.x += self.vx
        else:
            self.on_screen = False

        if 10 < self.y < Constants.SCREEN_H - 10:
            self.y += self.vy
        else:
            self.on_screen = False

        if not self.on_screen:
            Projectile.projectiles.remove(self)  # doesn't seem to mind removing even though reading through the list forwards

    @staticmethod
    def fire_bullet(char):
        if pygame.time.get_ticks() - Bullet.last_bullet_frame_count > FRAME_DELAY_BETWEEN_BULLETS:
            # BEWARE maybe do want a default when there's no direction...
            if char.facing() != STANDING:
                Projectile.projectiles.append(Bullet(char.x + char.width / 2,
                                                     char.y + char.height / 2,
                                                     BULLET_SPEED, char.facing()))
