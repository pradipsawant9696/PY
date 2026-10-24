
# Question 1: Write a GUI program in Python for Registration.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Registration Form")
root.geometry("350x400")

Label(root, text="Registration Form",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Email").pack()
email = Entry(root)
email.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Label(root, text="Gender").pack()
gender = StringVar(value="Male")

Radiobutton(root, text="Male",
            variable=gender, value="Male").pack()

Radiobutton(root, text="Female",
            variable=gender, value="Female").pack()

def register():
    if name.get() == "" or email.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

Button(root, text="Register", command=register).pack(pady=15)

root.mainloop()





