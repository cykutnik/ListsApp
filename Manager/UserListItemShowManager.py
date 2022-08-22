from ListsApp.Repository.UserListItemRepository import UserListItemRepository

class UserListItemShowManager():
    def __new__(self, items):
        repository = UserListItemRepository()
        if(isinstance(items, list)):
            items_list = []
            for id in items:
                items_list.append(repository.collection[id])
            return items_list