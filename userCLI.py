from Transaction import Transaction
class userCLI():

    @staticmethod   
    def getUserInput(categoryName = ""):
        
        print("Please enter the following:")
        bN = input("Business: ")
        m = input("Month: ")
        d = input("Day: ")
        y = input("Year: ")
        tM = input("Payment Type: ")
        tT = float(input("Total: "))
        print()

        return Transaction(
            businessName = bN, 
            transactionType = categoryName,
            month = m,
            day = d,
            year = y,
            transactionMethod = tM,
            transactionTotal = tT
        )
