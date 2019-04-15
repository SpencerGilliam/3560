from tkinter import*
from tkinter import Menu

root = Tk()
root.geometry("300x300")

mb = Menubutton(root, text="Welcome to the Menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Python", command=lambda: print("Python"))
mb.menu.add_command(label="C++", command=lambda: print("C++"))

mb.pack()

def doNothing():
        print("I won`t")

menu =  Menu(root)
root.config(menu=menu)

subMenu: Menu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="file1", command=doNothing)
subMenu.add_command(label="file2", command=doNothing)
subMenu.add_command(label="file3", command=doNothing)
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="redo", command=doNothing)

root.mainloop()