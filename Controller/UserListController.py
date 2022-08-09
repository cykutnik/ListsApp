from ListsApp.Manager.UserListDeleteManager import UserListDeleteManager
from ListsApp.Manager.UserListCreateManager import UserListCreateManager
from ListsApp.View.UserListView import UserListView

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
            id = input('Podaj id: ') #zamienic w przyszlosci na view
            self.delete(id)
    def show(self, id = None):
        if(id):
            user_list = self.repository.collection[id] #userlistshowmanager
            self.view.display([user_list])
        else:
            user_lists = self.repository.collection.values()
            id = self.view.display(user_lists)
            self.show(id)