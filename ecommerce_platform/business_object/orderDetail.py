class orderDetail:
    def __init__(self, orderDetailID, orderID, productID, quantity):
        self.orderDetailID = orderDetailID
        self.orderID = orderID
        self.productID = productID
        self.quantity = quantity
        
    def getOrderDetailID(self):
        return self.orderDetailID
    
    def setOrderDetailID(self, orderDetailID):
        self.orderDetailID = orderDetailID
        
    def getOrderID(self):
        return self.orderID
    
    def setOrderID(self, orderID):
        self.orderID = orderID
    
    def getProductID(self):
        return self.productID
    
    def setProductID(self, productID):
        self.productID = productID
        
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity):
        self.quantity = quantity