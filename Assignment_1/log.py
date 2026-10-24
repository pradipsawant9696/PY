# Question 2: Write a GUI program in Python for Login.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Form")
root.geometry("300x250")

Label(root, text="Login Form",
      font=("Arial", 16, "bold")).pack(pady=10)

Label(root, text="Username").pack()
username = Entry(root)
username.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

def login():
    if username.get() == "admin" and password.get() == "1234":
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()
