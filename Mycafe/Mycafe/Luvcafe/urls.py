from django.urls import path,include
from . import views

urlpatterns = [
    path('admin_page/', views.admin_page, name='admin_page'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('add_order/', views.add_order, name='add_order'),
    path('your_order/', views.your_order, name='your_order'),
    path('complaint_s/', views.complaint_s, name='complaint_s'),

    path('', views.home_page, name='home_page'),
    path('online/', views.online, name='online'),
    path('signup/', views.signup, name='signup'),
    path('complaint/', views.complaint, name='complaint'),
    path('signin/', views.signin, name='signin'),
    path('menu/', views.menu, name='menu'),
    path('your_cart/', views.your_cart, name='your_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('public_menu/', views.public_menu, name='public_menu'),
]