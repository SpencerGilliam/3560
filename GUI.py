from tkinter import *
from tkinter import filedialog
import pprint  # added import
import tkinter as tk
from tkinter.ttk import Combobox

filelist = []  # added line
root = tk.Tk()
root.geometry("500x500")

mb = Menubutton(root, text="PyAutoDoc Menu")

button = Button(text="Languages", width=30, command=lambda: Language)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
mb.pack()


#################################################################################################################
class Language(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        choiceVar = tk.StringVar()
        choices = ("Python", "C++", "C", "Ruby")
        choiceVar.set(choices[0])

        cb = Combobox(self, textvariable=choiceVar, values=choices)

        cb.pack()



if __name__ == "__main__":
    Language(root).pack(fill="both", expand=True)

###############################################################################################################
def OpenFile(root, filelist):
    filez = filedialog.askopenfilenames(parent=root, title='Select files')
    filez = root.tk.splitlist(filez)
    filelist += filez  # added line
    pp = pprint.PrettyPrinter(indent=0)  # added line
    pp.pprint(filelist)  # added line


button = Button(text="Select Files", width=30, command=lambda: OpenFile(root, filelist))
button.pack(padx=25, pady=20, side=tk.TOP)

root.mainloop()

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
