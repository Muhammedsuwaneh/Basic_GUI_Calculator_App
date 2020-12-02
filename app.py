
from tkinter import *

# set main root
root = Tk()
root.title("CASIO")
root.iconbitmap('./icons/iconfinder_calculator_309097.ico')
root.geometry("322x310")
root.resizable(0, 0)

# set screen frame
screenFrame = LabelFrame(root, padx=5, pady=5)
screenFrame.pack()

# set entry
e = Entry(screenFrame, width=72, font=('Helvetica', 24), bg="#d5dbdb")
e.pack(pady=5, padx=5)

# set global design variables
button_bg1 = "#0d4abb"
button_bg2 = "#ff0000"
button_fg = "#fff"


# App Logic


# displays numbers on screen
def display(number):
    e.insert(END, number)


# clears screen
def clear():
    e.delete(0, END)


# adds numbers
def add():
    global number
    number = int(e.get())
    e.delete(0, END)
    print(number)


# subtracts numbers
def subtract():
    pass


# divides numbers
def divide():
    pass


# multiplies numbers
def multiply():
    pass


# finalizes operations
def equal():
    pass


# set button frame
buttonFrame = LabelFrame(root, padx=1, pady=1)
buttonFrame.pack()

# set buttons
button7 = Button(buttonFrame, text="7", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=70, borderwidth=0, command=lambda: display(7))
button7.grid(row=1, column=0, padx=1, pady=1)
button8 = Button(buttonFrame, text="8", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(8))
button8.grid(row=1, column=1, padx=1, pady=1)
button9 = Button(buttonFrame, text="9", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(9))
button9.grid(row=1, column=2, padx=1, pady=1)
button_add = Button(buttonFrame, text="+", padx=30, pady=15, bg=button_bg2, fg=button_fg, font=50, borderwidth=0, command=add)
button_add.grid(row=1, column=3, padx=1, pady=1)

button4 = Button(buttonFrame, text="4", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=70, borderwidth=0, command=lambda: display(4))
button4.grid(row=2, column=0, padx=1, pady=1)
button5 = Button(buttonFrame, text="5", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(5))
button5.grid(row=2, column=1, padx=1, pady=1)
button6 = Button(buttonFrame, text="6", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(6))
button6.grid(row=2, column=2, padx=1, pady=1)
button_subtract = Button(buttonFrame, text="-", padx=30, pady=15, bg=button_bg2, fg=button_fg, font=50, borderwidth=0, command=subtract)
button_subtract.grid(row=2, column=3, padx=1, pady=1)

button1 = Button(buttonFrame, text="1", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=70, borderwidth=0, command=lambda: display(1))
button1.grid(row=3, column=0, padx=1, pady=1)
button2 = Button(buttonFrame, text="2", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(2))
button2.grid(row=3, column=1, padx=1, pady=1)
button3 = Button(buttonFrame, text="3", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(3))
button3.grid(row=3, column=2, padx=1, pady=1)
button_multiply = Button(buttonFrame, text="*", padx=30, pady=15, bg=button_bg2, fg=button_fg, font=50, borderwidth=0, command=multiply)
button_multiply.grid(row=3, column=3, padx=1, pady=1)

button0 = Button(buttonFrame, text="0", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=lambda: display(0))
button0.grid(row=4, column=0, padx=1, pady=1)
button_clear = Button(buttonFrame, text="C", padx=30, pady=15, bg=button_bg2, fg=button_fg, font=40, borderwidth=0, command=clear)
button_clear.grid(row=4, column=1, padx=1, pady=1)
button_equal = Button(buttonFrame, text="=", padx=30, pady=15, bg=button_bg1, fg=button_fg, font=50, borderwidth=0, command=add)
button_equal.grid(row=4, column=2, padx=1, pady=1)
button_division = Button(buttonFrame, text="/", padx=30, pady=15, bg=button_bg2, fg=button_fg, font=50, borderwidth=0, command=divide)
button_division.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
