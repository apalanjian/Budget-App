import sqlite3

class Connector():

    def __init__(self):
        self.connection = sqlite3.connect("budget.db")
        self.cursor = self.connection.cursor()

class BuildTables():

    def __init__(self, con = Connector()) -> None:
        self.cursor = con.cursor

    def __create_category_table__(self):
        self.cursor.execute("CREATE TABLE Categories(name category id total)")

class LoadData():

    def __init__(self, categoryName):
        self.categoryName = categoryName

    def getCategory(self):
        pass

    def queryBuilder(self):
        pass


if __name__ == '__main__':
    test = Connector()