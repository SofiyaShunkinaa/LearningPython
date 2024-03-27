from ursina import *

app = Ursina()

window.borderless = False
window.exit_button.enabled = False
window.fps_counter.enabled = False
window.cog_button.enabled = False
application.development = False

app.run()