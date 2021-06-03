from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.oreders import Order
from django.views import View  # import for class based views
import datetime



class OrderView(View):

    def get(self, request):

        self.date_status={}
        customer = request.session.get('customer_email')
        mail = request.session.get('customer_email')
        if mail:
            currentCustomer = Customer.get_customer_by_mail(mail)

        order = Order.get_order_by_customer(currentCustomer.id)

        # for O in order:
        # #self.date_margin(O.product.id, O.date)


        return  render(request,'orders.html',{'orders':order})


    def date_margin(self,pid,date):

        today = datetime.date.today()
        margin = datetime.timedelta(days=3)

        state = today - margin <= datetime.date(date) <= today + margin
        self.date_status[pid]=state

