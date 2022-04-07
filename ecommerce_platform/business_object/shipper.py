class shipper:
    def __init__(self, shipperID, shipperName, phone):
        self.shipperID = shipperID
        self.shipperName = shipperName
        self.phone = phone

        
    def getcshipperID(self):
        return self.shipperID
    
    def setshipperID(self, shipperID):
        self.shipperID = shipperID
    
    def getshipperName(self):
        return self.shipperName
    
    def setshipperName(self, shipperName):
        self.shipperName = shipperName
        
    def getphone(self):
        return self.phone
    
    def setphone(self, phone):
        self.phone = phone
        