from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    small = models.BooleanField(default= False)
    large = models.BooleanField(default=False)
    small = models.BooleanField(default=False)
    small = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='',null= True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')\

    @staticmethod
    def get_all_products():
        return  Product.objects.all()

    @staticmethod
    def get_all_products_by_id(id):
        return Product.objects.filter(id__in = id)
    @staticmethod
    def get_all_products_by_category( category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()
