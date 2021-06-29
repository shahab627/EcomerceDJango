from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.rate import Rate
from django.views import View  # import for class based views
from django.contrib.auth.hashers import make_password, check_password


class Index(View):

    def get(self, request):
        # checking if cart contain items for condition statements in home
        cart = request.session.get('cart')
        top_items=[]
        category_items =[]
        count =0
        if not cart:
            request.session['cart'] = {}

        # getting top rated items

        items = Rate.get_all_ratting().values()

        for p in items:
            top_items.append(Product.get_product_by_id(str(p.get('product_id'))))

        splitedSize = 4
        splited = [top_items[x:x + splitedSize] for x in range(0, len(top_items), splitedSize)]

        prds = None
        categ = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            prds = Product.get_all_products_by_category(categoryId)
        else:
            prds = Product.get_all_products()

        # applying category carousal split
        for c in categ:
            category_items.append(c)

        category_splited = [category_items[x:x + 3] for x in range(0, len(category_items), 3)]

        # Applying pagination
        paginator = Paginator(prds, 8)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Getiing user detail from session
        currentCustomer = None
        mail = request.session.get('customer_email')
        if mail:
            currentCustomer = Customer.get_customer_by_mail(mail)

        # -Post Data-------------------------------
        data = {}
        data['products'] = page_obj
        data['categories'] = categ
        data['currentCustomer'] = currentCustomer
        data['trending'] = splited
        data['trending-range'] = 4

        return render(request, 'index.html', data)

    def post(self, request):

        data = request.POST.get('size')  # getting size through ajax
        productId = request.POST.get('productId')  # getting product id from index page on click
        cart_Remove = request.POST.get('cartRemove')  # return true if we press - button on Home

        # size---------------------------------------------
        size = request.session.get('size')

        if data is not None:
            items = data.split('-')
            if size:
                size[items[1]] = items[0]
            else:
                size = {}
                size[items[1]] = items[0]

        request.session['size'] = size

        # -----------------------------------------------
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
