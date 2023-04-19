"""
 Owner - Hemesh Pratap Singh
 Date - 01/04/2023
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def blog (request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def rooms(request):
    return render(request, 'rooms.html')
