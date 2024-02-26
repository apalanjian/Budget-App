
class Transaction():

    def __init__(self, businessName = "", transactionType = "",
                 month = 1, day = 1, year = 2024,
                 transactionMethod = "",
                 transactionTotal = 0.0) -> None:
        self.businessName = businessName
        self.transactionType = transactionType
        self.month = month
        self.day = day
        self.year = year
        self.transactionMethod = transactionMethod
        self.transactionTotal = transactionTotal
        self.transactionId = 0

    def __repr__(self) -> str:
        return (f"Transaction [Business: {self.businessName}, " + 
                f"Type: {self.transactionType}, " +
                f"Date: {self.month}/{self.day}/{self.year}, " +
                f"Payment: {self.transactionMethod}, " +
                f"Total: {self.transactionTotal}]")