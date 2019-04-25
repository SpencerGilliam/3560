import tkinter
from tkinter import *
from tkinter import filedialog
import pprint  # added import
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox

filelist = []  # added line
root = tk.Tk()
root.geometry("500x500")

mb = Menubutton(root, text="PyAutoDoc Menu")

mb.pack()


########################################################################################################################
class Language(tk.Frame):  # Allow you to choose your language
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        choiceVar = tk.StringVar()
        choices = ("Python", "C++", "C", "Ruby","C#","Go","Java","Javascript" #Maybe Set up dynamically later
                   ,"PHP","Kotlin","Scala","Haskell","Lua","Rust","Perl") #Language Choices
        choiceVar.set(choices[0])

        cb = Combobox(self, textvariable=choiceVar, values=choices, state="readonly") # Drop down menu

        cb.pack()

button = Button(text="Languages", width=30, command=lambda: Language)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

if __name__ == "__main__":
    Language(root).pack(fill="both", expand=True)
########################################################################################################################
    def OpenFile(root, filelist): #Select Files function, produces a button, and allows you to choose multiple files
        filez = filedialog.askopenfilenames(parent=root, title='Select files')
        filez = root.tk.splitlist(filez)
        filelist += filez  # added line
        Filebox(root, filelist)


button = Button(text="Select Files", width=30, command=lambda: OpenFile(root, filelist))
button.pack(padx=25, pady=20, side=tk.TOP)

button2 = Button(text="Enter Commands", width=30, command=lambda: EnterComs(root))
button2.pack(padx=25, pady=10, side=tk.TOP)

#####################################################################################################
def Filebox(root, filelist): #opens a child window that displays the current selected files
	win1 = tk.Toplevel(bg = 'white')
	win1.title('Selected files')
	win1.geometry("600x600") #creates child window
	textbox = Text(win1)
	textbox.pack() #makes textbox
	def redirector(inputStr):
		textbox.insert(INSERT, inputStr) #function to redirect output
	sys.stdout.write = redirector #set sysout to redirector
	pp = pprint.PrettyPrinter(indent = 0)
	pp.pprint(filelist) #print out list
	textbox.config(state = DISABLED) #disable textbox so user cant mess with it
######################################################################################################

######################################################################################################
def EnterComs(root): #opens a child window that allows user to type in (has no actual functionality yet)
	win2 = tk.Toplevel(bg = 'white')
	win2.title("Enter Commands")
	win2.geometry("600x600") #creates child window
	textbox = Text(win2)
	textbox.pack()
	textbox.insert(INSERT, "Enter your commands: ") #makes window textbox and adds text at beginning
#######################################################################################################


root.mainloop()

########################################################################################################################
