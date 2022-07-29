class UserListItemManager:
    def add_item(item: UserListItem, user_list: UserList):
        user_list.items[item.id]=item
        item.list_id=user_list.id
    def remove_item(item: UserListItem, user_list: UserList):
        del user_list.items[item.id]