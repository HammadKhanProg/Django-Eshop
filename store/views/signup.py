from django.views import View
from django.shortcuts import render,redirect
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password,make_password

class Signup (View):
    def get (self,request):
        return render(request,"signup.html")
    def post (self,request):
        uname=request.POST.get('username')
        uemail=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        customer = Customer(username=uname,
                            email=uemail,
                            password=pass1,
                            confirm_password=pass2)
        errormessage=self.ValidateCustomer(customer)
            # for filling form after errror
        value={
                "uname":uname,
                "uemail":uemail,
                "pass1":pass1,
                "pass2":pass2,
            }
            
            # saving
        if not errormessage:
            customer.password=make_password(customer.password)
            customer.confirm_password=make_password(customer.confirm_password)
            customer.register()
            return redirect ("login")
        else:
            data={
                    'error': errormessage,
                    'values':value
                }
            return render(request, 'signup.html',data)
        

    def ValidateCustomer (self,customer,):
        errormessage=None
        if not customer.username:
            errormessage="User Name Required"
        elif len(customer.username) < 4:
            errormessage="User Name should be atleast 4 characters Long"
        elif not customer.password:
            errormessage="Enter Password Please"
        elif not customer.confirm_password:
            errormessage="Enter Confirm Password Please"
        elif customer.password!=customer.confirm_password:
            errormessage="Passwords does not match"
        # for email validatons
        elif customer.is_exits():
            errormessage="Email already eixts"

        return errormessage