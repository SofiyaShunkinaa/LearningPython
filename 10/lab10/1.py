import random
from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox

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
    check_position()


def check_position():
    snake_cords = canvas.coords(snake)
    global score
    for config in bugs:
        bug_cords = canvas.coords(config['bug'])  # Получаем координаты текущего объекта bug
        if bug_cords[0] - 50 < snake_cords[0] and bug_cords[0] + 50 > snake_cords[0] and bug_cords[1] - 50 < snake_cords[1] and bug_cords[1] + 50 > snake_cords[1]:
            canvas.delete(config['bug'])
            bugs.remove(config)
            score += 1
            score_label['text'] = "Score: " + str(score)
    if score == 7:
        messagebox.showinfo(title="Victory", message="You win!")
        close()


def close():
    global running
    running = False


def start():
    for config in bugs:
        config['speed_x'] = random.randint(0, 2)-1
        config['speed_y'] = random.randint(0, 2)-1
    canvas['bg'] = 'wheat2'


def stop():
    for config in bugs:
        config['speed_x'] = 0
        config['speed_y'] = 0
    canvas['bg'] = 'red'


# Window creation
window = Tk()
window.title("Snake Game")
window.protocol("WM_DELETE_WINDOW", close)
window.geometry("%dx%d+%d+%d" % (WIN_W, WIN_H+50, 450, 50))

# Game images
snake_img = PhotoImage(file="snake.png").subsample(8, 8)
bug_img = PhotoImage(file="bug.png").subsample(10, 10)

# Layout creation
canvas1 = Canvas(window, height=50, bg='wheat1')
canvas1.pack(fill=X)
canvas = Canvas(window, width=WIN_W, height=WIN_H, bg='wheat2')
canvas.pack()
score_label = ttk.Label(canvas1, font=('Helvetica'), text="Score: 0")
score_label.pack(side=LEFT, padx=5, pady=5)
btn_pause = ttk.Button(canvas1, text="Pause", command=stop)
btn_resume = ttk.Button(canvas1, text="Resume", command=start)
btn_resume.pack(side=RIGHT, padx=5, pady=5)
btn_pause.pack(side=RIGHT, padx=5, pady=5)



# Objects creation
bugs = []
snake = canvas.create_image(40, 40, image=snake_img)
for i in range(7):
    bug = canvas.create_image(random.randint(50, 450), random.randint(50, 550), image=bug_img)
    speed_x = random.randint(0, 2)-1
    speed_y = random.randint(0, 2)-1
    config = {'bug': bug, 'speed_x': speed_x, 'speed_y': speed_y}
    bugs.append(config)
score = 0



# Game cycle
running = True
while running:
    # Object managing
    for config in bugs:
        canvas.move(config['bug'], config['speed_x'], config['speed_y'])

        coords = canvas.coords(config['bug'])
        if coords[0]-20 < 0 or coords[0]+20 > WIN_W:
            config['speed_x'] = -config['speed_x']
        if coords[1]-20 < 0 or coords[1]+20 > WIN_H:
            config['speed_y'] = -config['speed_y']

    canvas.bind_all("<Key>", move_snake)


    # Window update
    window.update()
    time.sleep(0.01)

window.destroy()
