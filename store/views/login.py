from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View  # import for class based views
from django.contrib.auth.hashers import make_password, check_password


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('Email')
        password = request.POST.get('password')
        print(password, email)

        customer = Customer.get_customer_by_mail(email)

        Errormessage = None

        if customer:

            flag = check_password(password, customer.password)

            if flag:
                # creating session to remember user name, email
                request.session['customer_id']=customer.id
                request.session['customer_email']= customer.email
                return redirect('Homepage')
            else:
                Errormessage = " Password or Email not Valid !!"

        else:
            Errormessage = " Password or Email not Valid !!"

        return render(request, 'login.html', {'error': Errormessage})

def logout(request):
    request.session.clear()
    print("fffffffhello")
    return redirect('login')