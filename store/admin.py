from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.oreders import Order
from .models.oreders import Order_Customer,all_orders
from .models.rate import Rate
from .models.comments import Comment


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminOrder(admin.ModelAdmin):
    list_display = ['customer', 'phone', 'address', 'size', 'date', 'status', 'price']


class AdminComment(admin.ModelAdmin):
    list_display = ['product', 'customer', 'comment', 'date']

class AdminRatting(admin.ModelAdmin):
    list_display = ['product', 'customer', 'rating']

class AdminCustomerOrders(admin.ModelAdmin):
    list_display = ['customer','products_ordered', 'phone', 'address', 'size', 'date', 'status', 'price']

class AdminCustomerAllOrders(admin.ModelAdmin):
    list_display = ['customer','order', 'phone', 'address', 'date', 'price']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
admin.site.register(Rate,AdminRatting)
admin.site.register(Comment, AdminComment)
admin.site.register(Order_Customer, AdminCustomerOrders)
admin.site.register(all_orders, AdminCustomerAllOrders)
