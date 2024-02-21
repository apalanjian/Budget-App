import openpyxl
from Transaction import *
from BudgetCategory import *
from BudgetCalculations import *
from userCLI import userCLI

if __name__ == '__main__':
    a = Transaction(
        businessName = "Walmart", transactionType = "Household",
        month = 2, day = 20,
        transactionMethod = "Credit",
        transactionTotal = 60.34
        )
    temp = userCLI(categoryName="Household")
    temp.getUserInput()
    b = Transaction(
        businessName = temp.businessName, transactionType = temp.transactionType,
        month = temp.month, day = temp.day, year = temp.year,
        transactionMethod = temp.transactionMethod,
        transactionTotal = temp.transactionTotal
    )
    
    category = BudgetCategory('Household')
    category.transactions.append(a)
    category.transactions.append(b)


    
    print(f"{category.name}: {sumTotals(category)}")
    for i in category.transactions:
        print(f"\t{i}")

