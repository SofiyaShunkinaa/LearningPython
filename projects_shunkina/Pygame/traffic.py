import pygame.sprite


class TrafficCar(pygame.sprite.Sprite):
    def __init__(self, image, position, speed):
        super().__init__()
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = position

    def remove(self):
        if self.rect.top>750:
            self.kill()

    def update(self):
        if self.speed in range(4,6):
            self.rect.y -= self.speed
            # self.position = 800
        else:
            self.rect.y += self.speed
        self.remove()
