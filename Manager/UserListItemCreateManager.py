from ListsApp.Repository.UserListItemRepository import UserListItemRepository

class UserListItemCreateManager():
    def __init__(self, name, price):
        self.repository = UserListItemRepository()
        item = self.repository.create(name, price)
        #dodac item id do listy i list id do item