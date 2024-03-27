import time

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent=self.controller)

        self.hand_gun = Entity(parent=self.controller.camera_pivot,
                               scale=0.1,
                               position=Vec3(0.7, -1, 1.5),
                               rotation=Vec3(0, 170, 0),
                               model='Gun',
                               texture='Gun',
                               visible=False)

        self.knife = Entity(parent=self.controller.camera_pivot,
                               scale=0.4,
                               position=Vec3(0.7, -1, 1.5),
                               rotation=Vec3(0, 170, 0),
                               model='knife',
                               texture='knife_texture',
                               visible=False)

        self.weapons = [self.hand_gun, self.knife]
        self.current_weapon = 0
        self.switch_weapon()

    def switch_weapon(self):
        for i,v in enumerate(self.weapons):
            if i == self.current_weapon:
                v.visible = True
            else:
                v.visible = False

    def input(self,key):
        try:
            self.current_weapon = int(key) - 1
            self.switch_weapon()
        except ValueError:
            pass

        if key == 'scroll up':
            self.current_weapon = (self.current_weapon + 1) % len(self.weapons)
            self.switch_weapon()
        if key == 'scroll down':
            self.current_weapon = (self.current_weapon - 1) % len(self.weapons)
            self.switch_weapon()

        if key == 'left mouse down' and self.current_weapon == 0:
            Bullet(model='sphere',
                   color=color.black,
                   scale=0.2,
                   position=self.controller.camera_pivot.world_position,
                   rotation=self.controller.camera_pivot.world_rotation)

    def update(self):
        self.controller.camera_pivot.y = 2 - held_keys['left controller']


class Bullet(Entity):
    def __init__(self, speed=50, lifetime=10, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()

    def update(self):
        ray = raycast(self.world_position, self.forward, distance=self.speed*time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            destroy(self)

app = Ursina()

ground = Entity(model='plane',
                scale=20,
                texture='white_cube',

                collider='mesh')

player = Player(position=(0, 10, 0))
app.run()
