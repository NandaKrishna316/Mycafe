from django.urls import path
from . import views
urlpatterns=[
    path('book/', views.book, name='book'),
    path('genere/', views.genere, name='genere'),
    path('view_books/', views.view_books, name='view_books'),
]