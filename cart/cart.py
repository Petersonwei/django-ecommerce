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
