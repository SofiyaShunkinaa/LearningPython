from collections import defaultdict
from cocos.director import director
from cocos.layer import Layer
from cocos.scene import Scene
from cocos.sprite import Sprite
from pyglet.window import key
from cocos.collision_model import CircleShape, CollisionManager
from cocos.euclid import Vector2


class Game(Layer):
    is_event_handler = True

    def __init__(self):
        Layer.__init__(self)
        self.player = Actor(x=320, y=240, sprite='enot.png', color=(0,255,255))
        self.player.scale = .2
        self.add(self.player)

        for pos in [(100, 100), (540,380), (540,100), (100,380)]:
            self.add(Actor(pos[0], pos[1], 'ball.png', (255,255,0)))

        self.speed = 100
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def update(self, dt):
        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - (self.pressed[key.DOWN])

        if x != 0 or y != 0:
            pos = self.player.position
            x_ = pos[0] + self.speed * x * dt
            y_ = pos[1] + self.speed * y * dt
            self.player.position = (x_,y_)

    def on_key_press(self, k, modifiers):
        self.pressed[k] = 1

    def on_key_release(self, k, modifiers):
        self.pressed[k] = 0


class Actor(Sprite):
    def __init__(self, x, y, sprite, color):
        Sprite.__init__(self, image=sprite, color=color)
        self.position = pos = Vector2(x,y)
        self.cshape = CircleShape(pos, self.width/2)


if __name__ == '__main__':
    director.init()
    layer = Game()
    scene = Scene(layer)
    director.run(scene)
