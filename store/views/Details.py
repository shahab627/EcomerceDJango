from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View  # import for class based views
from django.contrib.auth.hashers import make_password, check_password


class Details(View):

    def get(self, request, productID):

        product = Product.get_product_by_id(productID)
        data = {}
        data['product'] = product

        return render(request, 'details.html',data)



    def post(self, request):

        Quantity = request.POST.get('quanity')
        pid = request.POST.get('id')
        SizeSelected = request.POST.get('size')


        # size---------------------------------------------
        if SizeSelected:
            size = request.session.get('size')

            if size:
                size[pid] = SizeSelected
            else:
                size = {}
                size[pid] = SizeSelected

            request.session['size'] = size
        # Cart---------------------------------------------

        cart = request.session.get('cart')
        if cart:
            cart[pid] = int(Quantity)
        else:
            cart = {}
            cart[pid] = int(Quantity)

        request.session['cart'] = cart



        return JsonResponse({'status': 'save'})
