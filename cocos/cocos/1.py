import cocos


class RotatingText(cocos.text.Label):
    def __init__(self, text = "", position = (0, 0)):
        super(RotatingText, self).__init__(text, position)
        self.schedule(self.update)

    def update(self, dt):
        self.rotation += dt * 20

cocos.director.director.init(width=1280, height=720, caption="Cocos Demo")
scene = cocos.scene.Scene()

scene.add(RotatingText("Hello world!", (100, 200)))
scene.add(cocos.text.Label("Hello world!", position = (100, 400), font_size =32, color=(80, 30, 128, 255)))
label = cocos.text.Label("Hello world!", position = (100, 200))
scene.add(label)
label.do(cocos.actions.MoveBy((0, 100), 5) | cocos.actions.FadeOut(3))



cocos.director.director.run(scene)
