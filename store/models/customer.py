from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):  # saving the data in database self is object from view.py
        self.save()

    def __str__(self):
        return self.first_name

    def isExist(self):
        if Customer.objects.filter(email=self.email) or Customer.objects.filter(phone=self.phone):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_mail(email):

        if Customer.objects.get(email=email):
            return Customer.objects.get(email=email)
        else:
            return False
