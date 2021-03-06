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
        status = "save"
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        mail = request.session.get('customer_email')
        price = request.POST.get('Price')

        if address is "" or phone is "":
            status = "not save"

        if mail:
            currentCustomer = Customer.get_customer_by_mail(mail)

        cart = request.session.get('cart')
        size = request.session.get('size')
        products = Product.get_all_products_by_id(list(cart.keys()))

        if size:
            for product in products:
                if size.get(str(product.id)) is None:
                    status = "not save"
        else:
            status = "not save"

        if status == "save":
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
                    Order.placeOrder(order)

            request.session['cart'] = {}
            request.session['size'] = {}
            return JsonResponse({'status': status})
        else:
            return JsonResponse({'status': status})
