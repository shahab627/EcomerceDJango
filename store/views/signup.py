from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View  # import for class based views
from django.contrib.auth.hashers import make_password, check_password
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'





class SignUp(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        # fetching data from webpage
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lasttname')
        phone = postData.get('phone')
        email = postData.get('Email')
        password = postData.get('password')

        # Refresh screen data store
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        # Data obtaining
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        # Filed check
        Errormessage = None
        Errormessage = self.validateCustomer(customer)

        # Saving Data
        Data = {
            'error': Errormessage,
            'Values': value
        }

        if not Errormessage:
            customer.password = make_password(customer.password)  # encoding the password

            Customer.register(customer)
            return redirect('Homepage')
        else:
            return render(request, 'signup.html', Data)

    def validateCustomer(self,customer):
        Errormessage = None

        if not customer.first_name:
            Errormessage = "First Name Field Empty !!"

        elif not customer.last_name:
            Errormessage = "Last Name Field Empty !!"

        elif not customer.password:
            Errormessage = "Password Field Empty !!"

        elif not customer.email:
            Errormessage = "Email Field Empty !!"

        elif not customer.phone:
            Errormessage = "Phone Field Empty !!"

        elif len(customer.phone) < 10:
            Errormessage = "Phone Number not valid !"

        elif len(customer.password) < 5:
            Errormessage = "Password Length smaller then 5 !"
        elif not (re.search(regex, customer.email)):
            Errormessage = "Email not Valid"
        elif Customer.isExist(customer):
            Errormessage = "Email or Phone Number exist Already !"
        return Errormessage