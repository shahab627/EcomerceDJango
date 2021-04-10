import datetime
from .customer import Customer
from .product import Product
from django.db import models


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productID = models.IntegerField(default=0)
    customerName = models.CharField(max_length=50,default='Anonymous ')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.datetime.today)
    comment = models.TextField(max_length=200,default='')

    @staticmethod
    def get_Comment(Product_Id):
            return Comment.objects.filter(productID=Product_Id)

    def addComment(self):
        self.save()
