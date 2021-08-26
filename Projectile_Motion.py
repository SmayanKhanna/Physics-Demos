#author - Smayan Khanna
#Date Completed - 27th August 2021

import pygame
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
caption = pygame.display.set_caption('Projectile Motion')

#Classes

class Projectile(object):

    def __init__(self,vel,angle):
        self.x = 100
        self.y = 400
        self.vel = vel
        self.angle = angle
        self.radius = 10
        self.x_vel = math.cos(self.angle)*self.vel
        self.y_vel = math.sin(self.angle)*self.vel
        self.gravity = 9.81

    # def physics(self):
    #     self.displacementx = self.x_vel*self.time
    #     self.displacementy = self.y_vel*self.time - 0.5*(self.gravity)*(self.time**2)
    #     xpath = self.x + self.displacementx
    #     ypath = self.y + self.displacementy

    def draw(self,screen):
        pygame.draw.circle(screen,black,(self.x,self.y),self.radius)

def Physics(time,x, y, xvel, yvel):
    gravity = 10
    disp_x = time * xvel
    disp_y = yvel*time - 0.5*(gravity)*(time**2)
    pathx = x + disp_x
    pathy = y - disp_y

    return (pathx,pathy)

def draw():
    screen.fill(white)
    Ball.draw(screen)
    pygame.draw.line(screen, black, (100, 500), (1000, 500), 10)
    pygame.display.update()

#Main Loop Variables/objects
run = True
Ball = Projectile(7,math.pi/3)

while run:
    clock.tick(60)
    system_time = pygame.time.get_ticks()/1500

    position = list(Physics(system_time, Ball.x, Ball.y, Ball.x_vel, Ball.y_vel))
    Ball.x = position[0]
    Ball.y = position[1]

    if Ball.y > 495:
        pygame.time.delay(10000)

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
        if event == pygame.K_2:
            print("additional keyboard functionality can be added")

    draw()

pygame.quit()

