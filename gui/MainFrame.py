from tkinter import *
from tkinter import ttk
from gui.Settings import GUISettings
from gui.InputFrame import *

class MainFrame():
    
    def __init__(self) -> None:
        self.root = Tk()
        self.settings = GUISettings()
        self.__load_settings__()

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=10, row=10, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.entryPane = InputFrame(self.mainframe)
        self.entryPane.pack()
        # self.entryPane.grid(column=0, row=0, columnspan=4, rowspan=10)


        #Buttons
        self._win_size_debug = Button(self.mainframe, text = "Dimensions", command= self.printDims)
        self.__add_btns__()

    def mainLoop(self):
        self.root.mainloop()

    def __load_settings__(self) -> None:
        self.root.title(self.settings.title)
        self.root.minsize(self.settings.dimX, self.settings.dimY)

    def __add_btns__(self) -> None:
        self._win_size_debug.pack()

    def printDims(self) -> None:
        print(f"x: {self.root.winfo_width()}, y: {self.root.winfo_height()}")

    """Event Handling"""
    # def checkEvents(self):
    #     if 