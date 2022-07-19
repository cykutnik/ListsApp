from ListsApp.Model.UserList import UserList
from ListsApp.Repository.UserListRepository import UserListRepository

class UserListControl:
    def create(name: str, repo: UserListRepository):
        user_list=UserList(name)
        repo.add(user_list)
        return user_list
    def delete(user_list: UserList, repo: UserListRepository):
        del repo.remove(user_list)
        del user_list