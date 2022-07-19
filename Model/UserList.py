class UserList:
    def __init__(self, name):
        self.name=name
        self.items={}
        self.id=id(self)