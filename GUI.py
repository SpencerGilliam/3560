from tkinter import*
from tkinter import Menu
from tkinter import filedialog

root = Tk()
root.geometry("800x500")

mb = Menubutton(root, text="Menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Python", command=lambda: print("Python"))
mb.menu.add_command(label="C++", command=lambda: print("C++"))

mb.pack()

def OpenFile(root):
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    filez = root.tk.splitlist(filez)
    print ("list of files =",filez)

button = Button(text="Open File",width = 30,command=lambda: OpenFile(root))
button.pack()

# def doNothing():
#         print("I won`t")

# menu =  Menu(root)
# root.config(menu=menu)
#
# subMenu: Menu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project", command=doNothing)
# subMenu.add_command(label="file2", command=doNothing)
# subMenu.add_command(label="file3", command=doNothing)
# subMenu.add_command(label="Exit", command=doNothing)
#
# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="redo", command=doNothing)

root.mainloop()