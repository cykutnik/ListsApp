from Model.UserList import UserList
from ListsApp.Model.UserListItem import UserListItem

class UserListView():
    def display(user_list: UserList):
        print('  {}: '.format(user_list.name.upper()))
        for item in user_list.items.values():
            print('- {}: {} zł'.format(item.name,item.price))