"""
 Owner - Hemesh Pratap Singh
 Date - 01/04/2023
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('<h1>Hemesh Pratap Singh </h1><button><a style="color:black;text-decoration: none;background-image: linear-gradient(180deg, black, transparent);" href="https://www.google.com">Google</a></button>')
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def post(request):
    return render(request, 'post.html')


def about(request):
    return render(request, 'about.html')


def remove_cap(request):
    lower = {'lower': request.GET.get('text', 'Default').lower()}
    return render(request, 'new.html', lower)
    # return HttpResponse('Remove caps ' + )
