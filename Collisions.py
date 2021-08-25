#author - Smayan Khanna
#Date Completed - 26th August 2021
import pygame
import math
import random
import numpy as np
import itertools

pygame.init()

#Clock
clock = pygame.time.Clock()

font = pygame.font.SysFont('Helvetica',20)

#Variables
Width = 1280
Height = 720

#Colours
white = (255,255,255)
black = (0,0,0)

#Screen Commands

screen = pygame.display.set_mode((Width, Height))
caption = pygame.display.set_caption('Collisions')

#Objects

class Ball(object):

    def __init__(self, x, y, angle):
        self.size = 10
        self.x = x
        self.y = y
        self.angle = angle
        self.vel = 2
        self.vel_x = math.cos(angle)* self.vel
        self.vel_y = math.sin(angle) * self.vel

    def draw(self, screen):
        self.move()
        pygame.draw.circle(screen, black, (self.x,self.y), self.size)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

def draw():

    screen.fill(white)
    #collisions ball to ball:

    for ball1, ball2 in itertools.combinations(balls, 2):

        hitbox1 = pygame.Rect(ball1.x, ball1.y, 15, 15)
        hitbox2 = pygame.Rect(ball2.x, ball2.y, 15, 15)

        is_collide = hitbox1.colliderect(hitbox2)

        if is_collide:
            ball1.vel_y, ball2.vel_y= ball2.vel_y, ball1.vel_y
            ball1.vel_x, ball2.vel_x = ball2.vel_x, ball1.vel_x

    # collisions ball to wall:
    hitbox_wall_bottom = pygame.Rect(0, 710, 1280, 720)
    hitbox_wall_top = pygame.Rect(0, -710, 1280, 720)
    hitbox_wall_right =pygame.Rect(1270, 0, 1280, 720)
    hitbox_wall_left = pygame.Rect(-1270, 0, 1280, 720)

    for ball in balls:
        hitbox_ball_wall = pygame.Rect(ball.x,ball.y,20,20)
        is_wall_collide_b = hitbox_ball_wall.colliderect(hitbox_wall_bottom)
        is_wall_collide_t = hitbox_ball_wall.colliderect(hitbox_wall_top)
        is_wall_collide_r = hitbox_ball_wall.colliderect(hitbox_wall_right)
        is_wall_collide_l = hitbox_ball_wall.colliderect(hitbox_wall_left)

        if is_wall_collide_b:
            ball.vel_x = ball.vel_x
            ball.vel_y = -ball.vel_y

        if is_wall_collide_t:
            ball.vel_x = ball.vel_x
            ball.vel_y = -ball.vel_y

        if is_wall_collide_r:
            ball.vel_x = -ball.vel_x
            ball.vel_y = ball.vel_y

        if is_wall_collide_l:
            ball.vel_x = -ball.vel_x
            ball.vel_y = ball.vel_y

    for ball in balls:
        ball.draw(screen)

    # Count = font.render('Count:' + str(collision_count), 1, black)
    # screen.blit(Count, (500, 500))

    pygame.display.update()

run = True


no_of_balls = 20
ball_position = []
balls = []

for num in range(no_of_balls):
    ball_position = [random.randint(10,1270), random.randint(10,710)]
    ball_angle = random.choice(np.arange(0.0, 6.28, 0.1))
    balls.append(Ball(ball_position[0],ball_position[1],ball_angle))

while run:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()

pygame.quit()

