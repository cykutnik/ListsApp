from ListsApp.Manager.UserListDeleteManager import UserListDeleteManager
from ListsApp.Manager.UserListCreateManager import UserListCreateManager
from ListsApp.Manager.UserListShowManager import UserListShowManager
from ListsApp.Manager.UserListItemShowManager import UserListItemShowManager
from ListsApp.View.UserListView import UserListView
from ListsApp.View.UserListItemView import UserListItemView

class UserListController:
    def __init__(self):
        self.view = UserListView()
    def create(self, name = None): 
        if(name):
            UserListCreateManager(name)
        else:
            name = input('Podaj nazwę: ') #tu bedzie bralo z view
            self.create(name)
    def delete(self, id = None):
        if(id):
            UserListDeleteManager(id)
        else:
            id = int(input('Podaj id: ')) #zamienic w przyszlosci na view
            self.delete(id)
    def show(self, id = None):
        if(id):
            user_list = UserListShowManager(id)
            self.view.display(user_list)
            items_list = UserListItemShowManager(user_list.items)
            UserListItemView(items_list)
        else:
            user_lists = UserListShowManager()
            id = self.view.display(user_lists)
            if(id):
                self.show(id)