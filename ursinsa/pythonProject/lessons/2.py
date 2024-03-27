from ursina import *
from ursina.prefabs.first_person_controller import *


def update():
     if player.x > 18:
         player.position = (18, 0, -11)


app = Ursina()

maze = Entity(model='map', texture='brick',
              scale=20, collider='mesh')

player = FirstPersonController(position=(18, 0, -11))

app.run()