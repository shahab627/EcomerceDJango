from django import  template

register = template.Library()

@register.filter(name = 'Currency')  #providing quantity to index page
def Currency(number):
    return "Rs "+str(number)

@register.filter(name = 'Total_Order')  #providing quantity to index page
def Total_Order(number1,number2):
    return number1*number2