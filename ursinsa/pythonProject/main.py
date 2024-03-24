from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


def input(key):
    if key == 'o':
        quit()

    if key == 'shift':
        global shift_click
        if shift_click % 2 == 0:
            player.speed = normal_speed + 3
            shift_click += 1
        else:
            player.speed = normal_speed
            shift_click += 1

# загрузка текстуры
grass_texture = load_texture('assets/grass.png')

for x_dynamic in range(16):
    for z_dynamic in range(16):
        Entity(model='assets/block1', scale=0.5, texture=grass_texture, position=Vec3(x_dynamic, 0, z_dynamic))

# добавление персонажа
player = FirstPersonController()
player.gravity = 0.0

arm_texture = load_texture('assets/arm_texture.png')
hand = Entity(parent=camera.ui, model='assets/arm',
              texture=arm_texture, scale=0.2,
              rotation=Vec3(150, -10, 0), position=Vec2(0.5, -0.6))


sky_texture = load_texture('assets/sky.png')
sky = Entity( model='sphere', texture=sky_texture,
              scale = 1000, double_sided=True)
app.run()
