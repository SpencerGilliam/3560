import tkinter as tk
from tkinter import ttk, filedialog, messagebox

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
        self.selectedFiles = None
        ###############################
        #   Language Selection Combobox
        self.cb = ttk.Combobox(self, textvariable=tk.StringVar(),
                       values=["Python", "C++", "C", "Ruby", "C#", "Go", "Java", "Javascript"
                           , "PHP", "Kotlin", "Scala", "Haskell", "Lua", "Rust", "Perl"],
                       state="readonly")  # Drop down menu
        self.cb.set("Select Language")
        self.cb.bind("<<ComboboxSelected>>",
                lambda event, argu=self.cb: self.langSelectEvent(event, argu))  # event to grab selected language
        self.cb.place(x=(w/2), y=35, anchor="center")
        ###############################

        ###############################
        #   Selected Files Textbox
        self.textbox = tk.Text(self)
        self.textbox.config(width=50, height=15, state=tk.DISABLED)
        self.textbox.place(x=(w/2), y=220, anchor="center")  # really should not use place manager, but it is easy
        ###############################

        ###############################
        #   File Select Button
        self.selectButton = tk.Button(self, text="Select Files", width=15, command=lambda: self.openFiles())
        self.selectButton.place(x=(w/2), y=400, anchor="center")
        ###############################

        ###############################
        #   Document Button
        self.docButton = tk.Button(self, text="Document", width=30, command=lambda: self.master.children["!application"].pages[1].lift() if not self.SELECTED == None and not self.selectedFiles == None
                                                    else messagebox.showinfo("Error", "Please Select a Language and Files"))
        self.docButton.place(x=(w/2), y=450, anchor="center")
        ###############################

    def openFiles(self):
        self.selectedFiles = filedialog.askopenfilenames(title="Select files")
        self.textbox.config(state=tk.NORMAL)
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, '\n'.join(self.selectedFiles))
        self.textbox.config(state=tk.DISABLED)

    def langSelectEvent(self, event, argu):
        self.SELECTED = argu.get()

#   Documentor page
class DocumenterPage(Page):
    def __init__(self, w):
        Page.__init__(self)
        #label = tk.Label(self, text="Page 2")
        #label.place(x=(w/2), y=25, anchor="center")