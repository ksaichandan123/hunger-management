from django.shortcuts import render
from foodstore.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {'products': products, }
    return render(request, 'home.html',context)
