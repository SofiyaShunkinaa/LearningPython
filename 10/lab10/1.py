import random
from tkinter import *
from tkinter import ttk
import time

# Window sizes
WIN_H = 600
WIN_W = 500


# Managing functions
def move_snake(event):
    if event.keysym == 'Left':
        canvas.move(snake, -10, 0)
    if event.keysym == 'Right':
        canvas.move(snake, 10, 0)
    if event.keysym == 'Up':
        canvas.move(snake, 0, -10)
    if event.keysym == 'Down':
        canvas.move(snake, 0, 10)


def check_position():
    snake_cords = canvas.coords(snake)
    for config in bugs:
        bug_cords = canvas.coords(bug)


def close():
    global running
    running = False


# Window creation
window = Tk()
window.title("Snake Game")
window.protocol("WM_DELETE_WINDOW", close)

# Game images
snake_img = PhotoImage(file="snake.png").subsample(8, 8)
bug_img = PhotoImage(file="bug.png").subsample(10, 10)

# Layout creation
canvas = Canvas(window, width=WIN_W, height=WIN_H, bg='wheat2')
canvas.pack()

# Objects creation
bugs = []
snake = canvas.create_image(40, 40, image=snake_img)
for i in range(7):
    bug = canvas.create_image(random.randint(50, 650), random.randint(50, 550), image=bug_img)
    speed_x = random.randint(-1, 1)
    speed_y = random.randint(-1, 1)
    config = {'bug': bug, 'speed_x': speed_x, 'speed_y': speed_y}
    bugs.append(config)

canvas.bind_all("<Key>", move_snake)

# Game cycle
running = True
while running:
    # Object managing
    for config in bugs:
        canvas.move(config['bug'], config['speed_x'], config['speed_y'])

        coords = canvas.coords(config['bug'])
        if coords[0] < 0 or coords[0] > WIN_W:
            config['speed_x'] = -config['speed_x']
        if coords[1] < 0 or coords[1] > WIN_H:
            config['speed_y'] = -config['speed_y']

    # Window update
    window.update()
    time.sleep(0.01)

window.destroy()
