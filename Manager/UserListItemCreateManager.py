from ListsApp.Repository.UserListItemRepository import UserListItemRepository

class UserListItemCreateManager():
    def __init__(self, name, price):
        self.repository = UserListItemRepository()
        self.repository.create(name, price)
        #jesli chce tutaj dodac item do listy i list_id do item, to jak mam sie odnosic do niego?