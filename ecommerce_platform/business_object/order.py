class order:
    def __init__(self, orderID, customerID, employeeID, orderDate, shipperID):
        self.orderID = orderID
        self.customerID = customerID
        self.employeeID = employeeID
        self.orderDate = orderDate
        self.shipperID = shipperID
        
    def getOrderID(self):
        return self.orderID
    
    def setOrderID(self, orderID):
        self.orderID = orderID
    
    def getCustomerID(self):
        return self.customerID
    
    def setCustomerID(self, customerID):
        self.customerID = customerID
        
    def getEmployeeID(self):
        return self.employeeID
    
    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID
        
    def getOrderDate(self):
        return self.orderDate
    
    def setOrderDate(self, orderDate):
        self.orderDate = orderDate
        
    def getShipperID(self):
        return self.shipperID
    
    def setShipperID(self, shipperID):
        self.shipperID = shipperID