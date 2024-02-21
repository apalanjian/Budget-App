
class BudgetCategory():

    def __init__(self, name = "") -> None:
        self.name = name
        self.size = 0
        self.transactions = []
        self.total = 0.0