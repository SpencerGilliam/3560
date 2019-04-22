from tkinter import*
from tkinter import Menu
from tkinter import filedialog
import pprint #added import

filelist = [] #added line
root = Tk()
root.geometry("800x500")

mb = Menubutton(root, text="PyAutoDoc Menu")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Python", command=lambda: print("Python"))
mb.menu.add_command(label="C++", command=lambda: print("C++"))

mb.pack()


def OpenFile(root, filelist):
    filez = filedialog.askopenfilenames(parent=root,title='Select files')
    filez = root.tk.splitlist(filez)
    filelist += filez #added line
    pp = pprint.PrettyPrinter(indent=0) #added line
    pp.pprint (filelist) #added line

button = Button(text="Select Files",width = 30,command=lambda: OpenFile(root, filelist))
button.pack()

root.mainloop()
