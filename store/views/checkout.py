from django.views import View
from django.shortcuts import render,redirect
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer


class Checkout(View):
    def post (self,request):
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        customer=request.session.get("customer_id")
        cart=request.session.get("cart")
        products=Product.products_id(list(cart.keys()))
        # print(address,phone,customer,cart)
        

        for product in products:
            order=Order(product=product,
                        customer=Customer(id=customer),
                        quantity=cart.get(str(product.id)),
                        price=product.price,
                        address=address,
                        phone=phone,
                        )
            order.save()
        request.session["cart"]={}

        return redirect ('cart')