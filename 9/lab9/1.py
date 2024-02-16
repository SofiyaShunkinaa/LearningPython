from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

clicks = 0


def finish():
    root.destroy()
    print('closing...')


def click_button():
    global clicks
    clicks += 1
    button['text'] = str(clicks)
    label['text'] = entry.get()

def checkbutton_changed():
    if enabled.get() == 1:
        showinfo(title='Info', message='On')
    else:
        showinfo(title='Info', message='off')


root = Tk()
root.title("My first GUI")
root.geometry("250x350+600+200")
root.update_idletasks()

label = Label(text="Hello World!")
label.pack()
button = ttk.Button(text="Submit", command=click_button)
button.pack()

test = StringVar(value="Radio")
radio = ttk.Radiobutton(text="Radio", variable=test, value="Radio")
radio1 = ttk.Radiobutton(text="Media", variable=test, value="Media")
radio.pack()
radio1.pack()

entry = ttk.Entry()
entry.pack(anchor=NW, padx=5, pady=5)

text = Text(height=5, width=50)
text.pack()

enabled = IntVar()
check = ttk.Checkbutton(text="Turn on", variable=enabled, command=checkbutton_changed())
check.pack(anchor=N, padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()
