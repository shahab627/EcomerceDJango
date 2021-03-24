from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.oreders import Order
from django.views import View  # import for class based views


class CheckOut(View):
    def get(self, request):
        pass

    def post(self, request):
        # getting data to place order
        # data obtain thro Ajax
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        customer = request.session.get('customer_email')
        mail = request.session.get('customer_email')
        if mail:
            currentCustomer = Customer.get_customer_by_mail(mail)

        cart = request.session.get('cart')
        size = request.session.get('size')
        products = Product.get_all_products_by_id(list(cart.keys()))

        for product in products:

            if size.get(str(product.id)) is not None:
                order = Order(customer=currentCustomer,
                              product=product,
                              productName=product.name,
                              price=product.price,
                              quantity=cart.get(str(product.id)),
                              phone=phone,
                              address=address,
                              size=size.get(str(product.id))
                )
                order.placeOrder()

        request.session['cart'] = {}
        request.session['size'] = {}

        return redirect('Homepage')
