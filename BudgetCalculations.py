from BudgetCategory import *

def sumTotals(cat = BudgetCategory()) -> float:
    sum = 0.0
    for i in cat.transactions:
        sum += i.transactionTotal

    return sum