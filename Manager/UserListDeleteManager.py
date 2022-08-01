from ListsApp.Repository.UserListRepository import UserListRepository
from ListsApp.Repository.UserListItemRepository import UserListItemRepository

class UserListDeleteManager:
    def __init__(self,id):
        self.list_repository = UserListRepository()
        self.item_repository = UserListItemRepository()