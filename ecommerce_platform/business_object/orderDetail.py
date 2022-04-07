class orderDetail:
    def __init__(self, orderDetailID, orderID, productID, quantity):
        self.orderDetailID = orderDetailID
        self.orderID = orderID
        self.productID = productID
        self.quantity = quantity
        
    def getorderDetailID(self):
        return self.orderDetailID
    
    def setorderDetailID(self, orderDetailID):
        self.orderDetailID = orderDetailID
        
    def getcorderID(self):
        return self.orderID
    
    def setorderID(self, orderID):
        self.orderID = orderID
    
    def getproductID(self):
        return self.productID
    
    def setproductID(self, productID):
        self.productID = productID
        
    def getquantity(self):
        return self.quantity
    
    def setquantity(self, quantity):
        self.quantity = quantity