from .customer import Customer
from .product import Product
from django.db import models


class Rate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    productName = models.CharField(max_length=50, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    @staticmethod
    def get_ratting(Product_name,Customer):
            return Rate.objects.filter(productName=Product_name, customer=Customer)

