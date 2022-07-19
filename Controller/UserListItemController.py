from Model.UserListItem import UserListItem
from Repository.UserListItemRepository import UserListItemRepository

class UserListItemController:
    def create(name: str, price, list_id, repo: UserListItemRepository):
        user_list_item=UserListItem(name,price)
        repo.add(user_list_item)
        user_list_item.list_id=list_id
        return user_list_item
    def delete(item: UserListItem, repo: UserListItemRepository):
        repo.remove(item)
        del item
    def update_name(item: UserListItem, name):
        item.name=name
    def update_price(item: UserListItem, price):
        item.price=price
        
    #przy delete cos, zeby nie probowalo usunac nieistniejacego
    #przedmiotu - w tej klasie czy w nowej?