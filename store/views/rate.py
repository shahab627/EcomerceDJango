from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.rate import Rate
from store.models.comments import Comment
from store.models.oreders import Order
from django.views import View  # import for class based views


class RateItem(View):

    # product id obtain by dynamic URL
    def get(self, request, productID):

        return render(request, 'RateReview.html')

    def post(self, request):

        # --- getting deatails from html thro Ajax----

        currentCustomer = None
        ratting = request.POST.get('ratting')
        pid = request.POST.get('PID')
        Products = Product.get_product_by_id(pid)

        mail = request.session.get('customer_email')
        if mail:
            currentCustomer = Customer.get_customer_by_mail(mail)

            rate = Rate(product=Products,
                        customer=currentCustomer,
                        rating=ratting)

            check = self.check_ratting(pid, currentCustomer.id)  # checking if ratting exists
            if check:
                Rate.update_ratting(pid, currentCustomer.id, ratting)  # update ratting
            else:
                Rate.add_ratting(rate)

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'not save'})

    def check_ratting(self, product_id, customer):
        return Rate.check_ratting(product_id, customer)
