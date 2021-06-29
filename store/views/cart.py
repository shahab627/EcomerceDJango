from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View  # import for class based views


class Cart(View):

    def get(self, request):
        # fetching items present in cart session from database
        ids = list(request.session.get('cart').keys())
        products = Product.get_all_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})

    def post(self, request):
        p_id = request.POST.get('id')
        cart = request.session.get('cart')
        if p_id is not None:
            del cart[p_id]
            request.session['cart'] = cart

        return JsonResponse({'status': 'done'})
