#author - Smayan Khanna
#Status: Incomplete

import pygame, sys
import math

pygame.init()

#Clock
clock = pygame.time.Clock()

#Variables Screen
Width = 1280
Height = 720

#Colors
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode((Width,Height))
screen_rect = screen.get_rect()
caption = pygame.display.set_caption('Projectile Motion')

#Classes
class Ball(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.colour = (0,0,0)

    def draw(self,screen):
        pygame.draw.circle(screen, self.colour, (self.x,self.y), self.size)

def Physics(y,time):
    gravitational_acceleration = 8
    height = math.fabs(y - 715)
    velocity = gravitational_acceleration * time

    return velocity

def draw():
    screen.fill(white)
    main_ball.draw(screen)
    pygame.display.update()

def Upward():
    running = True
    upward_time = pygame.time.get_ticks() / 1500
    while running:
        if main_ball.y > 200:
            running= False

        main_ball.y -= 100
        # y_velocity = -y_velocity + (gravitational_acceleration * system_time)
        # main_ball.y += y_velocity

#Main Loop Variables/objects
run = True
main_ball = Ball(600,200)
gravitational_acceleration = 5

while run:
    clock.tick(60)
    system_time = pygame.time.get_ticks() / 1500
    y_velocity = Physics(main_ball.y,system_time)
    main_ball.y += y_velocity
    hitbox_ball_wall = pygame.Rect(main_ball.x, main_ball.y, 20, 20)
    hitbox_wall_bottom = pygame.Rect(0, 715, 1280, 720)

    is_Collide = hitbox_wall_bottom.colliderect(hitbox_ball_wall)

    if is_Collide:
        Upward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    draw()

pygame.quit()
