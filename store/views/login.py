from django.views import View
from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect


class Login (View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get("return_url")
        return render(request,"login.html")
    
    def post (self,request):
        username=request.POST.get("username")
        password=request.POST.get("password1")
        customer=Customer.get_costomer_by_name(username)
        errormessage=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session["customer_id"]=customer.id
                if Login.return_url:
                     return HttpResponseRedirect(Login.return_url)
                else:
                    return redirect("home")
            else:
                errormessage="Invalid Email or Password"
        else:
            errormessage="Invalid Email or Password"

        data={
            "error":errormessage,
        }
        print("You Are : ",request.session.get("customer_email"))
        return render (request,"login.html",data)
    
def logout (request):
        request.session.clear()
        return redirect ("login")