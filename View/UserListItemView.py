from ListsApp.Model.UserListItem import UserListItem

class UserListItemView():
    def __init__(self, item_list):
        if(isinstance(item_list,list)):
            for item in item_list:
                print('{}. {}'.format(item.id,item.name.upper()))