class employee:
    def __init__(self, employeeID, lastName, firstName, birthDate, photo, notes):
        self.employeeID = employeeID
        self.lastName = lastName
        self.firstName = firstName
        self.birthDate = birthDate
        self.photo = photo
        self.notes = notes

    def getEmployeeID(self):
        return self.employeeID

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getBirthDate(self):
        return self.birthDate

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def getPhoto(self):
        return self.photo

    def setPhoto(self, photo):
        self.photo = photo

    def getNotes(self):
        return self.notes

    def setNotes(self, notes):
        self.notes = notes
