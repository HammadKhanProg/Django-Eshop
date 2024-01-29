from django.views import View
from store.models.category import Category
from store.models.product import Product
from django.shortcuts import render,redirect
from django.views import View

class Index (View):

    def post (self,request):
        product_id=request.POST.get("product")
        cart=request.session.get("cart")
        rem=request.POST.get("remove")
        if cart:
            quantity=cart.get(product_id)
            if quantity:
                if rem:
                    if quantity<=1:
                        cart.pop(product_id)
                    else:
                        cart[product_id]= quantity-1
                else:
                    cart[product_id]= quantity+1
            else:
                cart[product_id]=1
        else:
            cart={}
            cart[product_id]=1

        request.session["cart"]=cart
        return redirect ("home")


    def get(self,request):
        
        data={}
        product=None
        category=Category.objects.all()
        categoryid=request.GET.get("category")
        if categoryid:
            product=Product.get_all_products_by_id(categoryid)
        else:
            product=Product.get_all_products()


        data={
            "product":product,
            "category":category,
        }
        return render (request,"index.html",data)
    