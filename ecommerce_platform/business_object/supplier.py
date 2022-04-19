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
        
    
    def getSupplierID(self):
        return self.supplierID
    
    def setSupplierID(self, supplierID):
        self.supplierID = supplierID
        
    def getSupplierName(self):
        return self.supplierName
    
    def setSupplierName(self, supplierName):
        self.supplierName = supplierName
    
    def getContactName(self):
        return self.contactName
    
    def setContactName(self, contactName):
        self.contactName = contactName
        
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
        
    def getCity(self):
        return self.city
    
    def setCity(self, city):
        self.city = city
    
    def getPostalCode(self):
        return self.postalCode
    
    def setPostalCode(self, postalCode):
        self.postalCode = postalCode

    def getCountry(self):
        return self.country
    
    def setCountry(self, country):
        self.country = country
        
    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone
    
        