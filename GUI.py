import tkinter
from tkinter import *
from tkinter import filedialog, Tk, Toplevel
import pprint
import tkinter as tk
from tkinter.ttk import Combobox
from backendInteract import *

SELECTED = []
filelist = []  # list to store files
root: Tk = tk.Tk() # main window
root.geometry("500x500")

mb = Menubutton(root, text="PyAutoDoc Menu") #menu text

mb.pack()


########################################################################################################################
class Language(tk.Frame):  # Dropbox
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        cb = Combobox(self, textvariable=tk.StringVar(),
                      values=["Python", "C++", "C", "Ruby", "C#", "Go", "Java", "Javascript"
                          , "PHP", "Kotlin", "Scala", "Haskell", "Lua", "Rust", "Perl"],
                           state="readonly")  # Drop down menu

        cb.pack()
        cb.bind("<<ComboboxSelected>>", lambda event, argu=cb: self.callback(event, argu)) #event to grab selected language

    def callback(self, event, argu): #actual function call
        SELECTED.clear()
        SELECTED.append(argu.get())


if __name__ == "__main__":
    Language(root).pack(fill="both", expand=True)


########################################################################################################################
def OpenFile(root, filelist,
             textbox):  # Select Files function, produces a button, and allows you to choose multiple files
    filez = filedialog.askopenfilenames(parent=root, title='Select files') #opens dialog box
    filez = root.tk.splitlist(filez)  # splits file list
    filelist += filez  # adds files to list
    Filebox(root, filelist, textbox) #calls filebox to display files selected

######################################################################################################################

textbox = Text(root)
textbox.pack()
textbox.config(height=15)
textbox.config(width=50)
textbox.config(state=DISABLED) #creates textbox in middle of main window

button = Button(text="Select Files", width=30, command=lambda: OpenFile(root, filelist, textbox))
button.pack(padx=25, pady=20, side=tk.TOP) #select files button

button2 = Button(text="Document", width=30, command=lambda: EnterComs(root, SELECTED))
button2.pack(padx=25, pady=10, side=tk.TOP) #document button


#####################################################################################################
def Filebox(root, filelist, textbox):  #sends file to textbox in root
    textbox.config(state=NORMAL) #allows editng

    def redirector(inputStr):
       textbox.insert(INSERT, inputStr)  # function to redirect output

    sys.stdout.write = redirector  # set sysout to redirector
    textbox.delete("1.0", END) #empty current contents
    pp = pprint.PrettyPrinter(indent=0) #sets printer
    pp.pprint(filelist)  # print out list
    textbox.config(state=DISABLED)  # disable textbox so user cant mess with it


######################################################################################################

######################################################################################################
def EnterComs(root, SELECTED):  # opens a child window that allows user to type in
    if len(filelist) == 0: #exits if no files selected
        exit()
    definers = getRegex(SELECTED[0])
    lines = getLines(filelist[0], definers) #grabs definers and lines from backend
    keys = list(lines.keys()) 
    keys.sort()
    keys.reverse() #grabs the keys from dictionary and sorts them and reverses them
    win2: Toplevel = tk.Toplevel(bg='white')
    win2.title("Function Documentation")
    win2.geometry("900x600")  # creates child window
    Label(win2, text="Function name:").grid(row=0, padx=5, pady=5)
    Label(win2, text="Expected return type:").grid(row=1, padx=5, pady=5)
    Label(win2, text="Info on each of the parameters (Include how you passed your ref/val):").grid(row=2, padx=5,
                                                                                                   pady=5)
    Label(win2, text="Possible errors this code may throw that can change possible variables:").grid(row=3, padx=5,
                                                                                                     pady=5)
    Label(win2, text="Description of function:").grid(row=4, padx=5, pady=5) #adds labels
    e1 = Entry(win2)
    e2 = Entry(win2)
    e3 = Entry(win2)
    e4 = Entry(win2)
    e5 = Entry(win2) #adds entry boxes

    e1.grid(row=0, column=1, padx=5, pady=5)
    e1.config(width=40)
    e2.grid(row=1, column=1, padx=5, pady=5)
    e2.config(width=40)
    e3.grid(row=2, column=1, padx=5, pady=5)
    e3.config(width=40)
    e4.grid(row=3, column=1, padx=5, pady=5)
    e4.config(width=40)
    e5.grid(row=4, column=1, padx=5, pady=5)
    e5.config(width=40) #configures entry boxes
    
    Button(win2, text="No Comment", command=lambda:nocomment(lines, keys, definers)).grid(row=9, column=0, padx=40, pady=30) #no comment button
    Button(win2, text=">>", command=lambda:retrieve_input(lines, keys, definers, SELECTED)).grid(row=9, column=1, padx=25, pady=30) #next button

    textbox = Text(win2)
    textbox.grid(row=10, column=0)
    textbox.config(width=40)
    textbox.config(height=1)
    textbox.insert(END, lines[keys[0]])
    textbox.config(state=DISABLED) #makes textbox that displays the first function to document

    def retrieve_input(lines, keys, definers, SELECTED):   #takes input from user and adds it to document and iterates to next function         
        if len(filelist) == 0: #exits program if no more files detected
            exit()
        entries = [] #makes entries list
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
            entries.append(temp) #adds entries to list
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end") #clears fields
        addComment(filelist[0],entries,keys[0], SELECTED[0]) #adds comment to file at the line above the function (given by keys)
        if len(keys) != 0: #if there are still keys removes that entry from dictionary and keys
            del lines[keys[0]]
            del keys[0]
        display_next(lines, textbox, keys, definers) #displays next function

    def nocomment(lines, keys, definers): #skips current function to be documented
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end") #clears entries
        if len(keys) != 0: #if still keys skips line
            del lines[keys[0]]
            del keys[0]
        display_next(lines, textbox, keys, definers) #displays next function

    def display_next(lines, textbox, keys, definers): #displatys next function in textbox
        if len(lines) == 0: #if no more lines go to next file
            exit() #eliminates multiple files being used as of right now due to index issue
            filelist.pop(0)
            if len(filelist) == 0: #if no more files exit program
                exit()
            else:
                lines = getLines(filelist[0], definers)
                keys = list(lines.keys())
                keys.sort()
                keys.reverse() #gets lines and keys from next file
        textbox.config(state=NORMAL)
        textbox.delete("1.0", END)
        textbox.insert(END, lines[keys[0]])
        textbox.config(state=DISABLED) #updates the textbox

#######################################################################################################################################################################

root.mainloop()

########################################################################################################################
