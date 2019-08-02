from tkinter import *
from tkinter import filedialog, Tk, Toplevel, messagebox
import pprint
import tkinter as tk
from tkinter.ttk import Combobox
from backendInteract import *
import Pages

WIDTH = 500
HEIGHT = 500

#   Application class
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master, relief=tk.GROOVE)
        master.title("PyAutoGui")
        master.geometry("{}x{}".format(WIDTH, HEIGHT))
        master.resizable(width=False, height=False)

        self.contentFrame = tk.Frame(master, width=100, height=100)
        self.contentFrame.pack(anchor=tk.NW, fill=tk.BOTH, expand=True)

        self.pages = [] #init pages list

        self.addContent()

        for page in self.pages:
            page.place(in_=self.contentFrame, x=0, y=0, relwidth=1, relheight=1)

        self.pages[0].show()

    def addContent(self, contentFrame=None):
        self.pages.append(Pages.Menu(WIDTH))
        self.pages.append(Pages.DocumenterPage(WIDTH))

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.pack()
    root.mainloop()