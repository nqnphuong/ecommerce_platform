class category:
    def __init__(self, categoryID, categoryName, description):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.description = description

    def getCategoryID(self):
        return self.categoryID

    def setCategoryID(self, categoryID):
        self.categoryID = categoryID

    def getCategoryName(self):
        return self.categoryName

    def setCategoryName(self, categoryName):
        self.categoryName = categoryName

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

