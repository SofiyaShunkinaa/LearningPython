from cocos.director import director
from cocos.text import Label
from cocos.layer import Layer
from cocos.scene import Scene
from pyglet.window.key import symbol_string

class KeyDisplay(Layer):
    is_event_handler = True
    def __init__(self):
        Layer.__init__(self)
        self.text = Label('', x=100, y=100)

        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        keys = [symbol_string(k) for k in self.keys_pressed]
        text = "Simbols: " + ", ".join(keys)
        self.text.element.text = text

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()


if __name__ == '__main__':
    director.init()
    layer = KeyDisplay()
    scene = Scene(layer)
    director.run(scene)
