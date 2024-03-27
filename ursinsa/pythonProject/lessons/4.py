from ursina import *
from ursina.prefabs.first_person_controller import *

app = Ursina()

mountains = Terrain(heightmap='artboard', skip=4)

terrain = Entity(model=mountains,
                 scale=(100,20,100),
                 texture='new_texture',
                 collider='mesh')

player = FirstPersonController(y=100)

app.run()