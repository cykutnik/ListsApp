from ListsApp.Repository.UserListRepository import UserListRepository

class UserListCreateManager:
    def __init__(self,name):
        self.repository = UserListRepository()
        self.repository.create(name)