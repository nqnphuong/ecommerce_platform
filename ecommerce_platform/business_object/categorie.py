class categoryID:
    def __init__(self, categoryID, categoryName, description):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.description = description
        
    
    def getcategoryID(self):
        return self.categoryID
    
    def setcategoryID(self, categoryID):
        self.categoryID = categoryID
        
    def getcategoryName(self):
        return self.categoryName
    
    def setcategoryName(self, categoryName):
        self.categoryName = categoryName
    
    def getdescription(self):
        return self.description
    
    def setdescription(self, description):
        self.description = description
        