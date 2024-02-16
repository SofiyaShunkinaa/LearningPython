from tkinter import *
from tkinter import ttk
import re

def calculate_payment():
    s = float(entry1.get())
    r = float(entry2.get()) / 100
    n = float(entry3.get())

    p = s * (r / 12) * (1 + r / 12) ** n / ((1 + r / 12) ** n - 1)
    total = p * n
    extra = total - s

    text.insert('end', f'Your annuity payment (equal payment) on a mortgage: \n{p:.2f}\n'
                       f'Your total loan payment amount: \n{total:.2f}\n'
                       f'Your loan overpayment amount: \n{extra:.2f}\n')


def is_valid(value):
    result = re.match(r'\d[\d.,]*', value) is not None
    if not result:
        errmsg.set('Please enter correct data')
    else:
        errmsg.set('')
    return result


root = Tk()
root.title("Your credit calculator")
root.geometry("670x530")
root.update_idletasks()

errmsg = StringVar()
check = (root.register(is_valid), "%P")

label = ttk.Label(text="Annuity payment calculator", font=("Arial"))
label.pack(pady=10)

input_frame = ttk.Frame(borderwidth=1, relief=SOLID, )

iframe1 = ttk.Frame(input_frame)
iframe2 = ttk.Frame(input_frame)
iframe3 = ttk.Frame(input_frame)

label1 = ttk.Label(iframe1, text="Credit summary")
label1.pack(anchor=NW)
entry1 = ttk.Entry(iframe1, validate="key", validatecommand=check)
entry1.pack(anchor=W)
error1 = ttk.Label(iframe1, foreground="red", textvariable=errmsg)
error1.pack(padx=5, pady=5, anchor=W)

label2 = ttk.Label(iframe2, text="Interest rate")
label2.pack(anchor=NW)
entry2 = ttk.Entry(iframe2, validate="key", validatecommand=check)
entry2.pack(anchor=W)
error2 = ttk.Label(iframe2, foreground="red", textvariable=errmsg)
error2.pack(padx=5, pady=5, anchor=W)

label3 = ttk.Label(iframe3, text="Interest rate")
label3.pack(anchor=NW)
entry3 = ttk.Entry(iframe3, validate="key", validatecommand=check)
entry3.pack(anchor=W)
error3 = ttk.Label(iframe3, foreground="red", textvariable=errmsg)
error3.pack(padx=5, pady=5, anchor=W)

iframe1.pack(padx=5)
iframe2.pack(padx=5)
iframe3.pack(padx=5)
input_frame.pack(fill=X, pady=15, ipady=10)

button = ttk.Button(text="Calculate", command=calculate_payment)
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
