
# Question 4: Write a GUI program in Python for a Calculator.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.geometry("300x300")

Label(root, text="First Number").pack()
num1 = Entry(root)
num1.pack()

Label(root, text="Second Number").pack()
num2 = Entry(root)
num2.pack()

result = Label(root, text="Result: ")
result.pack(pady=10)

def calculate(op):
    try:
        a = float(num1.get())
        b = float(num2.get())

        if op == "+":
            ans = a + b
        elif op == "-":
            ans = a - b
        elif op == "*":
            ans = a * b
        else:
            if b == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            ans = a / b

        result.config(text="Result: " + str(ans))

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

Button(root, text="Addition (+)",
       command=lambda: calculate("+")).pack()

Button(root, text="Subtraction (-)",
       command=lambda: calculate("-")).pack()

Button(root, text="Multiplication (*)",
       command=lambda: calculate("*")).pack()

Button(root, text="Division (/)",
       command=lambda: calculate("/")).pack()

root.mainloop()
