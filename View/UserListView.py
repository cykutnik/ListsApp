from Model.UserList import UserList
from ListsApp.Model.UserListItem import UserListItem

class UserListView():
    def display(user_list):
        print('  {}: '.format(user_list.name.upper()))
        for item in user_list:
            print('- {}: {} zł'.format(item.name,item.price))