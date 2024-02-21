from Transaction import *
from BudgetCategory import *
from BudgetCalculations import *
from userCLI import userCLI
from MainFrame import MainFrame

if __name__ == '__main__':
    mainWin = MainFrame()
    mainWin.mainLoop()

    a = Transaction(
        businessName = "Walmart", transactionType = "Household",
        month = 2, day = 20,
        transactionMethod = "Credit",
        transactionTotal = 60.34
        )
    
    # b = userCLI.getUserInput(categoryName="Household")

    category = BudgetCategory('Household')
    category.transactions.append(a)
    # category.transactions.append(b)


    
    print(f"{category.name}: {sumTotals(category):.2f}")
    for i in category.transactions:
        print(f"\t{i}")

