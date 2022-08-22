from ListsApp.Repository.UserListRepository import UserListRepository

class UserListCreateManager:
    def __init__(self, name):
        repository = UserListRepository()
        repository.create(name)