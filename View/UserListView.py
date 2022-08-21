from ListsApp.View.UserListItemView import UserListItemView

class UserListView():
    def display(self, user_lists):
        if(isinstance(user_lists, list)):
            if(len(user_lists)>0):
                for user_list in user_lists:
                    print('{}. {}'.format(user_list.id,user_list.name.upper()))
                return int(input('Pokaż szczegóły dla listy numer: '))
            else:
                print('Brak list do wyświetlenia')
        else:
            print('{}: '.format(user_lists.name.upper()))
            for id in user_lists.items:
                UserListItemView(id)