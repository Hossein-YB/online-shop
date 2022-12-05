from products.models import Products

class Cart:
    """shop cart"""
    def __init__(self, request):
        """ Initialize  cart """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity):
        """Add product in the cart"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]: {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """remove product from cart"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """ Save changes in the session"""
        self.session.modified = True

    def clear(self):
        """delete cart"""
        del self.session['cart']
        self.save()

    def __iter__(self):
        """get product object in cart"""
        product_ids = self.cart.keys()

        cart = self.cart.copy()

        products = Products.objects.filter(id__in=product_ids)

        for product in products:
            cart[str(product.id)]['product_object'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        """return len object in the cart"""
        return len(self.cart.keys())

    def get_total_price(self):
        """return total products in the cart"""
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)
        
        return sum(product.price for product in products)
