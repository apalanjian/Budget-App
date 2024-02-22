from tkinter import ttk

class InputFrame(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=3)
        self.rowconfigure(0, weight=3)
        self.businessName = ""
        self.transactionType = ""
        self.month = 0
        self.day = 0
        self.year = 2024
        self.transactionMethod = ""
        self.transactionTotal = ""
        self.createInputFields()

    def createInputFields(self):
        self.transactionTypeEntry = ttk.Combobox(self, textvariable=self.transactionType)
        self.transactionTypeEntry.pack()
        self.businessNameEntry = ttk.Entry(self, textvariable=self.businessName)
        self.businessNameEntry.pack()
        self.monthEntry = ttk.Entry(self, textvariable=self.month)
        self.monthEntry.pack()
        self.dayEntry = ttk.Entry(self, textvariable=self.day)
        self.dayEntry.pack()
        self.yearEntry = ttk.Entry(self, textvariable=self.year)
        self.yearEntry.pack()
        self.transactionMethodEntry = ttk.Entry(self, textvariable=self.transactionMethod)
        self.transactionMethodEntry.pack()
        self.transactionTotalEntry = ttk.Entry(self, textvariable=self.transactionTotal)
        self.transactionTotalEntry.pack()