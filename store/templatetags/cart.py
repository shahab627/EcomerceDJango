from django import template
from store.models.rate import Rate

register = template.Library()

amount =[]


@register.filter(name='is_in_cart')  # providing availabilty to index page
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            return True

    return False


@register.filter(name='cart_quantity')  # providing quantity to index page
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if id == str(product.id):
            return cart.get(id)

    return 0


@register.filter(name='total_price')  # sum of quantities and price
def total_price(product, cart):
    return product.price * cart_quantity(product, cart)


@register.filter(name='total_Amount')  # sum of all items
def total_Amount(product, cart):
    Sum = 0
    for p in product:
        Sum += total_price(p, cart)

    amount.append(Sum)
    return Sum


@register.filter(name='grand_total')
def grand_total(rate):

    g_total = round(amount[0] + (amount[0] * 0.1))
    return g_total


@register.filter(name='product_size')  # sum of all items
def product_size(product, size):
    if size is not None:
        keys = size.keys()
        for id in keys:
            if id == str(product.id):
                return size.get(id)

    return "Please Select Size !!"


@register.filter(name='get_ratting')
def get_ratting(product):
    rate = []
    rating = list(Rate.get_ratting(str(product.id)).values())
    for i in range(int(rating[0].get('rating'))):
        rate.append(i)
    return rate
