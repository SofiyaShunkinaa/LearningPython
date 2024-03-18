import random
import pygame
import pygame.freetype
from my_car import MyCar


def get_car_img(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Симулятор суетолога")
background_color = (0, 0, 0)

my_car_img = get_car_img("img/car.png", (130, 80), 90)
road_img = pygame.image.load("img/road.png")
road_img = pygame.transform.scale(road_img, (500, 750))

my_car = MyCar((250, 600), my_car_img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    screen.blit(road_img, (0, 0))
    my_car.draw(screen)

    pygame.display.flip()
    clock.tick(60)
