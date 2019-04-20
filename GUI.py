from tkinter import*
from tkinter import Menu
from tkinter import filedialog
import os
# from tkfilebrowser import askopendirname, askopenfilenames, asksaveasfilename

root = Tk()
root.geometry("800x500")

mb = Menubutton(root, text="PyAutoDoc Menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Python", command=lambda: print("Python"))
mb.menu.add_command(label="C++", command=lambda: print("C++"))

mb.pack()

def OpenFile(root):
    filez = filedialog.askopenfilenames(parent=root, initialdir='/',initialfile='',filetypes=[("PNG", "*"),("JPEG", "*.jpg"),("All files", "*")])
    filez = root.tk.splitlist(filez)
    path = "C:\\Documents and Settings\\user\\Desktop\\Folder\\File1.txt"
    temp = path.split('\\')
    filename = temp[-1]
    print (filename)
    fileName = os.path.basename(path)
    print ("list of files =",filez)
    filez = root.tk.splitlist(filez)

button = Button(text="Select Files",width = 30,command=lambda: OpenFile(root))
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