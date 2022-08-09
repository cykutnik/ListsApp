from ListsApp.Model.UserListItem import UserListItem
from ListsApp.Repository.RepositoryMeta import RepositoryMeta

class UserListItemRepository(metaclass = RepositoryMeta):
    def __init__(self):
        self.collection = {}
    def create(self, name, price):
        item = UserListItem(name, price)
        self.collection[item.id]=item
    def delete(self, id):
        del self.collection[id]