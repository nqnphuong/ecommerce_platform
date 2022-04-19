class product:
    def __init__(self, productID, productName, supplierID, categoryID, unit, price):
        self.productID = productID
        self.productName = productName
        self.supplierID = supplierID
        self.categoryID = categoryID
        self.unit = unit
        self.price = price
        
    def getProductID(self):
        return self.productID
    
    def setProductID(self, productID):
        self.productID = productID
    
    def getProductName(self):
        return self.productName
    
    def setProductName(self, productName):
        self.productName = productName
        
    def getSupplierID(self):
        return self.supplierID
    
    def setSupplierID(self, supplierID):
        self.supplierID = supplierID
        
    def getCategoryID(self):
        return self.categoryID
    
    def setCategoryID(self, categoryID):
        self.categoryID = categoryID
        
    def getUnit(self):
        return self.unit
    
    def setUnit(self, unit):
        self.unit = unit
        
    def getPrice(self):
        return self.price
    
    def setPrice(self, price):
        self.price = price