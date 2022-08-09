from ListsApp.Repository.UserListRepository import UserListRepository
from ListsApp.Repository.UserListItemRepository import UserListItemRepository

class UserListDeleteManager:
    def __init__(self, id):
        list_repository = UserListRepository()
        item_repository = UserListItemRepository()
        count = len(list_repository.collection[id].items)
        for item in item_repository.collection.values():
            if item.list_id == id:
                item_repository.delete(item.id)
                count = count - 1
            if count == 0:
                break
        list_repository.delete(id)