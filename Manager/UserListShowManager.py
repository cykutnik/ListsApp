from ListsApp.Repository.UserListRepository import UserListRepository

class UserListShowManager:
    def __init__(self, id = None):
        repository = UserListRepository()
        if (id):
            return repository.collection[id]
        else:
            return repository.collection.values