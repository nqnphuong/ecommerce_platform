class shipper:
    def __init__(self, shipperID, shipperName, phone):
        self.shipperID = shipperID
        self.shipperName = shipperName
        self.phone = phone

        
    def getShipperID(self):
        return self.shipperID
    
    def setShipperID(self, shipperID):
        self.shipperID = shipperID
    
    def getShipperName(self):
        return self.shipperName
    
    def setShipperName(self, shipperName):
        self.shipperName = shipperName
        
    def getPhone(self):
        return self.phone
    
    def setPhone(self, phone):
        self.phone = phone
        