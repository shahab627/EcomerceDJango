from .customer import Customer
from .product import Product
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Rate(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(default='0', null=True, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return str(self.rating)

    @staticmethod
    def get_all_ratting():
        return Rate.objects.all().order_by('-rating')

    @staticmethod
    def get_ratting(Product_Id):
        return Rate.objects.filter(product_id=Product_Id)

    @staticmethod
    def check_ratting(Product_Id, customer):
        return Rate.objects.filter(product_id=Product_Id, customer_id=customer)

    @staticmethod
    def update_ratting(product_id, customer, new_rate):
        return Rate.objects.filter(product_id=product_id, customer_id=customer).update(rating=new_rate)

    def add_ratting(self):
        self.save()
