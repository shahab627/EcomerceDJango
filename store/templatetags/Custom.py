from django import  template

register = template.Library()

@register.filter(name = 'Currency')  #providing quantity to index page
def Currency(number):
    return "Rs "+str(number)