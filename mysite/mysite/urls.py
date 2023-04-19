from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('remove_cap', views.remove_cap,name='rmv'),
    path('contact', views.contact,name='contact'),
    path('post', views.post,name='post'),
    path('about', views.about,name='about'),
]
