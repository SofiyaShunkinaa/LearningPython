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
root.geometry("400x550+600+200")
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

langs = ['Python', 'Java', 'C', 'C++', 'Javascript', 'HTML', 'TypeScript', 'C#', 'PHP']
lang_vars = Variable(value=langs)
lang_list = Listbox(listvariable=lang_vars, height=5)
lang_list.pack(side=RIGHT, padx=5)

combo = ttk.Combobox(values=langs)
combo.pack(fill=X)

menu = Menu()
options = Menu(tearoff=0)
addional = Menu(tearoff=0)
addional.add_command(label="Commit and push")
addional.add_command(label="Undo")
addional.add_command(label="Redo")
options.add_cascade(label="Commit", menu=addional)
options.add_command(label="Push")
menu.add_cascade(label="Options", menu=options)
root.config(menu=menu)

lang_str = StringVar(value=langs)
listbox = Listbox(listvariable=lang_str, height=5)
listbox.pack(side=LEFT)
scroll = ttk.Scrollbar(orient='vertical', command=listbox.yview)
scroll.pack(side=RIGHT, fill=Y)


root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()
