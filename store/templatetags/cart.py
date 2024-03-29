from django import template
register=template.Library()


@register.filter(name="is_in_cart")
def is_in_cart (product,cart):
    keys=cart.keys()
    for id in keys:
        if id == str(product.id):
            return True
    return False

@register.filter(name="cart_count")
def cart_count (product,cart):
    keys=cart.keys()
    for id in keys:
        if id == str(product.id):
            return cart.get(id)
    return 0

@register.filter(name="price")
def price (product,cart):
    return product.price * cart_count(product,cart)


@register.filter(name="total")
def total (products,cart):
    sum=0
    for p in products:
        sum += price(p,cart)
    return sum