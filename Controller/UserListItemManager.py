from ListApp.Model.UserList import UserList
from ListApp.Model.UserListItem import UserListItem

class UserListItemManager:
    def add_item(item: UserListItem, user_list: UserList):
        user_list.items.append(item)
    def remove_item(item: UserListItem, user_list: UserList):
        user_list.items.remove(item)