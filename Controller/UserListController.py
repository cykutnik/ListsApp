from ListsApp.Model.UserList import UserList
from ListsApp.Model.UserListRepository import UserListRepository

class UserListControl:
    def create(name: str, repo: UserListRepository):
        user_list=UserList(name)
        repo.repository[id(user_list)]=user_list
        return user_list
    def delete(user_list: UserList):
        del user_list