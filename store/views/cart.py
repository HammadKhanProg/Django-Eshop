from django.views import View
from django.shortcuts import render
from store.models.product import Product

class Cart (View):
    def get (self,request):
        ids=list(request.session.get("cart").keys())
        products=Product.objects.filter(id__in=ids)
        print(products)
        return render(request,"cart.html",{"products":products})