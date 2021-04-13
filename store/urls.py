
from django.contrib import admin
from django.urls import path
from .views import home,signup,login,cart,checkout,orders,RateReview,Details
from .views.login import logout
from  store.middlewares.auth import auth_middleware
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',home.Index.as_view(),name ='Homepage'),
    path('SignUp',signup.SignUp.as_view(), name = 'signup'),
    path('login',login.Login.as_view(),name = 'login'),
    path('logout',logout,name = 'logout'),
    path('Cart',auth_middleware(cart.Cart.as_view()), name ='cart'),
    path('check-out',checkout.CheckOut.as_view(), name ='checkout'),
    path('orders', auth_middleware(orders.OrderView.as_view()), name ='order'),
    path('ratereview', RateReview.RateReview.as_view(), name='RateReview'),
    path('ratereview/<str:productID>/', RateReview.RateReview.as_view(), name='RateReview'),
    path('details/<str:productID>/', Details.Details.as_view(), name='Details'),
    path('details', Details.Details.as_view(), name='Details')

]

urlpatterns += staticfiles_urlpatterns()