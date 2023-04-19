from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('pos/<str:id>/', views.pos,name='pos'),
]
