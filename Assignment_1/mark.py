
# Question 5: Write a GUI program in Python for a Marksheet.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Marksheet")
root.geometry("350x400")

Label(root, text="Student Marksheet",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Student Name").pack()
name = Entry(root)
name.pack()

Label(root, text="English Marks").pack()
english = Entry(root)
english.pack()

Label(root, text="Maths Marks").pack()
maths = Entry(root)
maths.pack()

Label(root, text="Science Marks").pack()
science = Entry(root)
science.pack()

result = Label(root, text="")
result.pack(pady=10)

def calculate():
    try:
        e = int(english.get())
        m = int(maths.get())
        s = int(science.get())

        if name.get() == "":
            messagebox.showerror("Error", "Enter student name")
            return

        if any(mark < 0 or mark > 100 for mark in [e, m, s]):
            messagebox.showerror("Error", "Marks must be between 0 and 100")
            return

        total = e + m + s
        percentage = total / 3

        if min(e, m, s) < 35:
            status = "Fail"
        else:
            status = "Pass"

        result.config(
            text=f"Name: {name.get()}\n"
                 f"Total: {total}/300\n"
                 f"Percentage: {percentage:.2f}%\n"
                 f"Result: {status}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid marks")

Button(root, text="Calculate Result",
       command=calculate).pack(pady=10)

root.mainloop()
