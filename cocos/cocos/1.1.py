from cocos.layer import ColorLayer
from cocos.scene import Scene
from cocos.director import director
from cocos.text import Label
from cocos.actions import ScaleBy, Repeat, Reverse, RotateBy
from cocos.sprite import Sprite

class Hello(ColorLayer):
    def __init__(self):
        ColorLayer.__init__(self, 64, 64, 64, 255, 255)

        label = Label("Hello from Cocos2d",
                      font_name="Arial",
                      font_size=32,
                      anchor_x="center", anchor_y="center")
        label.position = 320, 240
        self.add(label)
        sprite = Sprite("enot.png")
        sprite.position = 320, 340
        sprite.scale = 0.5
        self.add(sprite, z=1)

        scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale+Reverse(scale)))
        sprite.do(Reverse(scale)+scale)


if __name__ == "__main__":
    director.init()
    layer = Hello()
    layer.do(RotateBy(360, duration=10))
    scene = Scene(layer)
    director.run(scene)