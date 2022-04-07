class supplier:
    def __init__(self, supplierID, supplierName, contactName, address, city, postalCode, country, phone):
        self.supplierID = supplierID
        self.supplierName = supplierName
        self.contactName = contactName
        self.address = address
        self.city = city
        self.postalCode = postalCode
        self.country = country
        self.phone = phone
        
    
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
        