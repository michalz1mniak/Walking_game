import pygame, pymunk, sys
import pymunk.pygame_util
from player import Player
from ground import Walls


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
background = pygame.image.load('background.png')

space = pymunk.Space()
space.gravity = (0,900)

player = Player()
player.add_to_space(space)

walls = Walls()
walls.add_to_space(space)

def get_camera_offset(player_pos, screen_size):
    offset_x = player_pos.x - screen_size[0] // 2
    offset_y = 0  
    return pymunk.Vec2d(offset_x, offset_y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player.torso_left_arm_motor.rate = -10
    elif keys[pygame.K_w]:
        player.torso_left_arm_motor.rate = 10
    else:
        player.torso_left_arm_motor.rate = 0

    if keys[pygame.K_e]:
        player.torso_right_arm_motor.rate = -10
    elif keys[pygame.K_r]:
        player.torso_right_arm_motor.rate = 10
    else:
        player.torso_right_arm_motor.rate = 0

    if keys[pygame.K_a]:
        player.torso_left_leg_motor.rate = -10
    elif keys[pygame.K_s]:
        player.torso_left_leg_motor.rate = 10
    else:
        player.torso_left_leg_motor.rate = 0
        
    if keys[pygame.K_d]:
        player.torso_right_leg_motor.rate = -10
    elif keys[pygame.K_f]:
        player.torso_right_leg_motor.rate = 10
    else:
        player.torso_right_leg_motor.rate = 0

    offset = get_camera_offset(player.torso_body.position, screen.get_size())

    screen.blit(background, (-offset.x-100, 0))
    walls.draw(screen, offset)
    player.draw_all(screen, offset)

    # 3300 koniec gry
    

    clock.tick(60)
    space.step(1/50)  
    pygame.display.flip()
