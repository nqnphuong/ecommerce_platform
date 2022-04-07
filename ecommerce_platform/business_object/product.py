class product:
    def __init__(self, productID, productName, supplierID, categoryID, unit, price):
        self.productID = productID
        self.productName = productName
        self.supplierID = supplierID
        self.categoryID = categoryID
        self.unit = unit
        self.price = price
        
    def getproductID(self):
        return self.orderID
    
    def setproductID(self, productID):
        self.productID = productID
    
    def getproductName(self):
        return self.productName
    
    def setproductName(self, productName):
        self.productName = productName
        
    def getsupplierID(self):
        return self.supplierID
    
    def setsupplierID(self, supplierID):
        self.supplierID = supplierID
        
    def getcategoryID(self):
        return self.categoryID
    
    def setcategoryID(self, categoryID):
        self.categoryID = categoryID
        
    def getunit(self):
        return self.unit
    
    def setunit(self, unit):
        self.unit = unit
        
    def getprice(self):
        return self.price
    
    def setprice(self, price):
        self.price = price