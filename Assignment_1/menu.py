# Question 3: Write a GUI program in Python that contains a menu
# and uses the menu to open different windows.


from tkinter import *
root = Tk()
root.title("Menu Program")
root.geometry("400x300")
Label(root, text="Main Window",
 font=("Arial", 18)).pack(pady=50)
def open_window(title):
 win = Toplevel(root)
 win.title(title)
 win.geometry("300x200")
 Label(win, text=title, font=("Arial", 16)).pack(pady=50)
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(
 label="Open Window 1",
 command=lambda: open_window("Window 1")
)
file_menu.add_command(
 label="Open Window 2",
 command=lambda: open_window("Window 2")
)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
root.mainloop()