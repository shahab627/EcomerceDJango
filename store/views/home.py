from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View  # import for class based views
from django.contrib.auth.hashers import make_password, check_password


class Index(View):

    def get(self, request):
        # checking if cart contain items for condition statements in home
        cart =request.session.get('cart')
        if not cart:
            request.session['cart']={}


        prds = None
        categ = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            prds = Product.get_all_products_by_category(categoryId)
        else:
            prds = Product.get_all_products()

        # Getiing user detail from session
        currentCustomer =None
        mail = request.session.get('customer_email')
        if mail:
            currentCustomer=Customer.get_customer_by_mail(mail)

        #--------------------------------
        data = {}
        data['products'] = prds
        data['categories'] = categ
        data['currentCustomer'] = currentCustomer


        # return render(request,'orders.html')
        return render(request, 'index.html', data)



    def post(self, request):

        data = request.POST.get('size')   # getting size through ajax
        productId = request.POST.get('productId')  # getting product id from index page on click
        cart_Remove = request.POST.get('cartRemove') # return true if we press - button on Home

        # size---------------------------------------------
        size = request.session.get('size')
        print(size)

        if data is not None:
            items = data.split('-')
            if size:
                size[items[1]] = items[0]
            else:
                size = {}
                size[items[1]] = items[0]

        request.session['size'] = size

        #-----------------------------------------------
        # handling cart and quantity
        if productId is not None:

            cart = request.session.get('cart')
            print(cart, type(productId), productId)

            if cart:
                quantity = cart.get(productId)
                if quantity:
                    if cart_Remove:
                        if quantity <= 1:
                            cart.pop(productId)
                        else:
                            cart[productId] = quantity - 1
                    else:
                        cart[productId] = quantity + 1
                else:
                    cart[productId] = 1
            else:
                cart = {}
                cart[productId] = 1

            request.session['cart'] = cart


        return redirect('Homepage')
