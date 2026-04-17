from django.shortcuts import render
from .models import Book,Theme

def book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        published_date = request.POST.get('published_date')

        Book.objects.create(title=title, author=author, price=price, published_date=published_date)

    return render(request, 'book.html')

def genere(request):
    if request.method == 'GET':
        genere = request.GET.get('genere')
        discription = request.GET.get('discription')
        if genere and discription:
            Theme.objects.create(genere=genere, discription=discription)
    return render(request, 'genere.html')

def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books' : books})
