from ListsApp.Model.UserListItem import UserListItem

class UserListItemView():
    def __init__(self, item: UserListItem):
        print("{}. {}: {}".format(item.id, item.name, item.price))