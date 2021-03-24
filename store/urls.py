
from django.contrib import admin
from django.urls import path
from .views import home,signup,login,cart,checkout,orders
from .views.login import logout


urlpatterns = [
    path('',home.Index.as_view(),name ='Homepage'),
    path('SignUp',signup.SignUp.as_view(), name = 'signup'),
    path('login',login.Login.as_view(),name = 'login'),
    path('logout',logout,name = 'logout'),
    path('Cart',cart.Cart.as_view(), name ='cart'),
    path('check-out',checkout.CheckOut.as_view(), name ='checkout'),
    path('orders', orders.OrderView.as_view(), name ='order')

]
