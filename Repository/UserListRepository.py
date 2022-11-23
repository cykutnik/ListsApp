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
    def get(self, id):
        user_list = self.collection[id]
        return [user_list.id, user_list.name]