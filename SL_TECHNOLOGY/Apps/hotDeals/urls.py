from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotDeals, name='hotDeals')
]
