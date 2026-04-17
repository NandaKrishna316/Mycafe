from django.shortcuts import render
from .models import Tastes, register, Complaint
from django.shortcuts import redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login

def home_page(request):
    return render(request, 'home_page.html')


def your_order(request):
    orders = Tastes.objects.all()
    return render(request, 'your_order.html', {'orders': orders})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        home_address = request.POST.get('home_address')
        contact_number = request.POST.get('contact_number')

        if register.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        register.objects.create_user(username=username, email=email, password=password,home_address=home_address, contact_number=contact_number)
        return redirect('signin') 
    return render(request, 'signup.html')


def add_order(request):
    if not request.user.is_superuser:
         return redirect('home_page')
    if request.method == 'POST':
        tastes = request.POST.get('tastes')
        price = request.POST.get('price')

        Tastes.objects.create(tastes=tastes, price=price)
        return redirect('your_order')
    return render(request, 'add_order.html')


def online(request):
    return render(request, 'online.html')


def complaint(request):
    if request.method == 'POST':
        complaint_text = request.POST.get('complaint')
        Complaint.objects.create(complaint_text=complaint_text)

            # You can save the complaint to the database or send it via email here
    return render(request, 'complaint.html')


def complaint_s(request):
    if request.user.is_superuser:
        complaints = Complaint.objects.all()
        return render(request, 'complaint_s.html', {'complaints': complaints})
    else:
        return redirect('home_page')


def admin_page(request):
    if request.user.is_superuser:
        return render(request, 'admin_page.html')
    else:
        return redirect('home_page')


def signin(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Authenticate the user (you can use Django's built-in authentication system)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)

                if request.user.is_superuser:
                    return render(request, 'admin_page.html')
                else:
                    return redirect('online')  # Redirect to a success page after login
            else:
                form.add_error(None, "Invalid username or password")
            

    else:
        form = loginForm()
    return render(request, 'signin.html', {"form": form})
