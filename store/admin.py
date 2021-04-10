from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.oreders import Order
from .models.rate import Rate
from .models.comments import Comment


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['phone']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order,AdminOrder)
admin.site.register(Rate)
admin.site.register(Comment)
