from ListsApp.Repository.UserListItemRepository import UserListItemRepository
from ListsApp.Repository.UserListRepository import UserListRepository

class UserListItemCreateManager():
    def __init__(self, name, price, list_id):
        item_repository = UserListItemRepository()
        list_repository = UserListRepository()
        
        item = item_repository.create(name, price)
        user_list = list_repository.collection[list_id]
        user_list.items.append(item.id)
        item.list_id = list_id