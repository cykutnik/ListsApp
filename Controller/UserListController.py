from ListApp.Model.UserList import UserList

class UserListControl:
    def create(name: str):
        return UserList(name)
    def delete(user_list: UserList):
        del user_list