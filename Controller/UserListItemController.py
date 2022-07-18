from Model.UserListItem import UserListItem
from Repository.UserListItemRepository import UserListItemRepository

class UserListItemController:
    def create(name: str, price, list_id, repo: UserListItemRepository):
        user_list_item=UserListItem(name,price)
        repo.repository[user_list_item.id]=user_list_item
        user_list_item.list_id=list_id
        return user_list_item
    def delete(item: UserListItem, repo: UserListItemRepository):
        del repo.repository[item.id]
        del item
    #update_item? zmiana price, zmiana name
    #walidacja ceny nie na tym poziomie - na view
    #przy delete cos, zeby nie probowalo usunac nieistniejacego
    #przedmiotu - w tej klasie czy w nowej?