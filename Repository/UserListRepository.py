from ListsApp.Model.UserList import UserList
from ListsApp.Repository.RepositoryMeta import RepositoryMeta

class UserListRepository(metaclass = RepositoryMeta):
    def __init__(self):
        self.collection = {}
    def create(self, name):
        user_list = UserList(name)
        self.collection[user_list.id] = user_list
        return user_list
    def delete(self, id):
        del self.collection[id]