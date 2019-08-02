import tkinter as tk
from tkinter import ttk

class Page(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
    def show(self, event=None):
        self.lift()

#   Main menu
class Menu(Page):
    def __init__(self, w):
        Page.__init__(self)
        #label = tk.Label(self, text="Python Template Window")
        #label.place(x=(w/2), y=25, anchor="center")  # Place label at top of screen
        self.SELECTED = None    #init SELECTED var
        cb = ttk.Combobox(self, textvariable=tk.StringVar(),
                       values=["Python", "C++", "C", "Ruby", "C#", "Go", "Java", "Javascript"
                           , "PHP", "Kotlin", "Scala", "Haskell", "Lua", "Rust", "Perl"],
                       state="readonly")  # Drop down menu
        cb.set("Select Language")
        cb.bind("<<ComboboxSelected>>",
                lambda event, argu=cb: self.callback(event, argu))  # event to grab selected language

    def callback(self, event, argu):
        self.SELECTED = argu.get()

#   Documentor page
class DocumenterPage(Page):
    def __init__(self, w):
        Page.__init__(self)
        #label = tk.Label(self, text="Page 2")
        #label.place(x=(w/2), y=25, anchor="center")