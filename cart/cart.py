from products.models import Products
from django.contrib import messages
from django.utils.translation import gettext as _


class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1, replace_quantity=False):
        """
        Add the specified product to the cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        elif replace_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('The product has been added to your cart'))
        self.save()

    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            messages.success(self.request, _('The product has been removed'))
            return True

    def save(self):
        """
        Mark session as modified to save changes
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        messages.success(self.request, _('Your Cart is clean'))
        self.save()

    def get_total_price(self):
        return sum(item['product_obj'].price * item['quantity'] for item in self.cart.values())
