from tkinter import ttk
from tkinter import StringVar

class NavMenu(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.__init_buttons__()

    def __init_buttons__(self):
        self.homeBtn = ttk.Button(self, text="Home")
        self.homeBtn.grid(column=0,row=0,sticky="EW")

        self.settingsBtn = ttk.Button(self, text="Settings")
        self.settingsBtn.grid(column=0,row=1,sticky="EW")

        self.addCatBtn = ttk.Button(self, text="Add Category")
        self.addCatBtn.grid(column=0,row=2,sticky="EW")

        self.addTransBtn = ttk.Button(self, text="New Transaction")
        self.addTransBtn.grid(column=0,row=4,sticky="EW")

    