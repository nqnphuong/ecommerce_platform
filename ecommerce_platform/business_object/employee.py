class employee:
    def __init__(self, employeeID, lastName, firstName, birthDate, photo, notes):
        self.employeeID = employeeID
        self.lastName = lastName
        self.firstName = firstName
        self.birthDate = birthDate
        self.photo = photo
        self.notes = notes

    def getemployeeID(self):
        return self.employeeID
    
    def setemployeeID(self, employeeID):
        self.employeeID = employeeID
        
    def getlastName(self):
        return self.lastName
    
    def setlastName(self, lastName):
        self.lastName = lastName
    
    def getfirstName(self):
        return self.firstName
    
    def setfirstName(self, firstName):
        self.firstName = firstName
        
    def getbirthDate(self):
        return self.birthDate
    
    def setbirthDate(self, birthDate):
        self.birthDate = birthDate
        
    def getphoto(self):
        return self.photo
    
    def setphoto(self, photo):
        self.photo = photo

    def getnotes(self):
        return self.notes
    
    def setnotes(self, notes):
        self.notes = notes