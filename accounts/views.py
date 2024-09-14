from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in.")
            return redirect('dashboard')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, "User does not exist. Please register.")
                print("Redirecting to register...")
                return redirect('register')
            else:
                messages.error(request, "Invalid login credentials")
                print("Invalid credentials")
                return redirect('login')
    return render(request, 'accounts/logreg.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are successfully logged out.")
        return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'Please fill out all fields.')
            return redirect('register')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email address already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'You are registered successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

# @login_required(login_url='login')
def dashboard(request):
    return render(request, 'Pages/index.html')
