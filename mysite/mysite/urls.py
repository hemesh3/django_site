from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about,name='about_us'),
    path('contact/', views.contact,name='contact'),
    path('rooms/', views.rooms,name='rooms'),
    path('gallery/', views.gallery,name='gallery'),
    path('blog/', views.blog,name='blog'),
]
