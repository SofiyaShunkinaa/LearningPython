import random
import pygame
import pygame.freetype
from my_car import MyCar
from road import Road
from traffic import TrafficCar


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

my_car_sound = pygame.mixer.Sound('img/sound1.wav')
my_car_sound.play(-1)

crash_sound = pygame.mixer.Sound('img/crash.wav')


road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

traffic_cars_group = pygame.sprite.Group()
spawn_traffic_time = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_traffic_time, 1000)

my_car_img = get_car_img("img/car.png", (130, 80), 90)
road_img = pygame.image.load("img/road.png")
road_img = pygame.transform.scale(road_img, (500, 750))

traffic_car_images = []
traffic_car1 = get_car_img("img/car1.png", (130, 80), -90)
traffic_car2 = get_car_img("img/car2.png", (130, 80), -90)
traffic_car3 = get_car_img("img/car3.png", (200, 80), -90)
traffic_car_images.extend((traffic_car1, traffic_car2, traffic_car3))

road = Road(road_img, (250, 400))
road_group.add(road)
road = Road(road_img, (250, -120))
road_group.add(road)


def spawn_road():
    road_bg = Road(road_img, (250, -600))
    road_group.add(road_bg)


def spawn_traffic():
    position = (random.choice([60, 190]), random.randint(-60, -40))
    speed = random.randint(7, 10)
    traffic_car = TrafficCar(random.choice(traffic_car_images), position, speed)
    traffic_cars_group.add(traffic_car)


def draw_all():
    road_group.update()
    road_group.draw(screen)
    traffic_cars_group.update()
    traffic_cars_group.draw(screen)
    my_car.draw(screen)


my_car = MyCar((250, 600), my_car_img)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()
        if event.type == spawn_traffic_time:
            spawn_traffic()

    screen.fill(background_color)
    my_car.move()
    draw_all()
    my_car.crash(crash_sound, traffic_cars_group)

    pygame.display.flip()
    clock.tick(90)
