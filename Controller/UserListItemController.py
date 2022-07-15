from Model.UserListItem import UserListItem

class UserListItemController:
    def create(name: str, price):
        return UserListItem(name,price)
    def delete(item: UserListItem):
        del item
    #update_item? zmiana price, zmiana name
    #walidacja ceny nie na tym poziomie - na view
    #przy delete cos, zeby nie probowalo usunac nieistniejacego
    #przedmiotu - w tej klasie czy w nowej?