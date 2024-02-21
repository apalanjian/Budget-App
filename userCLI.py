
class userCLI():

    def __init__(self, categoryName = "") -> None:
        self.businessName = ""
        self.transactionType = categoryName
        self.month = 1
        self.day = 1
        self.year = 2024
        self.transactionMethod = ""
        self.transactionTotal = 0.0

    def getUserInput(self):
        # change to return an instance of Transaction
        print("Please enter the following:")
        self.businessName = input("Business: ")
        self.month = input("Month: ")
        self.day = input("Day: ")
        self.year = input("Year: ")
        self.transactionMethod = input("Payment Type: ")
        self.transactionTotal = float(input("Total: "))
        print()
