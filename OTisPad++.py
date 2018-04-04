import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300 #this will be the width of the application upon launch
    __thisHeight = 300 #this will be the height of the application upon launch
    __thisTextArea = Text(__root) #we call of text area from the library i.e. tkinter
    __thisMenuBar = Menu(__root) #we call of menu bar from the library i.e. tkinter
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0) #here we create the file menu on the menubar
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0) #here we create the edit menu on the menubar
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0) #here we create the help menu on the menubar
    __thisScrollBar = Scrollbar(__thisTextArea)  #here we create the scroll-bar on the text area
    __file = None

    def __init__(self, **kwargs):
        # initialization

        # set icon ; you inser this code when you have an icon you want to use to display your application
        try:
            self.__root.wm_iconbitmap("Notepad.ico")  # GOT TO FIX THIS ERROR (ICON)
        except:
            pass

        # set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # set the window text
        self.__root.title("Untitled - OTisPad") #this is an instance of the application when run

        # center the window ;  this will make the application upon launch will run at the center of the screen
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # to make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        #this adds new as a button to the file menu; to aid user open a new OTisPad
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        # this adds open as a button to the file menu; to aid user open an existing document
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        # this adds save as a button to the file menu; to aid user save a file being worked on
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        # this adds new as a button to the file menu; to aid user exit OTisPad; same as close
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)
        # this adds new as a button to the edit menu; to aid user cut
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)

        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("Notepad", "Created by: Otiboe Gabriel Kwame (http://otiboegabriel.com)")
    #display this information
    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # no file to open
            self.__file = None
        else:
            # try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - OTisPad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                # change the window title
                self.__root.title(os.path.basename(self.__file) + " - OTisPad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # run main application
        self.__root.mainloop()


# run main application
notepad = Notepad(width=600, height=400)
notepad.run()
