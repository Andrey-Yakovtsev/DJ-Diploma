from .cart import Cart
from shop.models import Category

def cart(request):
    return {'cart': Cart(request)}

def category(request):
    return {"parents": Category.objects.filter(parent_category=None)}