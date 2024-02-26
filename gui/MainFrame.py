from tkinter import *
from tkinter import ttk
from gui.Settings import GUISettings
from gui.InputFrame import InputFrame
from gui.Menus import NavMenu

class MainFrame():
    
    def __init__(self) -> None:
        self.root = Tk()
        self.settings = GUISettings()
        self.__load_settings__()

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)

        self.navigationFrame = NavMenu(self.mainframe)
        self.navigationFrame.grid(column=0,row=0, sticky="N")

        self.entryPane = InputFrame(self.mainframe)
        self.entryPane.grid(column=1, row=0, columnspan=1, rowspan=1)
        
        


        #Buttons
        # self._win_size_debug = Button(self.mainframe, text = "Dimensions", command= self.printDims)
        # self._win_size_debug.grid(column=4, row=5, padx=5, pady=5)
        self.__add_btns__()



    def mainLoop(self):
        self.root.mainloop()

    def __load_settings__(self) -> None:
        self.root.title(self.settings.title)
        self.root.minsize(self.settings.dimX, self.settings.dimY)

    def __add_btns__(self) -> None:
        pass
        # self._win_size_debug.pack()

    def printDims(self) -> None:
        print(f"x: {self.root.winfo_width()}, y: {self.root.winfo_height()}")

    """Event Handling"""
    # def checkEvents(self):
    #     if 