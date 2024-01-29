from django.views import View
from django.shortcuts import render
from store.models.orders import Order
from store.middlewares.auth import auth_midddleware
from django.utils.decorators import method_decorator

class OrderView(View):
    def get (self,request):
        customer=request.session.get('customer_id')
        orders=Order.get_order_by_customer(customer)
        return render(request,"orders.html",{"orders":orders})