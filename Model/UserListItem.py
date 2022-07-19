class UserListItem:
    def __init__(self, name: str, price):
        self.name=name
        self.price=price
        self.id=id(self)
        self.list_id=None