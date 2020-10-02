from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    text_area.delete(1.0,END)

def openFile():
    
    open_file_data=filedialog.askopenfile(initialdir="/",title="Select the file to Open",filetypes=(("text files","*.txt"),("all files","*.*")))
    
    if (open_file_data!=None):
        text_area.delete(1.0,END)

    for i in open_file_data:
        text_area.insert(END,i) # entering the data into text area .

    open_file_data.close() # after opening the file always close it

def saveFile():

    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file=None

        else:
            f=open(file,"w")
            f.write(text_area.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"- Notepad")
    
    else:
        #save the file
        f=open(file,"w")
        f.write(text_area.get(1.0,END))
        f.close()

def QuitApp():
    root.destroy()

def cut():
    text_area.event_generate(("<<Cut>>"))

def copy():
    text_area.event_generate(("<<Copy>>"))

def paste():
    text_area.event_generate(("<<Paste>>"))

def about():
    messagebox.showinfo("Notepad","Notepad by code with SATVIK")

if __name__ == "__main__":
    #basic tkinter setup
    root=Tk()
    root.title("Text Editor by : S@tVIK")
    root.geometry("700x750")

    # adding text area
    text_area=Text(root,font='lucida 13',bd=10,padx=10,pady=5,undo=True)
    text_area.pack(fill=BOTH,expand=True)
    file=None

    # creating menu bar
    Menu_bar=Menu(root)

    #creating file menu
    File_menu=Menu(Menu_bar,tearoff=0)
    #adding commands in file
    File_menu.add_command(label="New",command=newFile)
    File_menu.add_cascade(label="Open",command=openFile)
    File_menu.add_command(label="Save",command=saveFile)
    # File_menu.add_command(label="Save As",command=save_as_file)

    File_menu.add_separator()

    File_menu.add_command(label="Exit",command=QuitApp)
    Menu_bar.add_cascade(label="File",menu=File_menu)

    #creating edit menu
    Edit_menu=Menu(Menu_bar,tearoff=0)
    #adding commands in edit
    Edit_menu.add_command(label="Cut",command=cut)
    Edit_menu.add_command(label="Copy",command=copy)
    Edit_menu.add_command(label="Paste",command=paste)
    Edit_menu.add_separator()
    Edit_menu.add_command(label="Undo",command=text_area.edit_undo)
    Edit_menu.add_command(label="Redo",command=text_area.edit_redo)

    Menu_bar.add_cascade(label="Edit",menu=Edit_menu)

    #creating help menu
    Help_menu=Menu(Menu_bar,tearoff=0)
    Help_menu.add_command(label="About Notepad",command=about)
    Menu_bar.add_cascade(label="Help",menu=Help_menu)

    # scroll bar
    scroll=Scrollbar(text_area)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=text_area.yview)
    text_area.config(yscrollcommand=scroll.set)

    root.config(menu=Menu_bar)
    root.mainloop()

