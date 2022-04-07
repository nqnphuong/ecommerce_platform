class shipper:
    def __init__(self, shipperID, shipperName, phone):
        self.shipperID = shipperID
        self.shipperName = shipperName
        self.phone = phone

        
    def getcorderID(self):
        return self.orderID
    
    def setorderID(self, orderID):
        self.orderID = orderID
    
    def getcustomerID(self):
        return self.customerID
    
    def setcustomerID(self, customerID):
        self.customerID = customerID
        
    def getemployeeID(self):
        return self.employeeID
    
    def setemployeeID(self, employeeID):
        self.employeeID = employeeID
        
    def getorderDate(self):
        return self.orderDate
    
    def setorderDate(self, orderDate):
        self.orderDate = orderDate
        
    def getshipperID(self):
        return self.shipperID
    
    def setshipperID(self, shipperID):
        self.shipperID = shipperID