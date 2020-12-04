
from tkinter import *

# set main root
root = Tk()
root.title("CASIO")
root.iconbitmap('icon.ico')
root.geometry("322x310")
root.resizable(0, 0)

# set global design variables
bg1 = "#0d4abb"
bg2 = "#ff0000"
bg3 = "#ccccff"
fg = "#fff"

# set screen frame
screenFrame = LabelFrame(root, padx=5, pady=5, bg=bg1)
screenFrame.pack()

# set entry
e = Entry(screenFrame, width=72, font=('Helvetica', 24), bg=bg3)
e.pack(pady=5, padx=5)

# App Logic


class ButtonActions():

    def __init__(self):
        self._first_number = 0
        self._second_number = 0
        self._result = 0
        self._operation = ''

    def display(self, num):
        e.insert(END, num)

    @staticmethod
    def clear_screen():
        e.delete(0, END)

    @staticmethod
    def warning():
        e.delete(0, END)
        e.insert(END, "Syntax Error")

    def _add(self):
        try:
            self._operation = '+'
            self._first_number = int(e.get())
            self.clear_screen()
        except:
            self.warning()

    def subtract(self):
        try:
            self._operation = '-'
            self._first_number = int(e.get())
            self.clear_screen()
        except:
            self.warning()

    def divide(self):
        try:
            self._operation = '/'
            self._first_number = int(e.get())
            self.clear_screen()
        except:
            self.warning()

    def multiply(self):
        try:
            self._operation = '*'
            self._first_number = int(e.get())
            self.clear_screen()
        except:
            self.warning()

    def equal(self):
        self._second_number = int(e.get())
        if self._operation == '+':
            try:
                self._result = self._second_number + self._first_number
                self.clear_screen()
                self.display(self._result)
            except:
                self.warning()
        elif self._operation == '-':
            try:
                self._result = self._first_number - self._second_number
                self.clear_screen()
                self.display(self._result)
            except:
                self.warning()
        elif self._operation == '/':
            try:
                self._result = round((self._first_number / self._second_number), 2)
                self.clear_screen()
                self.display(self._result)
            except:
                self.warning()
        elif self._operation == '*':
            try:
                self._result = self._second_number * self._first_number
                self.clear_screen()
                self.display(self._result)
            except:
                self.warning()


# Button Actions object

button_object = ButtonActions()

# set button frame
buttonFrame = LabelFrame(root, padx=1, pady=1, bg=bg3)
buttonFrame.pack()

# set buttons
button7 = Button(buttonFrame, text="7", padx=30, pady=15, bg=bg1, fg=fg, font=70, borderwidth=0, command=lambda: button_object.display(7))
button7.grid(row=1, column=0, padx=1, pady=1)
button8 = Button(buttonFrame, text="8", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(8))
button8.grid(row=1, column=1, padx=1, pady=1)
button9 = Button(buttonFrame, text="9", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(9))
button9.grid(row=1, column=2, padx=1, pady=1)
button_add = Button(buttonFrame, text="+", padx=30, pady=15, bg=bg2, fg=fg, font=50, borderwidth=0, command= button_object._add)
button_add.grid(row=1, column=3, padx=1, pady=1)

button4 = Button(buttonFrame, text="4", padx=30, pady=15, bg=bg1, fg=fg, font=70, borderwidth=0, command=lambda: button_object.display(4))
button4.grid(row=2, column=0, padx=1, pady=1)
button5 = Button(buttonFrame, text="5", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(5))
button5.grid(row=2, column=1, padx=1, pady=1)
button6 = Button(buttonFrame, text="6", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(6))
button6.grid(row=2, column=2, padx=1, pady=1)
button_subtract = Button(buttonFrame, text="-", padx=30, pady=15, bg=bg2, fg=fg, font=50, borderwidth=0, command= button_object.subtract)
button_subtract.grid(row=2, column=3, padx=1, pady=1)

button1 = Button(buttonFrame, text="1", padx=30, pady=15, bg=bg1, fg=fg, font=70, borderwidth=0, command=lambda: button_object.display(1))
button1.grid(row=3, column=0, padx=1, pady=1)
button2 = Button(buttonFrame, text="2", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(2))
button2.grid(row=3, column=1, padx=1, pady=1)
button3 = Button(buttonFrame, text="3", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(3))
button3.grid(row=3, column=2, padx=1, pady=1)
button_multiply = Button(buttonFrame, text="*", padx=30, pady=15, bg=bg2, fg=fg, font=50, borderwidth=0, command= button_object.multiply)
button_multiply.grid(row=3, column=3, padx=1, pady=1)

button0 = Button(buttonFrame, text="0", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command=lambda: button_object.display(0))
button0.grid(row=4, column=0, padx=1, pady=1)
button_clear = Button(buttonFrame, text="C", padx=30, pady=15, bg=bg2, fg=fg, font=40, borderwidth=0, command= button_object.clear_screen)
button_clear.grid(row=4, column=1, padx=1, pady=1)
button_equal = Button(buttonFrame, text="=", padx=30, pady=15, bg=bg1, fg=fg, font=50, borderwidth=0, command= button_object.equal)
button_equal.grid(row=4, column=2, padx=1, pady=1)
button_division = Button(buttonFrame, text="/", padx=30, pady=15, bg=bg2, fg=fg, font=50, borderwidth=0, command= button_object.divide)
button_division.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
