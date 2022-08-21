from ListsApp.Repository.UserListRepository import UserListRepository

class UserListShowManager:
    def __new__(self, id = None):
        repository = UserListRepository()
        if (id):
            return repository.collection[id]
        else:
            return list(repository.collection.values())