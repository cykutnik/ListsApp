from Model.UserListItem import UserListItem

class UserListItemRepository:
    def __init__(self):
        self.repository={}
    def add(self, item: UserListItem):
        self.repository[item.id]=item
    def remove(self, item: UserListItem):
        del self.repository[item.id]