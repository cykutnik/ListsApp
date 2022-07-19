from Model.UserList import UserList

class UserListRepository:
    def __init__(self):
        self.repository={}
    def add(self, user_list: UserList):
        self.repository[user_list.id]=user_list
    def remove(self, user_list: UserList):
        del self.repository[user_list.id]