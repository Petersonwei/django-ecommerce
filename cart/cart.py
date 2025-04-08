from decimal import Decimal
from store.models import Product


class Cart():

    def __init__(self, request):
        self.session = request.session


        # Returning User Get the cart from the existing session
        cart = self.session.get('session_key')

        # New User Create a new cart

        if 'session_key' not in request.session:

            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, product_qty):

        # Convert the product ID to a string to use as a dictionary key
        product_id = str(product.id)

        # Check if the product is already in the cart
        if product_id in self.cart:
            # If product exists, update the quantity
            self.cart[product_id]['qty'] = product_qty
        else:
            # If product doesn't exist in cart, add it with price and quantity
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True

    def __len__(self):
        """
        Get the cart data and count the quantity of items
        """
        return sum(item['qty'] for item in self.cart.values())

    
    def __iter__(self):
        """
        Create a for loop iteration
        """
        all_product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=all_product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item
