import mysql.connector

class Connector():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tempSQLAP24!",
            database="Budget"
        )

        self.myCursor = self.mydb.cursor()


class LoadData():

    def __init__(self, categoryName):
        self.categoryName = categoryName

    def getCategory(self):
        pass

    def queryBuilder(self):
        pass


if __name__ == '__main__':
    test = Connector()