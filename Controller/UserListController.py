from ListsApp.Repository.UserListRepository import UserListRepository
from ListsApp.View.UserListView import UserListView

class UserListController:
    def __init__(self):
        self.repository = UserListRepository()
        self.view = UserListView()
    def create(self, name = None): 
        if(name):
            self.repository.create(name)
        else:
            name = input('Podaj nazwę: ') #tu bedzie bralo z view
            self.create(name)
    # def delete(user_list: UserList, repo: UserListRepository):
    #     repo.remove(user_list)
    #     del user_list
    def show(self, id = None):
        if(id):
            user_list = self.repository.collection[id]
            self.view.display([user_list])
        else:
            user_lists = self.repository.collection.values()
            id = self.view.display(user_lists)
            self.show(id)