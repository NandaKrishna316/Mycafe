from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('customer-list', views.customer_list, name='customer_list'),
]