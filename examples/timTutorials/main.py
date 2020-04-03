import pygame
from Player import Player
from Zombie import Zombie
from MovingObject import Bullet
from Constants import Constants

# global initialisations
pygame.init()
win = pygame.display.set_mode((Constants.SCREEN_W, Constants.SCREEN_H))
timer = pygame.time.Clock()
pygame.display.set_caption("Somewhat following Tim's tutorials") # https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=2&t=0s
font = pygame.font.Font('freesansbold.ttf', 20)
help_text = font.render("keys left/right up=jump space=shoot", True, (255, 255, 255))

# player and zombie
player = Player(100, Constants.SCREEN_H - Player.PLAYER_SPRITE_H * 2, 5) # x, y, speed
zombie = Zombie(400, Constants.SCREEN_H - Player.PLAYER_SPRITE_H * 2, 2) # x, y, speed

def draw():
    win.fill(Constants.BG_COLOUR)
    player.draw(win)
    zombie.draw(win)
    Bullet.draw_bullets(win)
    win.blit(help_text, (20, 20))

def move_objects():
    Bullet.move_bullets()
    zombie.move()

running = True
while running:
    for event in pygame.event.get():            # single press

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:     # fire bullet
                Bullet.fire_bullet(player)

    # detect keys that are down
    player.move(pygame.key.get_pressed())

    # other objects
    move_objects()

    # draw to the screen
    draw()

    # update the display, delay a bit and set the fps
    pygame.display.update()
    pygame.time.delay(50)
    timer.tick(Constants.FPS)
