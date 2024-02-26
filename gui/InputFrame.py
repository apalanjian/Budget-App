from tkinter import ttk
from tkinter import StringVar
from tkinter import IntVar
from Transaction import Transaction as T
from datetime import datetime

class InputFrame(ttk.Frame):

    def __init__(self, master):
        super().__init__(master,relief="sunken")
        self.businessName = StringVar(value="")
        self.transactionType = StringVar(value="")
        self.month = IntVar(value=datetime.now().month)
        self.day = IntVar(value=datetime.now().day)
        self.year = IntVar(value=datetime.now().year)
        self.transactionMethod = StringVar(value="")
        self.transactionTotal = StringVar(value="")
        self.createInputFields()

    def createInputFields(self):
        self.transactionTypeLabel = ttk.Label(self, text="Category Name: ")
        self.transactionTypeLabel.grid(column=0, row = 0, sticky="W", padx=5, pady=5)
        self.transactionTypeEntry = ttk.Combobox(
            self, textvariable=self.transactionType, 
            values=["Household", "Restaurants", "Grocceries"], state= "readonly"
            )
        self.transactionTypeEntry.grid(column=1, row = 0, sticky="E", padx=5, pady=5)

        self.businessNameLabel = ttk.Label(self, text="Business Name: ")
        self.businessNameLabel.grid(column=0, row = 1, sticky="W", padx=5, pady=5)
        self.businessNameEntry = ttk.Entry(self, textvariable=self.businessName)
        self.businessNameEntry.grid(column=1, row = 1, sticky="E", padx=5, pady=5)

        self.__date_frame__()

        self.transactionMethodLabel = ttk.Label(self, text="Payment Type: ")
        self.transactionMethodLabel.grid(column=0, row = 5, sticky="W", padx=5, pady=5)
        self.transactionMethodEntry = ttk.Entry(self, textvariable=self.transactionMethod)
        self.transactionMethodEntry.grid(column=1, row = 5, sticky="E", padx=5, pady=5)

        self.transactionTotalLabel = ttk.Label(self, text="Total: ")
        self.transactionTotalLabel.grid(column=0, row = 6, sticky="W", padx=5, pady=5)
        self.transactionTotalEntry = ttk.Entry(self, textvariable=self.transactionTotal)
        self.transactionTotalEntry.grid(column=1, row = 6, sticky="E", padx=5, pady=5)

        self.submitTransactionBtn = ttk.Button(self,text="Submit",command=self.createTransaction)
        self.submitTransactionBtn.grid(column=1, row=7, sticky="E",padx=2,pady=2)

    def __date_frame__(self):
        self.dateLabel = ttk.Label(self, text="Date(m/d/yyyy): ")
        self.dateLabel.grid(column=0, row = 2, pady=5)

        self.dateFrame = ttk.Frame(self)
        self.dateFrame.grid(column=1, row = 2)
        #Change to date and 3 Spinboxes
        self.monthEntry = ttk.Spinbox(self.dateFrame, from_=1, to=12, width=3, textvariable=self.month)
        self.monthEntry.grid(column=0, row = 0, sticky="E")

        self.slashLabel = ttk.Label(self.dateFrame, text="/")
        self.slashLabel.grid(column=1, row = 0, sticky="E")
        self.dayEntry = ttk.Spinbox(self.dateFrame, from_=1, to=31, width=3, textvariable=self.day)
        self.dayEntry.grid(column=2, row = 0, sticky="E")

        self.slashLabel2 = ttk.Label(self.dateFrame, text="/")
        self.slashLabel2.grid(column=3, row = 0, sticky="E")
        self.yearEntry = ttk.Spinbox(self.dateFrame,from_=1993, to=2100, width=5, textvariable=self.year)
        self.yearEntry.grid(column=4, row = 0)

    def createTransaction(self):
        a = T(businessName=self.businessName.get(),
              transactionType=self.transactionType.get(),
              month=self.month.get(),
              day=self.day.get(),
              year=self.year.get(),
              transactionMethod=self.transactionMethod.get(),
              transactionTotal=self.transactionTotal.get())
        
        #pass Transaction to database query builder
        
        print(a)
        self.__clear_fields__()

    def __clear_fields__(self):
        self.businessName.set("")
        self.transactionType.set("")
        self.month.set(datetime.now().month)
        self.day.set(value=datetime.now().day)
        self.year.set(value=datetime.now().year)
        self.transactionMethod.set("")
        self.transactionTotal.set("")



"""
TODO:
    
"""