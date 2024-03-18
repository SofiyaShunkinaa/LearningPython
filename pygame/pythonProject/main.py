import random
import pygame
import pygame.freetype
from my_car import MyCar
from road import Road


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

my_car_sound = pygame.mixer.Sound('img/sound.wav')
my_car_sound.play(-1)

road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

my_car_img = get_car_img("img/car.png", (130, 80), 90)
road_img = pygame.image.load("img/road.png")
road_img = pygame.transform.scale(road_img, (500, 750))

road = Road(road_img, (250, 400))
road_group.add(road)
road = Road(road_img, (250, -50))
road_group.add(road)


def spawn_road():
    road = Road(road_img, (250, -600))
    road_group.add(road)


def draw_all():
    road_group.update()
    road_group.draw(screen)
    my_car.draw(screen)


my_car = MyCar((250, 600), my_car_img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()

    screen.fill(background_color)
    draw_all()

    pygame.display.flip()
    clock.tick(60)
