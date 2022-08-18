from ListsApp.Model.UserList import UserList

class UserListRepository():
    collection = {}
    
    def __init__(self):
        pass
    def create(self, name):
        user_list = UserList(name)
        self.collection[user_list.id] = user_list
        return user_list
    def delete(self, id):
        del self.collection[id]