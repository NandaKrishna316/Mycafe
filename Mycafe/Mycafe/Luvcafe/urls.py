from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('your_order/', views.your_order, name='your_order'),
    path('online/', views.online, name='online'),
    path('add_order/', views.add_order, name='add_order'),
    path('signup/', views.signup, name='signup'),
    path('menu/', views.menu, name='menu'),
    path('complaint/', views.complaint, name='complaint'),
    path('complaint_s/', views.complaint_s, name='complaint_s'),
    path('signin/', views.signin, name='signin'),
]