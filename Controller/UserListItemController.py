from ListsApp.Manager.UserListItemCreateManager import UserListItemCreateManager
from ListsApp.Manager.UserListItemDeleteManager import UserListItemDeleteManager

class UserListItemController:
    def __init__(self):
        pass #tu bedzie jakis view i te sprawy
    def create(self, name = None, price = None, list_id = None):
        if(name and price and list_id):
            UserListItemCreateManager(name, price, list_id)
        elif(name == None):
            name = input("Podaj nazwę przedmiotu: ") #zamiana na view
            self.create(name, price, list_id)
        elif(price == None):
            price = input("Podaj cenę przedmiotu: ") #zamiana na view
            self.create(name, price, list_id)
        else:
            list_id = input("Podaj id listy: ") #zamiana na view
            self.create(name, price, list_id)
    def delete(self, id = None):
        if(id):
            UserListItemDeleteManager(id)
        else:
            id = input('Podaj id: ') #zamiana na view
            self.delete(id)
    # def update_name(item: UserListItem, name):
    #     item.name=name
    # def update_price(item: UserListItem, price):
    #     item.price=price