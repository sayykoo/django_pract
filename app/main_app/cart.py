from django.contrib.sessions.backends.base import SessionBase
from .models import ShopModel

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'

    def __init__(self, session: dict) -> None:
        self.session : dict = session
        self.cart = self.session.get(self.CART_SESSION_ID)

        if not self.cart:
            self.cart = self.session[self.CART_SESSION_ID] = {}

    def __iter__(self):
        item_ids = self.cart.keys()
        items = ShopModel.objects.filter(id__in = itemkitch__ids)
        
        cart = self.cart.copy()
        
        for itemkitch in items:
            cart[str(itemkitch.id)]['itemkitch'] = itemkitch
            
        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session.modified = True
        
    def add(self, item_kitch, quantity = 1, update_quantity  = False):
        itemkitch_id = str(itemkitch.id)
        
        if itemkitch_id not in self.cart:
            self.cart[itemkitch_id] = {'quantity' : 0, 'price': itemkitch.price}
            
        if update_quantity:
            self.cart[itemkitch_id]['quantity'] = quantity
            
        else:
            self.cart[itemkitch_id]['quantity'] += quantity
            
        self.save()
        
    def remove(self, itemkitch):
        itemkitch_id = str(itemkitch.id)
        
        if itemkitch_id in self.cart:
            if self.cart[itemkitch_id]['quantity'] > 1:
                self.cart[itemkitch_id]['quantity'] -= 1
            else:
                del self.cart[itemkitch_id]
            self.save()
            
    def get_total_price(self):
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())
    
    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()
            