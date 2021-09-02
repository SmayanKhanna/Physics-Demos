#author - Smayan Khanna
#Status = Incomplete

import pygame
from pygame.math import Vector2
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
class Rope(object):

    def __init__(self,centre_x, centre_y,angle ):
        self.centre_x = centre_x
        self.centre_y = centre_y
        self.angle = angle
        self.end_x = 300
        self.end_y = 300

    def draw(self,screen):
        pygame.draw.line(screen, black, (self.centre_x, self.centre_y), (self.end_x, self.end_y), 4)

def Physics(endx,endy,centrex,centrey,angle):
    # radius = math.sqrt((centrex-endx)**2 + (centrey-endy)**2)
    radius = 400
    x_pos = radius * math.sin(angle)
    y_pos = radius * math.sin(angle)

    return (x_pos,y_pos)


def draw():
    screen.fill(white)
    String.draw(screen)
    pygame.draw.line(screen, (200, 90, 20), pole, pole + vec, 3)
    pygame.display.update()

#Main Loop Variables/objects
run = True
pole = Vector2(screen_rect.center)
vec = Vector2()
vec.from_polar((90, 60))

String = Rope(640,360,0)

while run:
    clock.tick(100)
    positions = list(Physics(String.end_x,String.end_y,String.centre_x,String.centre_y,String.angle))
    String.end_x = positions[0]
    # String.end_y = positions[1]
    String.angle += 0.017

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    draw()

pygame.quit()

