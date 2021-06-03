from django.contrib.sessions import serializers
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View  # import for class based views
from django.contrib.auth.hashers import make_password, check_password
import re
import twilio
import os
from twilio.rest import Client
import random
from django.core import serializers

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):

        otp_code_created = None
        # fetching data from webpage
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lasttname')
        phone = postData.get('phone')
        email = postData.get('Email')
        password = postData.get('password')
        code = postData.get('code')

        if code:  # for verification of code

            # getting otp code from session
            otp_code_created = request.session.get('otp_code')
            # getting customer details from session
            value = request.session.get('current_customer')

            if str(otp_code_created) == code and value:
                self.create_account(value) # creating Account on verification
                return JsonResponse({'status': 'valid'})
            else:
                return JsonResponse({'status': 'invalid'})


        else:
            # Refresh screen data store
            value = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'password':password
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

            if Errormessage:  # error exist

                return JsonResponse({'error': Errormessage})
            else:
                otp_code_created = random.randint(1000, 9999)
                request.session['otp_code'] = otp_code_created
                request.session['current_customer'] = value
                print("sfsfsd", otp_code_created)
                # Phone number Validity
                # Your Account Sid and Auth Token from twilio.com/console
                # and set the environment variables. See http://twil.io/secure
                account_sid = 'AC41fc5ae23648611d4be51f1bf5e1b008'
                auth_token = 'edc9179e44ee543ae7d7518e98366752'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='This is your phone confirmation code : ' + str(otp_code_created),
                    from_='+14243390978',
                    to='+92' + phone
                )

                return JsonResponse({'error': Errormessage})

    def create_account(self, value):
        # Data obtaining
        customer = Customer(first_name=value['first_name'],
                            last_name=value['last_name'],
                            phone=value['phone'],
                            email=value['email'],
                            password=value['password'])

        customer.password = make_password(customer.password)  # encoding the password
        Customer.register(customer)

    def otp_varification(self, opt):
        pass

    def validateCustomer(self, customer):
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


