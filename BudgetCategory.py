
class BudgetCategory():

    def __init__(self, name = "") -> None:
        self.name = name
        self.size = 0
        self.transactions = []
        self.total = 0.0

    def sumTotals(self):
        self.total = 0.0
        for i in self.transactions:
            self.total += i.transactionTotal