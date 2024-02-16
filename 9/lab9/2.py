from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Your credit calculator")
root.geometry("670x450")
root.update_idletasks()

label = ttk.Label(text="Annuity payment calculator", font=("Arial"))
label.pack(pady=10)

input_frame = ttk.Frame(borderwidth=1, relief=SOLID, )

iframe1 = ttk.Frame(input_frame)
iframe2 = ttk.Frame(input_frame)
iframe3 = ttk.Frame(input_frame)

label1 = ttk.Label(iframe1, text="Credit summary")
label1.pack(anchor=NW)
entry1 = ttk.Entry(iframe1)
entry1.pack(anchor=W)

label2 = ttk.Label(iframe2, text="Interest rate")
label2.pack(anchor=NW)
entry2 = ttk.Entry(iframe2)
entry2.pack(anchor=W)

label3 = ttk.Label(iframe3, text="Interest rate")
label3.pack(anchor=NW)
entry3 = ttk.Entry(iframe3)
entry3.pack(anchor=W)

iframe1.pack(padx=5)
iframe2.pack(padx=5)
iframe3.pack(padx=5)
input_frame.pack(fill=X, pady=15, ipady=10)

button = ttk.Button(text="Calculate")
button.pack(fill=X, padx=40, pady=20)

label_result = ttk.Label(text="Your annuity payment")
label_result.pack(pady=10)

result_frame = ttk.Frame()
text = Text(result_frame, height=5)
text.pack(side=LEFT, expand=1)
scrollbar = ttk.Scrollbar(result_frame, orient=VERTICAL, command=text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
result_frame.pack(fill=X)

root.mainloop()