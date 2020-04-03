import pygame
from Constants import Constants

FRAME_DELAY_BETWEEN_BULLETS = 300  # so spaced out
BULLET_SPEED = 20


class MovingObject:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed


class Bullet(MovingObject):
    # bullets list
    bullets = []
    last_bullet_frame_count = -1
    bullet_radius = 5

    def __init__(self, x, y, speed):
        super().__init__(x, y, speed)
        Bullet.last_bullet_frame_count = pygame.time.get_ticks()

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), Bullet.bullet_radius)

    def move(self):
        if 10 < self.x < Constants.SCREEN_W - 10:
            self.x += self.speed
        else:
            Bullet.bullets.remove(self)    # doesn't seem to mind removing even though reading through the list forwards

    @staticmethod
    def draw_bullets(win):
        for b in Bullet.bullets:
            b.draw(win)

    @staticmethod
    def move_bullets():
        for b in Bullet.bullets:
            b.move()

    @staticmethod
    def fire_bullet(player):
        if pygame.time.get_ticks() - Bullet.last_bullet_frame_count > FRAME_DELAY_BETWEEN_BULLETS:
            Bullet.bullets.append(Bullet(player.x + player.half_sprite_w,
                                         player.y + player.half_sprite_h,
                                         BULLET_SPEED * player.last_direction))


class SpriteObject(MovingObject):
    def __init__(self, x, y, speed, img, sprite_i, sprite_j, sprite_w, sprite_h, standing_i, standing_j,
                 left_j, right_j, walk_frames):
        super().__init__(x, y, speed)
        self.img = img
        self.sprite_i = sprite_i           # indices up and down the sprite sheet
        self.sprite_j = sprite_j
        self.sprite_w = sprite_w
        self.sprite_h = sprite_h
        self.half_sprite_w = round(sprite_w / 2)
        self.half_sprite_h = round(sprite_h / 2)
        self.last_direction = -1    # default to facing left (for bullets)
        self.standing_i = standing_i
        self.standing_j = standing_j
        self.left_j = left_j
        self.right_j = right_j
        self.walk_frames = walk_frames

    def draw(self, win):
        pos_on_screen = (self.x, self.y, self.sprite_w, self.sprite_h)
        frame_in_sprite = pygame.Rect(self.sprite_i * self.sprite_w,
                                      self.sprite_j * self.sprite_h,
                                      self.sprite_w, self.sprite_h)
        win.blit(self.img, pos_on_screen, frame_in_sprite)

    def move_left(self):
        self.x = max(self.x - self.speed, 0)
        self.last_direction = -1
        self.sprite_j = self.left_j  # row on sprite sheet

    def move_right(self):
        self.x = min(self.x + self.speed, Constants.SCREEN_W - self.sprite_w)
        self.last_direction = 1
        self.sprite_j = self.right_j  # row on sprite sheet

    def advance_animation(self):
        if pygame.time.get_ticks() % Constants.WALK_ANIMATION_FRAMES == 0:  # animation too fast if every frame
            self.sprite_i = (self.sprite_i + 1) % self.walk_frames
