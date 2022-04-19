class Customer:
    def __init__(self, customerID, customerEmail, password, customerName, contactName, address, city, postalCode,
                 country):
        self.customerID = customerID
        self.customerEmail = customerEmail
        self.password = password
        self.customerName = customerName
        self.contactName = contactName
        self.address = address
        self.city = city
        self.postalCode = postalCode
        self.country = country

    def getCustomerID(self):
        return self.customerID

    def setCustomerID(self, customerID):
        self.customerID = customerID

    def getCustomerEmail(self):
        return self.customerEmail

    def setCustomerEmail(self, customerEmail):
        self.customerEmail = customerEmail

    def getPassword(self):
        return self.password

    def setPassword(self, Password):
        self.password = Password

    def getCustomerName(self):
        return self.customerName

    def setCustomerName(self, customerName):
        self.customerName = customerName

    def getContactName(self):
        return self.customerID

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
