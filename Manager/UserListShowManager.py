from ListsApp.Repository.UserListRepository import UserListRepository

class UserListShowManager:
    def __init__(self,id = None):
        self.repository = UserListRepository()
        if (id):
            return self.repository.collection[id]
        else:
            return self.repository.collection