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
        
    
    def getsupplierID(self):
        return self.supplierID
    
    def supplierID(self, supplierID):
        self.supplierID = supplierID
        
    def getsupplierName(self):
        return self.supplierName
    
    def setsupplierName(self, supplierName):
        self.supplierName = supplierName
    
    def getcontactName(self):
        return self.contactName
    
    def setcontactName(self, contactName):
        self.contactName = contactName
        
    def getaddress(self):
        return self.address
    
    def setaddress(self, address):
        self.address = address
        
    def getcity(self):
        return self.city
    
    def setcity(self, city):
        self.city = city
    
    def getpostalCode(self):
        return self.postalCode
    
    def setpostalCode(self, postalCode):
        self.postalCode = postalCode

    def getcountry(self):
        return self.country
    
    def setcountry(self, country):
        self.country = country
        
    def getphone(self):
        return self.phone
    
    def setphone(self, phone):
        self.phone = phone
    
        