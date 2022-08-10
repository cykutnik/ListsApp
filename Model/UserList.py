class UserList:
    def __init__(self, name):
        self.name=name
        self.items=[] #contains items' ids
        self.id=id(self)