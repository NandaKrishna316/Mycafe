from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def customer_list(request):
    return render(request, 'customer_list.html')