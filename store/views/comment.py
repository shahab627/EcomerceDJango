from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, JsonResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from  store.models.comments import Comment
from store.models.oreders import Order
from django.views import View  # import for class based views


class RateReview(View):

    # product id obtain by dynamic URL
    def get(self, request,productID):

        comments = Comment.get_Comment(productID)
        data = {}
        data['ProductID'] = productID
        if comments:
            data['Comments'] = comments

        print(comments)
        return render(request, 'RateReview.html', data)


    def post(self, request):

        # --- getting deatails from html thro Ajax----
        name = None
        status ="save"
        currentCustomer=None
        msg = request.POST.get('msg')
        pid = request.POST.get('PID')


        Products = Product.get_all_products_by_id(pid)

        mail = request.session.get('customer_email')
        if mail:
            currentCustomer = Customer.get_customer_by_mail(mail)
            if currentCustomer:
                name = currentCustomer.first_name + " " + currentCustomer.last_name
                # Saving the Data to DataBase

                for P in Products:
                    if str(pid) == str(P.id):
                        myProdcut = P

                comment = Comment(product=myProdcut,
                                  productID=pid,
                                  customerName=name,
                                  customer=currentCustomer,
                                  comment=msg)
                Comment.addComment(comment)
        else:
            status= "error"


        # Updating on Post
        comments = Comment.get_Comment(pid).values()
        commentsData = list(comments)
        return JsonResponse({'status':status, 'CommentsData':commentsData})