from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.

def index(request):
    products = Product.objects.all()
    n = len(products)
    nslides = n // 4 + ceil((n / 4) - (n // 4))
    allprod = []
    categories = Product.objects.values('product_category')
    cats = { item['product_category'] for item in categories }
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprod.append([prod,range(1,nslides)])

    # param = {'product': products, 'no_slides': nslides, 'range': range(1,nslides)}
    # allprod = [[products,range(1,nslides)],
    #            [products,range(1,nslides)]]
    param = {'allprods':allprod}
    # return HttpResponse("SHOP INDEX")
    return render(request, 'shop/index.html',param)


def about(request):
    # return HttpResponse("SHOP INDEX")
    return render(request, 'shop/about.html')

def cart(request):
    # return HttpResponse("SHOP INDEX")
    return render(request, 'shop/cart.html')