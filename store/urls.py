from .views.home import Index
from .views.login import Login
from .views.login import logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import Checkout
from .views.order import OrderView
from django.urls import path
from .middlewares.auth import auth_midddleware

urlpatterns = [
    path("",Index.as_view(),name="home"),
    path("signup/",Signup.as_view(),name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("logout/", logout ,name="logout"),
    path("cart/",Cart.as_view(),name="cart"),
    path("check-out/",auth_midddleware(Checkout.as_view()),name="check-out"), 
    path("orders/",auth_midddleware(OrderView.as_view()),name="orders"), 
] 
