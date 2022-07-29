from ListsApp.Model.UserList import UserList

class UserListRepository:
    def __init__(self):
        self.collection = {}
    def create(self, name):
        user_list = UserList(name)
        self.collection[user_list.id] = user_list
    def delete(self, id):
        del self.collection[id]