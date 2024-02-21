from tkinter import *
from Settings import GUISettings

class MainFrame():
    
    def __init__(self) -> None:
        self.root = Tk()
        self.settings = GUISettings()
        self.__load_settings__()

        #Buttons
        self._win_size_debug = Button(self.root, text = "Dimensions", command= self.printDims)
        self.__add_btns__()

    def mainLoop(self):
        self.root.mainloop()

    def __load_settings__(self) -> None:
        self.root.title(self.settings.title)
        self.root.minsize(self.settings.dimX, self.settings.dimY)

    def __add_btns__(self) -> None:
        self._win_size_debug.pack(side = "top")

    def printDims(self) -> None:
        print(f"x: {self.root.winfo_width()}, y: {self.root.winfo_height()}")

    """Event Handling"""
    # def checkEvents(self):
    #     if 