from ListsApp.Controller.UserListController import UserListController
from ListsApp.Controller.UserListItemController import UserListItemController

c1 = UserListController()
c2 = UserListItemController()

c1.create('Pierwsza')
c1.show()
c2.create()
c2.create()
c1.delete()
c1.show()