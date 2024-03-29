import cocos

class HelloCocos(cocos.layer.Layer):
    def __init__(self):
        super().__init__()
        label = cocos.text.Label('Hello Cocos', font_name='Times New Roman', font_size=32,
                                 anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))

        size = cocos.director.director.get_window_size()
        print(size)
        label.position = 640, 360
        self.add(label)


if __name__ == '__main__':
    cocos.director.director.init(width=1280, height=720, caption='Hello Cocos')
    hello = HelloCocos()
    scene = cocos.scene.Scene(hello)
    cocos.director.director.run(scene)