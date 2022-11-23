from ListsApp.Model.UserListItem import UserListItem

class UserListItemRepository():
    collection = {}
    
    def __init__(self):
        pass
    def create(self, name, price):
        item = UserListItem(name, price)
        self.collection[item.id]=item
        return item
    def delete(self, id):
        del self.collection[id]
    def get(self, id):
        item = self.collection[id]
        return [item.id, item.name, item.price, item.list_id]