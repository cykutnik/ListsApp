from ListsApp.Repository.UserListItemRepository import UserListItemRepository
from ListsApp.Repository.UserListRepository import UserListRepository

class UserListItemDeleteManager():
    def __init__(self, id):
        item_repository = UserListItemRepository()
        list_repository = UserListRepository()
        
        item = item_repository.collection[id]
        list_id = item.list_id
        user_list = list_repository.collection[list_id]
        user_list.items.remove(item.id)
        
        item_repository.delete(id)