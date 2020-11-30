
from tkinter import *

# set main root
root = Tk()
root.title("CASIO")
root.configure(bg="#34495e")
root.iconbitmap('./icons/iconfinder_calculator_309097.ico')
root.geometry("305x370")
root.resizable(0, 0)

# set screen frame
screenFrame = LabelFrame(root, padx=5, pady=5, bg="#2e4053")
screenFrame.pack()

# set entry
e = Entry(screenFrame, width=72, font=('Helvetica', 24), bg="#d5dbdb")
e.pack(pady=5, padx=5)


# App Logic


def display(number):
    e.insert(END, number)


# set button frame
buttonFrame = LabelFrame(root, padx=1, pady=1)
buttonFrame.pack()

# set buttons
button1 = Button(buttonFrame, text="7", padx=39, pady=15, bg="#5d6d7e", fg="#fff", font=70, borderwidth=0,
                 command=lambda: display(7))
button1.grid(row=1, column=0, padx=2, pady=2)
button2 = Button(buttonFrame, text="8", padx=39, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0, command=lambda: display(8))
button2.grid(row=1, column=1, padx=2, pady=2)
button3 = Button(buttonFrame, text="9", padx=38, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0, command=lambda: display(9))
button3.grid(row=1, column=2, padx=2, pady=2)

button4 = Button(buttonFrame, text="4", padx=39, pady=15, bg="#5d6d7e", fg="#fff", font=70, borderwidth=0, command=lambda: display(4))
button4.grid(row=2, column=0, padx=2, pady=2)
button5 = Button(buttonFrame, text="5", padx=39, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0, command=lambda: display(5))
button5.grid(row=2, column=1, padx=2, pady=2)
button6 = Button(buttonFrame, text="6", padx=38, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0, command=lambda: display(6))
button6.grid(row=2, column=2, padx=2, pady=2)

button7 = Button(buttonFrame, text="1", padx=39, pady=15, bg="#5d6d7e", fg="#fff", font=70, borderwidth=0, command=lambda: display(1))
button7.grid(row=3, column=0, padx=2, pady=2)
button8 = Button(buttonFrame, text="2", padx=39, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0, command=lambda: display(2))
button8.grid(row=3, column=1, padx=2, pady=2)
button9 = Button(buttonFrame, text="3", padx=38, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0, command=lambda: display(3))
button9.grid(row=3, column=2, padx=2, pady=2)

button_add = Button(buttonFrame, text="+", padx=40, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0)
button_add.grid(row=4, column=0, padx=2, pady=2)
button_subtract = Button(buttonFrame, text="-", padx=40, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0)
button_subtract.grid(row=4, column=1, padx=2, pady=2)
button_multiply = Button(buttonFrame, text="*", padx=40, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0)
button_multiply.grid(row=4, column=2, padx=2, pady=2)

button_division = Button(buttonFrame, text="/", padx=42, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0)
button_division.grid(row=5, column=0, padx=2, pady=2)
button_equal = Button(buttonFrame, text="-", padx=40, pady=15, bg="#5d6d7e", fg="#fff", font=50, borderwidth=0)
button_equal.grid(row=5, column=1, padx=2, pady=2)
button_clear = Button(buttonFrame, text="AC", padx=30, pady=15, bg="#5d6d7e", fg="#fff", font=40, borderwidth=0)
button_clear.grid(row=5, column=2, padx=2, pady=2)

root.mainloop()
