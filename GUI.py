from tkinter import *
from tkinter import filedialog, Tk, Toplevel
import pprint  # added import
import tkinter as tk
from tkinter.ttk import Combobox

filelist = []  # added line
root: Tk = tk.Tk()
root.geometry("500x500")

mb = Menubutton(root, text="PyAutoDoc Menu")

mb.pack()


########################################################################################################################
class Language(tk.Frame):  # Allow you to choose your language
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        choiceVar = tk.StringVar()
        choices = ("Python", "C++", "C", "Ruby", "C#", "Go", "Java", "Javascript"  # Maybe Set up dynamically later
                   , "PHP", "Kotlin", "Scala", "Haskell", "Lua", "Rust", "Perl")  # Language Choices
        choiceVar.set(choices[0])

        cb = Combobox(self, textvariable=choiceVar, values=choices, state="readonly")  # Drop down menu

        cb.pack()


button = Button(text="Languages", width=30, command=lambda: Language)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

if __name__ == "__main__":
    Language(root).pack(fill="both", expand=True)


########################################################################################################################
    def OpenFile(root, filelist):  # Select Files function, produces a button, and allows you to choose multiple files
        filez = filedialog.askopenfilenames(parent=root, title='Select files')
        filez = root.tk.splitlist(filez) #splits file list
        filelist += filez  # added line
        Filebox(root, filelist)

button = Button(text="Select Files", width=30, command=lambda: OpenFile(root, filelist))
button.pack(padx=25, pady=20, side=tk.TOP)

button2 = Button(text="Document", width=30, command=lambda: EnterComs(root))
button2.pack(padx=25, pady=10, side=tk.TOP)


#####################################################################################################
def Filebox(root, filelist):  # opens a child window that displays the current selected files
    win1 = tk.Toplevel(bg='white')
    win1.title('Selected files')
    win1.geometry("600x600")  # creates child window
    textbox = Text(win1)
    textbox.pack()  # makes textbox

    def redirector(inputStr):
        textbox.insert(INSERT, inputStr)  # function to redirect output

    sys.stdout.write = redirector  # set sysout to redirector
    pp = pprint.PrettyPrinter(indent=0)
    pp.pprint(filelist)  # print out list
    textbox.config(state=DISABLED)  # disable textbox so user cant mess with it


######################################################################################################

######################################################################################################
def EnterComs(root):  # opens a child window that allows user to type in
    win2: Toplevel = tk.Toplevel(bg='white')
    win2.title("Function Documentation")
    win2.geometry("900x600")  # creates child window
    textbox = Text(win2)
    textbox.pack()
    textbox.insert(INSERT, "Function name: \n"
                           "Expected return type:\n"
                           "Info on each of the parameters (Include how you have passed your ref/val):\n"
                           "Possible errors this code may throw that can change possible variables:\n"
                           "Description of Function: \n")  # makes window textbox and adds text at beginning

    win1 = tk.Button(win2, text='No Comment')
    win1.pack(padx=40, pady=30, side=tk.TOP)
    win2 = tk.Button(win2, text='>>')
    win2.pack(padx=25,pady=30,side=tk.TOP)


#######################################################################################################


root.mainloop()

########################################################################################################################
