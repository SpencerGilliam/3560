import tkinter
from tkinter import *
from tkinter import filedialog, Tk, Toplevel
import pprint  # added import
import tkinter as tk
from tkinter.ttk import Combobox
from backendInteract import *

filelist = []  # added line
root: Tk = tk.Tk()
root.geometry("500x500")

mb = Menubutton(root, text="PyAutoDoc Menu")

mb.pack()


########################################################################################################################
class Language(tk.Frame):  # Dropbox
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        cb = Combobox(self, textvariable=tk.StringVar(),
                      values=["Python", "C++", "C", "Ruby", "C#", "Go", "Java", "Javascript"
                              # Maybe Set up dynamically later
                          , "PHP", "Kotlin", "Scala", "Haskell", "Lua", "Rust", "Perl"],
                      state="readonly")  # Drop down menu

        cb.pack()
        cb.bind("<<ComboboxSelected>>", lambda event, arg=cb: self.callback(event, arg))

    def callback(self, event, arg):
        setLang(arg.get())


if __name__ == "__main__":
    Language(root).pack(fill="both", expand=True)


########################################################################################################################
def OpenFile(root, filelist,
             textbox):  # Select Files function, produces a button, and allows you to choose multiple files
    filez = filedialog.askopenfilenames(parent=root, title='Select files')
    filez = root.tk.splitlist(filez)  # splits file list
    filelist += filez  # added line
    Filebox(root, filelist, textbox)
    setFiles(filelist)


######################################################################################################################

textbox = Text(root)
textbox.pack()
textbox.config(height=15)
textbox.config(width=50)
textbox.config(state=DISABLED)

button = Button(text="Select Files", width=30, command=lambda: OpenFile(root, filelist, textbox))
button.pack(padx=25, pady=20, side=tk.TOP)

button2 = Button(text="Document", width=30, command=lambda: EnterComs(root))
button2.pack(padx=25, pady=10, side=tk.TOP)


#####################################################################################################
def Filebox(root, filelist, textbox):  # opens a child window that displays the current selected file
    textbox.config(state=NORMAL)

    def redirector(inputStr):
        textbox.insert(INSERT, inputStr)  # function to redirect output

    sys.stdout.write = redirector  # set sysout to redirector
    textbox.delete("1.0", END)
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(filelist)  # print out list
    textbox.config(state=DISABLED)  # disable textbox so user cant mess with it


######################################################################################################

######################################################################################################
def EnterComs(root):  # opens a child window that allows user to type in
    i = 0
    j = 0
    definers = getDefiners(LANGUAGE)
    lines = getLines(filelist[0], definers)
    i = find(lines, i)
    win2: Toplevel = tk.Toplevel(bg='white')
    win2.title("Function Documentation")
    win2.geometry("900x600")  # creates child window
    Label(win2, text="Function name:").grid(row=0, padx=5, pady=5)
    Label(win2, text="Expected return type:").grid(row=1, padx=5, pady=5)
    Label(win2, text="Info on each of the parameters (Include how you passed your ref/val):").grid(row=2, padx=5,
                                                                                                   pady=5)
    Label(win2, text="Possible errors this code may throw that can change possible variables:").grid(row=3, padx=5,
                                                                                                     pady=5)
    Label(win2, text="Description of function:").grid(row=4, padx=5, pady=5)
    e1 = Entry(win2)
    e2 = Entry(win2)
    e3 = Entry(win2)
    e4 = Entry(win2)
    e5 = Entry(win2)

    e1.grid(row=0, column=1, padx=5, pady=5)
    e1.config(width=40)
    e2.grid(row=1, column=1, padx=5, pady=5)
    e2.config(width=40)
    e3.grid(row=2, column=1, padx=5, pady=5)
    e3.config(width=40)
    e4.grid(row=3, column=1, padx=5, pady=5)
    e4.config(width=40)
    e5.grid(row=4, column=1, padx=5, pady=5)
    e5.config(width=40)
    
    Button(win2, text="No Comment").grid(row=9, column=0, padx=40, pady=30)
    Button(win2, text=">>", command=lambda:retrieve_input(j, lines)).grid(row=9, column=1, padx=25, pady=30)

    textbox = Text(win2)
    textbox.grid(row=10, column=0)
    textbox.config(width=40)
    textbox.config(height=1)
    #textbox.insert(END, filelist[j])
    textbox.insert(END, lines[i])
    textbox.config(state=DISABLED)

    def retrieve_input(j, lines):
        i = 0
        i = find(lines, i)
        if i == -1:
            j = j + 1
            lines = getLines(filelist[j], definers)
            i = 0
        entries = []
        temp = e1.get()
        if(temp != ""):
            entries.append(temp)
        temp = e2.get()
        if(temp != ""):
            entries.append(temp)
        temp = e3.get()
        if(temp != ""):
            entries.append(temp)
        temp = e4.get()
        if(temp != ""):
            entries.append(temp)
        temp = e5.get()
        if(temp != ""):
            entries.append(temp)
        addComment(filelist[j],entries,i)
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end")
        
        lines.pop(i, None)
        display_next(j, lines, textbox)

def display_next(j, lines, textbox):
    i = 0
    i = find(lines, i)
    if i == -1:
        j = j + 1
        lines = getLines(fileslist[j], definers)
        i = 0
    textbox.config(state=NORMAL)
    textbox.delete("1.0", END)
    textbox.insert(END, lines[i])
    textbox.config(state=DISABLED)

def find(lines, i):
    while not i in lines:
        i = i + 1
    if not bool(lines):
        return -1
    else:
        return i


#problem: cannot go past second function in file and only outputs to top function. might be scope issue
root.mainloop()

########################################################################################################################
