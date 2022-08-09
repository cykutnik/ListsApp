from ListsApp.Model.UserList import UserList
from ListsApp.View.UserListItemView import UserListItemView

class UserListView():
    def display(self, user_lists):
        if(len(user_lists)>1):
            for user_list in user_lists:
                print('{}. {}'.format(user_list.id,user_list.name.upper()))
            return int(input('Pokaż szczegóły dla listy numer: '))
        elif(len(user_lists)==1):
            print('{}: '.format(user_lists[0].name.upper()))
            for item in user_lists[0].items.values():
                UserListItemView(item)
        else:
            pass #tutaj blad, bo nie mozna wypisac zawartosci listy o dlugosci 0